This is a minimalistic demo application built for an university to track students and courses offered.

Project Requirements:

1. python 3
2. virtualenv  --> pip install virtualenv (Installation command)

Setup Steps:

Step1 : `git clone https://github.com/aniruddha-sanjaykumar/university_app.git`

Clone the repository and cd(change directory) to the repository base folder.

Step2 : `python3 -m venv env`

Create a virtual environment.

Step3: `source env/bin/activate`

Activate the virtual environment just created.

Step4: `pip install -r requirements.txt`

Install dependencies.

Step5: `python run.py`

Start the server. 

The application runs on http://127.0.0.1:5000/ by default.

API endpoints supported:

GET /app/courses --> Get list of courses (id, name --> url params).

Sample call: `GET http://127.0.0.1:5000/app/courses`

POST /app/courses --> Add a new course.

Sample call: `POST http://127.0.0.1:5000/app/courses`

Sample request body:
`{
        "id": "chemistry102",
        "instructor": "Alex",
        "name": "Chemistry - 102",
}`

GET /app/students --> Get list of students (id, name --> url params).

Sample call: `GET http://127.0.0.1:5000/app/students` 

POST /app/students --> Add a new student.

Sample call: `POST http://127.0.0.1:5000/app/students`

Sample request body:
`{
        "courses": [
            "chemistry101"
        ],
        "id": "uni2021002",
        "name": "Bob"
    }`

PUT /app/students --> Enroll student to new course.

Sample call: `PUT http://127.0.0.1:5000/app/students`

Sample request body:
`{
        "courses": [
            "physics101"
        ],
        "id": "uni2021002",
        "name": "Bob"
    }`
    
GET /app/exams --> Get list of exams. 

Sample call: `GET http://127.0.0.1:5000/app/exams`

POST /app/exams --> Add a new exam.

Sample call: `POST http://127.0.0.1:5000/app/exams`

GET /app/exams/<id> --> Get a particular exam using id.

Sample call: `GET http://127.0.0.1:5000/app/exams/physics101-i1`

GET /app/exams/<id>/results --> Get exam results.

Sample call: `GET http://127.0.0.1:5000/app/exams/physics101-i1/results`

POST /app/exams/<id>/results --> Post result for an exam.

Sample call: `POST http://127.0.0.1:5000/app/exams/physics101-i2/results`

Sample request body: 
`{
        "marks_scored": 60,
        "result": "Pass",
        "student_id": "uni2021001"
}`
