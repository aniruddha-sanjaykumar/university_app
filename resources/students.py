from flask_restful import Resource
from flask import jsonify, request
from Model import students, courses


class Student(Resource):
    """
    APIs and methods related to Students resource.
    """
    def get(self):
        """
        GET API to fetch the students data based on id and name parameters.
        :return: list of students.
        """
        try:
            student_id = request.args.get('id', default=None, type=str)
            student_name = request.args.get('name', default=None, type=str)

            if student_id:
                if student_id in students:
                    return jsonify([students[student_id]])
                else:
                    return {'message': 'No resource found'}, 404

            if student_name:
                response = []
                for item in students.values():
                    if student_name.lower() in item['name'].lower():
                        response.append(item)
                return jsonify(response)

            return jsonify(list(students.values()))
        except Exception as e:
            return {'message': 'Internal Server error', 'error': e}, 500

    def post(self):
        """
        POST API to add new students.
        :return: JSON message to indicate the success/failure of adding new student.
        """
        try:
            json_data = request.get_json(force=True)
            if not json_data:
                return {'message': 'No input data provided'}, 400

            if 'courses' not in json_data:
                return {'message': 'Invalid input data provided. courses key missing'}, 422

            if 'id' not in json_data:
                return {'message': 'Invalid input data provided'}, 422

            if json_data["courses"]:
                for course_id in json_data["courses"]:
                    if course_id in courses:
                        courses[course_id]["students"].append(json_data['id'])
                    else:
                        return {'message': 'Invalid input of course names provided'}, 422

            students[json_data['id']] = json_data
            return {'message': 'Student added successfully'}, 200

        except Exception as e:
            return {'message': 'Internal Server error', 'error': e}, 500

    def put(self):
        """
        PUT API to enroll students to new courses.
        :return: JSON message to indicate the success/failure of enrolling student to new course.
        """
        try:
            json_data = request.get_json(force=True)
            if not json_data:
                return {'message': 'No input data provided'}, 400

            if 'courses' not in json_data:
                return {'message': 'Invalid input data provided. courses key missing'}, 422

            if 'id' not in json_data:
                return {'message': 'Invalid input data provided'}, 422

            if json_data["courses"]:
                for course_id in json_data["courses"]:
                    if course_id in courses:
                        courses[course_id]["students"].append(json_data['id'])
                    else:
                        return {'message': 'Invalid input of course names provided'}, 422

            students[json_data['id']]['courses'] += json_data['courses']
            return {'message': 'Student enrolled successfully'}, 200

        except Exception as e:
            return {'message': 'Internal Server error', 'error': e}, 500
