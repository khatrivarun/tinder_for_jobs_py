from Repositories.ApplicationRepository import ApplicationRepository
from Controllers.StateController import *


class ApplicationController:
    def __init__(self):
        self.repository = ApplicationRepository()

    def like(self, job_id, applicant_email_id, company_email_id):
        try:
            if middleware():
                return self.repository.create(job_id, applicant_email_id, company_email_id)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def accept(self, job_id, applicant_email_id, company_email_id):
        try:
            if middleware():
                return self.repository.respond(job_id, applicant_email_id, company_email_id, "Accepted")
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def reject(self, job_id, applicant_email_id, company_email_id):
        try:
            if middleware():
                return self.repository.respond(job_id, applicant_email_id, company_email_id, "Rejected")
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)
