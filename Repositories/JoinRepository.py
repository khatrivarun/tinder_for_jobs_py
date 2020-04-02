import sqlite3
from Models.Application import Application
from Models.Company import Company
from Models.Applicant import Applicant
from Models.Job import Job
from Models.Domain import Domain
import os.path


class JoinRepository:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "../database.db")
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def get_applicant_with_domain(self, email_id):
        applicant = dict()
        applicant['applicant'] = Applicant()
        applicant['domains'] = list()

        self.cursor.execute('''
            SELECT * FROM applicant AS a NATURAL JOIN domain WHERE a.email_id = ?
        ''', (email_id,))
        result = self.cursor.fetchall()
        if result is None:
            return None
        else:
            applicant['applicant'].email_id = result[0][0]
            applicant['applicant'].name = result[0][1]
            applicant['applicant'].dob = result[0][2]
            applicant['applicant'].gender = result[0][3]
            applicant['applicant'].age = result[0][4]
            applicant['applicant'].tel_no = result[0][5]
            applicant['applicant'].experience = result[0][6]
            applicant['applicant'].password = result[0][7]

            for rows in result:
                domain = Domain()
                domain.applicant_email = email_id
                domain.domain_name = rows[len(rows) - 1]
                applicant['domains'].append(domain)

            return applicant

    def get_jobs_with_companies(self, applicant_email_id):
        jobs = list()

        self.cursor.execute('''
            SELECT * FROM company INNER JOIN job WHERE company.email_id = job.company_email_id
            AND job.job_id NOT IN (
                SELECT application.job_id FROM application WHERE applicant_email_id = ?
            )
        ''', (applicant_email_id,))
        result = self.cursor.fetchall()

        if result is None:
            return None
        else:
            for row in result:
                company = Company()
                job = Job()
                company.email_id = row[0]
                company.name = row[1]
                company.location = row[2]
                company.website = row[3]
                company.description = row[4]
                job.job_id = row[6]
                job.location = row[7]
                job.requirements = row[8]
                job.company_email_id = row[9]
                jobs.append({
                    'company': company,
                    'job': job
                })

            return jobs

    def get_applications_with_applicants(self, job_id):
        applications = list()

        self.cursor.execute('''
            SELECT * FROM application a INNER JOIN applicant a2 WHERE a.applicant_email_id = a2.email_id AND a.job_id = ?
        ''', (job_id,))

        result = self.cursor.fetchall()
        if result is None:
            return None
        else:
            for row in result:
                applicant = Applicant()
                application = Application()
                application.application_id = row[0]
                application.job_id = row[1]
                application.company_email_id = row[2]
                application.applicant_email_id = row[3]
                application.response = row[4]
                applicant.email_id = row[5]
                applicant.name = row[6]
                applicant.dob = row[7]
                applicant.gender = row[8]
                applicant.age = row[9]
                applicant.tel_no = row[10]
                applicant.experience = row[11]
                applications.append({
                    'application': application,
                    'applicant': applicant
                })

            return applications

    def get_applied_jobs(self, email_id):
        applications = list()
        self.cursor.execute('''
            SELECT c.name, a.response, j.requirements FROM company c INNER JOIN application a INNER JOIN job j
            WHERE c.email_id = a.company_email_id AND a.job_id = j.job_id AND a.applicant_email_id = ?
        ''', (email_id,))

        result = self.cursor.fetchall()

        if result is None:
            return None

        for row in result:
            applications.append({
                "company_name": row[0],
                "response": row[1],
                "job_requirements": row[2]
            })

        return applications
