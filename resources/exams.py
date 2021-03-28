from flask_restful import Resource
from flask import jsonify, request
from Model import exams, courses, students


class Exam(Resource):
    """
    APIs and methods related to Exams resource.
    """
    def get(self, id=""):
        """
        GET API to fetch the exams data based on id parameter.
        :param id: exam id
        :return: list of exams or particular exam data if id is not null.
        """
        try:
            if id:
                if id in exams:
                    return jsonify(exams[id])
                else:
                    return {'message': 'No resource found'}, 404

            return jsonify(list(exams.values()))
        except Exception as e:
            return {'message': 'Internal Server error', 'error': e}, 500

    def post(self):
        """
        POST API to add new exams.
        :return: JSON message to indicate the success/failure of adding new exam.
        """
        try:
            json_data = request.get_json(force=True)
            if not json_data:
                return {'message': 'No input data provided'}, 400

            if 'id' not in json_data:
                return {'message': 'Invalid input data provided'}, 422

            if json_data['course_id'] not in courses:
                return {'message': 'Invalid input of course id provided'}, 422

            if 'exams' in courses[json_data['course_id']]:
                courses[json_data['course_id']]['exams'].append(json_data['id'])
            else:
                courses[json_data['course_id']]['exams'] = [json_data['id']]

            for student in students.values():
                if json_data['course_id'] in student['courses']:
                    if 'exams' in student:
                        student['exams'].append(json_data['id'])
                    else:
                        student['exams'] = [json_data['id']]

            exams[json_data['id']] = json_data
            return {'message': 'Exam added successfully'}, 200

        except Exception as e:
            return {'message': 'Internal Server error', 'error': e}, 500
