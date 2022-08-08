from flask import Flask, jsonify
from models import Candidates, session, Students, Images

app = Flask(__name__)
app = Flask(__name__.split('.')[0])


@app.route('/student/<id>', methods=['GET'])
def get_student(student_id):
    pass           


@app.route('/students', methods=['GET'])
def all_student():
    returnInfo = []
    students = session.query(Students).all()
    for student in students:
        returnInfo.append(
            {
                "username":student.username,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "gender": student.gender,
                "phonenumber": student.phone_number,
                "dob": student.dob,
                "level": student.level,
                "email": student.email,
                "college": student.college,
                "department": student.department
            }
        )
    results = {
        "all students": returnInfo
    }

    return jsonify(results)


@app.route('/images', methods=['GET'])
def all_images():
    returnInfo = []
    images = session.query(Images).all()
    for image in images:
        returnInfo.append(
            {
                "image_url": image.image_url
            }
        )
    results = {
        "all images": returnInfo
    }

    return jsonify(results)


@app.route('/candidates', methods=['GET'])
def all_candidates():
    returnInfo = []
    candidates = session.query(Candidates).all()
    for candidate in candidates:
        returnInfo.append(
            {
                "candidates": candidate.student_id
            }
        )
    results = {
        "candidates": returnInfo
    }

    return jsonify(results)
if __name__ == '__main__':
    app.run(debug=True)