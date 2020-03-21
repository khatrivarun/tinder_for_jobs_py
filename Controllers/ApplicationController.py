from Repositories.ApplicationRepository import ApplicationRepository


class ApplicationController:
    def __init__(self):
        self.repository = ApplicationRepository()

    def like(self, job_id, applicant_email_id, company_email_id):
        try:
            return self.repository.create(job_id, applicant_email_id, company_email_id)
        except Exception as error:
            return str(error)

    def accept(self, job_id, applicant_email_id, company_email_id):
        try:
            return self.repository.respond(job_id, applicant_email_id, company_email_id, "Accepted")
        except Exception as error:
            return str(error)

    def reject(self, job_id, applicant_email_id, company_email_id):
        try:
            return self.repository.respond(job_id, applicant_email_id, company_email_id, "Rejected")
        except Exception as error:
            return str(error)
