import sqlite3
from Models.Job import Job


class JobRepository:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
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

        job.job_id = result[0]
        job.location = result[1]
        job.requirements = result[2]
        job.company_email_id = result[3]

        return job
