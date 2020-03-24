import sqlite3
from Models.Applicant import Applicant
import os.path


class ApplicantRepository:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "../database.db")
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def create(self, applicant_details):
        applicant = Applicant()
        applicant_tuple = tuple(values for keys, values in applicant_details.items())

        self.connection.execute(
            '''INSERT INTO applicant( email_id, name, dob, gender, age, tel_no, experience, password )VALUES (?, ?, ?, ?, ?, ?, ?, ?);''',
            applicant_tuple)
        applicant.email_id = applicant_details['email_id']
        applicant.name = applicant_details['name']
        applicant.dob = applicant_details['dob']
        applicant.gender = applicant_details['gender']
        applicant.age = applicant_details['age']
        applicant.tel_no = applicant_details['tel_no']
        applicant.experience = applicant_details['experience']
        applicant.password = applicant_details['password']

        self.connection.commit()

        return applicant

    def get(self, email_id, password):
        applicant = Applicant()
        self.cursor.execute('''SELECT * FROM applicant WHERE email_id = ? AND password = ?''', (email_id, password))
        result = self.cursor.fetchone()
        if result is None:
            return None
        else:
            applicant.email_id = result[0]
            applicant.name = result[1]
            applicant.dob = result[2]
            applicant.gender = result[3]
            applicant.age = result[4]
            applicant.tel_no = result[5]
            applicant.experience = result[6]
            applicant.password = result[7]

            return applicant

    def get_by_email_id(self, email_id):
        applicant = Applicant()
        self.cursor.execute('''SELECT * FROM applicant WHERE email_id = ?''', (email_id,))
        result = self.cursor.fetchone()
        if result is None:
            return None
        else:
            applicant.email_id = result[0]
            applicant.name = result[1]
            applicant.dob = result[2]
            applicant.gender = result[3]
            applicant.age = result[4]
            applicant.tel_no = result[5]
            applicant.experience = result[6]
            applicant.password = result[7]

            return applicant

    def update(self, applicant_details):
        applicant = Applicant()
        applicant_details['where_email_id'] = applicant_details['email_id']
        applicant_tuple = tuple(values for keys, values in applicant_details.items())

        self.connection.execute(
            '''UPDATE applicant SET email_id = ?, name = ?, dob = ?, gender = ?, age = ?, tel_no = ?, experience = ?, password = ? WHERE email_id = ?''',
            applicant_tuple)
        applicant.email_id = applicant_details['email_id']
        applicant.name = applicant_details['name']
        applicant.dob = applicant_details['dob']
        applicant.gender = applicant_details['gender']
        applicant.age = applicant_details['age']
        applicant.tel_no = applicant_details['tel_no']
        applicant.experience = applicant_details['experience']
        applicant.password = applicant_details['password']

        self.connection.commit()

        return applicant

    def delete(self, email_id):
        self.connection.execute('''DELETE FROM applicant WHERE email_id = ?''', email_id)
        self.connection.commit()
