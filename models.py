from sqlalchemy import create_engine, String, Integer, Date, ForeignKey, Column
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import psycopg2


# db dependecies instanciations
engine = create_engine('postgresql+psycopg2://postgres:NexusDatabase@nexus-database.cwt8zh4gaxtg.us-east-1.rds.amazonaws.com/nexus_database')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
Base = declarative_base()


# Database connection and creation
def database_connect():
    try:
        if engine.connect():
            Base.metadata.create_all(engine)
            print("Database Created")
        else:
            print('could not establish connection')
    except Exception as e:
        print(f'Could not create database: {e}')

# conection init      
database_connect()

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
    college = Column('college', String(255), nullable=False)
    department = Column('department', String(255), nullable=False)

    # one-to-one relation
    child1 = relationship("Images", uselist=False)
    child2 = relationship("Candidates", uselist=False)


    # class instance
    def __init__(self, username, first_name, last_name, gender, phone_number, dob, level, email, college, department):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self. phone_number = phone_number
        self.dob = dob
        self.level = level
        self.email = email
        self.college = college
        self.department = department


# Images table model
class Images(Base):
    __tablename__ = "images"

    # columns
    image_id = Column('image_id', Integer, primary_key=True, nullable=False)
    image_url = Column('image_url', String(255), nullable=False)
    student_id = Column('student_id', Integer, ForeignKey("student.student_id")) # student reference

    # many-to-one relation
    parent = relationship("Students", back_populates="child1")
    

    # class instance
    def __init__(self, image_url):
        self.image_url = image_url


# candidate table model
class Candidates(Base):
    __tablename__ = "candidate"

    # columns
    candidate_id = Column('candidate_id', Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey("student.student_id")) # student reference

    # many-to-one relation
    parent = relationship("Students", back_populates="child2")
    
    
    # class instance
    def __init__(self):
        pass