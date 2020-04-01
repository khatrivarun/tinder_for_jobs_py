from Repositories.JoinRepository import JoinRepository
from Controllers.StateController import *


class JoinController:
    def __init__(self):
        self.repository = JoinRepository()

    def get_domains(self, email_id):
        try:
            if middleware_applicant():
                return self.repository.get_applicant_with_domain(email_id)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def get_jobs(self, applicant_email_id):
        try:
            if middleware_applicant():
                return self.repository.get_jobs_with_companies(applicant_email_id)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def get_applications(self, job_id):
        try:
            if middleware_company():
                return self.repository.get_applications_with_applicants(job_id)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def get_applied_jobs(self, email_id):
        try:
            if middleware_applicant():
                return self.repository.get_applied_jobs(email_id)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)
