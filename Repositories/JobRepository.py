import sqlite3
from Models.Job import Job
import os.path


class JobRepository:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "../database.db")
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def create(self, location, requirements, company_email_id):
        job = Job()

        self.connection.execute('''INSERT INTO job(location, requirements, company_email_id) VALUES(?, ?, ?)''',
                                (location, requirements, company_email_id))
        self.connection.commit()

        self.cursor.execute('''SELECT * FROM job WHERE location = ? AND requirements = ? AND company_email_id = ?''',
                            (location, requirements, company_email_id))
        result = self.cursor.fetchone()

        job.job_id = result[0]
        job.location = result[1]
        job.requirements = result[2]
        job.company_email_id = result[3]

        return job

    def get_all(self):
        jobs_list = list()
        self.cursor.execute('''SELECT * FROM job''')
        result = self.cursor.fetchall()

        if result is None:
            return None
        else:
            for row in result:
                job = Job()
                job.job_id = row[0]
                job.location = row[1]
                job.requirements = row[2]
                job.company_email_id = row[3]
                jobs_list.append(job)

            return jobs_list

    def get_jobs_by_company(self, email_id):
        jobs_list = list()
        self.cursor.execute('''SELECT * FROM job WHERE company_email_id = ?''', (email_id,))
        result = self.cursor.fetchall()

        if result is None:
            return None
        else:
            for row in result:
                job = Job()
                job.job_id = row[0]
                job.location = row[1]
                job.requirements = row[2]
                job.company_email_id = row[3]
                jobs_list.append(job)

            return jobs_list

    def get(self, location, requirements, company_email_id):
        job = Job()

        self.cursor.execute('''SELECT * FROM job WHERE location = ? AND requirements = ? AND company_email_id = ?''',
                            (location, requirements, company_email_id))
        result = self.cursor.fetchone()

        if result is None:
            return None
        else:
            job.job_id = result[0]
            job.location = result[1]
            job.requirements = result[2]
            job.company_email_id = result[3]

            return job

    def update(self, old_location, old_requirements, old_company_email_id, new_location, new_requirements,
               new_company_email_id):
        self.connection.execute(
            '''UPDATE company SET location = ?, requirements = ?, company_email_id = ? WHERE location = ? AND requirements = ? AND company_email_id = ?''',
            (
                new_location, new_requirements, new_company_email_id, old_location, old_requirements,
                old_company_email_id))

        self.connection.commit()

        job = self.get(new_location, new_requirements, new_company_email_id)

        return job

    def delete(self, location, requirements, company_email_id):
        self.connection.execute('''DELETE FROM job WHERE location = ? AND requirements = ? AND company_email_id = ?''',
                                (location, requirements, company_email_id))

        self.connection.commit()
