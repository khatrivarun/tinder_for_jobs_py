from Repositories.JobRepository import JobRepository
from Controllers.StateController import *


class JobController:
    def __init__(self):
        self.repository = JobRepository()

    def add_job(self, location, requirements, company_email_id):
        try:
            if middleware():
                return self.repository.create(location, requirements, company_email_id)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def available_jobs(self):
        try:
            if middleware():
                return self.repository.get_all()
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def company_jobs(self, email_id):
        try:
            if middleware():
                return self.repository.get_jobs_by_company(email_id)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def update_details(self, old_location, old_requirements, old_company_email_id, new_location, new_requirements,
                       new_company_email_id):
        try:
            if middleware():
                return self.repository.update(old_location, old_requirements, old_company_email_id, new_location,
                                              new_requirements,
                                              new_company_email_id)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def delete_job(self, location, requirements, company_email_id):
        try:
            if middleware():
                return self.repository.delete(location, requirements, company_email_id)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)
