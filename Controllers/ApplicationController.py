from Repositories.ApplicationRepository import ApplicationRepository


class ApplicationController:
    def __init__(self):
        self.repository = ApplicationRepository()

    def like(self, job_id, applicant_email_id, company_email_id):
        return self.repository.create(job_id, applicant_email_id, company_email_id)

    def accept(self, job_id, applicant_email_id, company_email_id):
        return self.repository.respond(job_id, applicant_email_id, company_email_id, "Accepted")

    def reject(self, job_id, applicant_email_id, company_email_id):
        return self.repository.respond(job_id, applicant_email_id, company_email_id, "Rejected")
