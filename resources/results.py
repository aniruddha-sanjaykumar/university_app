from flask_restful import Resource
from flask import jsonify, request
from Model import results


class Result(Resource):
    """
    APIs and methods related to Results resource.
    """
    def get(self, id):
        """
        GET API to fetch the results of a particular exam.
        :param id: exam id
        :return: exam results
        """
        try:
            student_id = request.args.get('id', default=None, type=str)
            if id in results:
                if student_id:
                    for result in results[id]:
                        if student_id == result['student_id']:
                            return jsonify([result])
                return jsonify(results[id])
            else:
                return {'message': 'No resource found'}, 404

        except Exception as e:
            return {'message': 'Internal Server error', 'error': e}, 500

    def post(self, id):
        """
        POST API to add results for a particular exam.
        :param id: exam id
        :return: JSON message to indicate the success/failure of adding results.
        """
        try:
            json_data = request.get_json(force=True)
            if not json_data:
                return {'message': 'No input data provided'}, 400

            if id in results:
                results[id] += [json_data]
            else:
                results[id] = [json_data]
            return {'message': 'Result added successfully'}, 200

        except Exception as e:
            return {'message': 'Internal Server error', 'error': e}, 500
