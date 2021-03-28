# To keep the application simple, I have gone with a simple non persistent data approach.
# In real life, this file would contain DB models and schemas. This is only for demo purposes.


courses = {
    "physics101": {"name": "Physics - 101",
                   "id": "physics101",
                   "instructor": "John",
                   "exams": ["physics101-i1"],
                   "students": ["uni2021001"]
                   },
    "chemistry101": {"name": "Chemistry - 101",
                     "id": "chemistry101",
                     "instructor": "Alex",
                     "exams": [],
                     "students": ["uni2021002"]
                     }

}

students = {
    "uni2021001": {"name": "Justin",
                   "id": "uni2021001",
                   "courses": ["physics101"],
                   "exams": ["physics101-i1"]
                   },
    "uni2021002": {"name": "Bob",
                   "id": "uni2021002",
                   "courses": ["chemistry101"],
                   "exams": []
                   }
}

exams = {
    "physics101-i1": {"name": "Physics Internals 1",
                      "id": "physics101-i1",
                      "course_id": "physics101",
                      "max_marks": 100,
                     }
}

results = {
    "physics101-i1": [{"student_id": "uni2021001", "marks_scored": 60, "result": "Pass"}]
}

