from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth
from models import Candidates, session, Students, Images

app = Flask(__name__)
app = Flask(__name__.split('.')[0])
api = Api(app)
auth = HTTPBasicAuth()



# @app.route('/account/<id>', methods=['POST'])
# def create_account(id, usrname, pwd):
#     user = request.form[
#         {
#             "password": user.password

#         }
#     ]
        


@app.route('/student/<id>', methods=['GET'])
def get_student(id):
    try:
        student = session.query(Students).filter_by(student_id=id).first()
        result = {
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
        return jsonify(result)
    except Exception as e:
        print(e)
    

    
@app.route('/students', methods=['GET'])
def all_student():
    returnInfo = []
    try:
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
    except Exception as e:
        print(e)
    
    

@app.route('/image/<id>', methods=['GET'])
def get_image(id):
    try:
        image = session.query(Images).filter_by(image_id=id)
        result = {
            "image_url": image.image_url
        }
        return jsonify(result)
    except Exception as e:
        print(e)
    
    

# getting all images route
@app.route('/images', methods=['GET'])
def all_images():
    returnInfo = []
    try:
        images = session.query(Images).all()
        for image in images:
            returnInfo.append(
                {
                    "image_url": image.image_url,
                }
            )
        results = {
            "all images": returnInfo
        }
        return jsonify(results)
    except Exception as e:
        print(e)

    

@app.route('/candidate/<id>', methods=['GET'])
def get_candidate(id):
    try:
        candidate = session.query(Candidates).filter_by(candidate_id=id).first()
        result = {
            "candidate_student_id": candidate.student_id
        }
        return jsonify(result)
    except Exception as e:
        print(e)

    

@app.route('/candidates', methods=['GET'])
def all_candidates():
    returnInfo = []
    try:
        candidates = session.query(Candidates).all()
        for candidate in candidates:
            returnInfo.append(
                {
                    "candidates_students_id": candidate.student_id
                }
            )
        results = {
            "candidates": returnInfo
        }
        return jsonify(results)
    except Exception as e:
        print(e)



if __name__ == '__main__':
    app.run(debug=True)