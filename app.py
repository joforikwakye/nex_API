import json
from flask import Flask, jsonify, request
from models import Candidates, session, Students, Images
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app = Flask(__name__.split('.')[0])
 

@app.route('/login', methods=['POST'])
def login():
    d = {}
    username = request.json['username']
    password = request.json['password']

    student = session.query(Students).filter_by(username=username).first()
    if student:
            verify = check_password_hash(pwhash=student.password, password=password)
            if verify:
                result = {
                    'student_id': student.student_id,
                    'status': 'Login successful'
                } 
                return jsonify(result)

            else:    
                    d['status'] = 'Incorrect username or password'
                    return jsonify(d)
    else:
            d['status'] = 'Username does not exist'
            return jsonify(d)


@app.route('/student/<id>', methods=['GET'])
def get_student(id):
    try:
        student_name = session.query(Students).filter_by(student_id=id).first()
        student_image = session.query(Images).filter_by(student_id = id).first()

        result = {
           'first_name': student_name.first_name,
           'image': student_image.image_url
        }    
        return jsonify(result)
    except Exception as e:
        print(e)



@app.route('/student_update/<id>', methods=['PUT'])
def update_student(id):
    try:
        student = session.query(Students).filter_by(student_id=id).first()
        
        if student:
            password = request.json['password']

            pwd_hash = generate_password_hash(password=password)
            student.password = pwd_hash
        
            session.commit()
        else:
            print("Student does not exist")
            
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
        image = session.query(Images).filter_by(student_id=id).first()
        result = {
            "image_url": image.image_url
        }
        return jsonify(result)
    except Exception as e:
        return 'does not work'
    
    

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


if __name__ == '__main__':
    app.run(debug=True)