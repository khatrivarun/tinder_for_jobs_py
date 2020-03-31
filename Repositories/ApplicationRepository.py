from Models.Application import Application
import sqlite3
import os.path


class ApplicationRepository:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "../database.db")
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def create(self, job_id, applicant_email_id, company_email_id):
        application = Application()
        application.job_id = job_id
        application.applicant_email_id = applicant_email_id
        application.company_email_id = company_email_id
        application.response = 'Applied'

        self.connection.execute(
            '''INSERT INTO application(job_id, company_email_id, applicant_email_id, company_email_id) VALUES (?, ?, ?, ?)''',
            (job_id, company_email_id, applicant_email_id, company_email_id))

        self.connection.commit()

        application.application_id = self.get(job_id, applicant_email_id, company_email_id).application_id

        return application

    def get(self, job_id, applicant_email_id, company_email_id):
        application = Application()

        self.cursor.execute(
            '''SELECT * FROM application WHERE job_id = ? AND applicant_email_id = ? AND company_email_id = ?''',
            (job_id, applicant_email_id, company_email_id))
        result = self.cursor.fetchone()

        if result is None:
            return None
        else:
            application.application_id = result[0]
            application.job_id = result[1]
            application.company_email_id = result[2]
            application.applicant_email_id = result[3]
            application.response = result[4]

            return application

    def get_all(self, job_id):
        application_list = list()

        self.cursor.execute('''SELECT * FROM application WHERE job_id = ?''', job_id)
        result = self.cursor.fetchall()

        if result is None:
            return None
        else:
            for row in result:
                application = Application()
                application.application_id = row[0]
                application.job_id = row[1]
                application.company_email_id = row[2]
                application.applicant_email_id = row[3]
                application.response = row[4]
                application_list.append(application)

            return application_list

    def respond(self, job_id, applicant_email_id, company_email_id, response):
        application = self.get(job_id, applicant_email_id, company_email_id)
        application.response = 'Rejected'

        self.connection.execute('''UPDATE application SET response = ? WHERE application_id = ?''',
                                (response, application.application_id))
        self.connection.commit()

        return application

    def delete(self, job_id, applicant_email_id, company_email_id):
        application = self.get(job_id, applicant_email_id, company_email_id)

        self.connection.execute('''DELETE FROM application WHERE application_id = ?''', application.application_id)
        self.connection.commit()
