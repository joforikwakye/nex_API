from sqlalchemy import create_engine, String, Integer, Date, ForeignKey, Column
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


# db dependecies instanciations
engine = create_engine('')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
Base = declarative_base()


# Database connection and creation
def database_connect(engine, session):
    try:
        if engine.connect():
            Base.metadata.create_all(session)
            print("Database Created")
        else:
            print("Could not connect to database")
    except Exception as e:
        print(f'Could not create database: {e}')
        

# student table model
class Students(Base):
    __tablename__ = "student"

    # columns
    student_id = Column('student_id', Integer, primary_key=True, nullable=False)
    username = Column('username', String(255), nullable=False)
    first_name = Column('first_name', String(255), nullable=False)
    last_name = Column('last_name', String(255), nullable=False)
    gender = Column('gender', String(255), nullable=False)
    phone_number = Column('phone_number', String(255), nullable=False)
    dob = Column('dob', Date, nullable=False)
    level = Column('level', nullable=False)
    email = Column('email', String(255), nullable=False)

    # one-to-many relation
    children = relationship("Images", "Department", "College", "Candidate", back_populates="student")


    def __repr__(self):
        return f"""
        username = {self.student_id}
        firstname = {self.first_name}
        lastname = {self.last_name}
        gender = {self.gender}
        phonenumber = {self.phone_number}
        dob = {self.dob}
        level = {self.level}
        email = {self.email}
        """


# Images table model
class Images(Base):
    __tablename = "images"

    # columns
    image_id = Column('image_id', Integer, primary_key=True, nullable=False)
    image_url = Column('image_url', String(255), nullable=False)
    student_id = Column('student_id', Integer, ForeignKey("student.id")) # student reference

    # many-to-one relation
    parent = relationship("Student", back_populates="children")


    def __repr__(self):
        return f"""
        username = {self.image_url}
        """


# college table model
class College(Base):
    __tablename__ = "college"

    # columns
    college_id = Column('college_id', Integer, primary_key=True, nullable=False)
    college_name = Column('college_name', String(255), nullable=False)
    student_id = Column('student_id', Integer, ForeignKey("student.id")) # student reference

    # one-to-many relation
    child = relationship("Department", back_populates="college")

    # many-to-one relation
    parent = relationship("Student", back_populates="children")

    
    def __repr__(self):
        return f"""
        username = {self.college_name}
        """

    

# department table model
class Department(Base):
    __tablename__ = "department"

    # columns
    dept_id = Column('dept_id', Integer, primary_key=True, nullable=False)
    college_id = Column('college_id', Integer, ForeignKey("college.id"))  # college 
    dept_name = Column('dept_name', String, nullable=False)
    student_id = Column('student_id', Integer, ForeignKey("student.id"))

    # many-to-one relation
    parent = relationship("College", back_populates="child")
    


# candidate table model
class Candidate(Base):
    __tablename__ = "candidate"

    # columns
    candidate_id = Column('candidate_id', Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey("student.id")) # student reference