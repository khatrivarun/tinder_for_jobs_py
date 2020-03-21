from Repositories.JobRepository import JobRepository
from Models.Job import Job


class JobController:
    def __init__(self):
        self.repository = JobRepository()

    def add_job(self, location, requirements, company_email_id):
        try:
            return self.repository.create(location, requirements, company_email_id)
        except Exception as error:
            return str(error)

    def available_jobs(self):
        try:
            return self.repository.get_all()
        except Exception as error:
            return str(error)

    def company_jobs(self, email_id):
        try:
            return self.repository.get_jobs_by_company(email_id)
        except Exception as error:
            return str(error)

    def update_details(self, old_location, old_requirements, old_company_email_id, new_location, new_requirements,
                       new_company_email_id):
        try:
            return self.repository.update(old_location, old_requirements, old_company_email_id, new_location,
                                          new_requirements,
                                          new_company_email_id)
        except Exception as error:
            return str(error)

    def delete_job(self, location, requirements, company_email_id):
        try:
            return self.repository.delete(location, requirements, company_email_id)
        except Exception as error:
            return str(error)
