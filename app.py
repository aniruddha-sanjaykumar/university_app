from flask import Blueprint
from flask_restful import Api
from resources.courses import Course
from resources.students import Student
from resources.exams import Exam
from resources.results import Result

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(Course, '/courses')
api.add_resource(Student, '/students')
api.add_resource(Exam, '/exams', '/exams/<string:id>')
api.add_resource(Result, '/exams/<string:id>/results')
