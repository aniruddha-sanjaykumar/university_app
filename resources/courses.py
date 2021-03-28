from flask_restful import Resource
from flask import jsonify, request
from Model import courses


class Course(Resource):
    """
    APIs and methods related to Courses resource.
    """
    def get(self):
        """
        GET API to fetch the courses based on id and name parameters.
        :return: list of courses.
        """
        try:
            course_id = request.args.get('id', default=None, type=str)
            course_name = request.args.get('name', default=None, type=str)

            if course_id:
                if course_id in courses:
                    return jsonify([courses[course_id]])
                else:
                    return {'message': 'No resource found'}, 404

            if course_name:
                response = []
                for item in courses.values():
                    if course_name.lower() in item['name'].lower():
                        response.append(item)
                return jsonify(response)

            return jsonify(list(courses.values()))
        except Exception as e:
            return {'message': 'Internal Server error', 'error': e}, 500

    def post(self):
        """
        POST API to add new courses.
        :return: JSON message to indicate the success/failure of adding new course.
        """
        try:
            json_data = request.get_json(force=True)
            if not json_data:
                return {'message': 'No input data provided'}, 400

            if 'id' not in json_data:
                return {'message': 'Invalid input data provided'}, 422

            courses[json_data['id']] = json_data
            return {'message': 'Course added successfully'}, 200

        except Exception as e:
            return {'message': 'Internal Server error', 'error': e}, 500


