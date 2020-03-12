from Utilities.HashPassword import *
from Repositories.CompanyRepository import CompanyRepository


class ApplicantController:
    def __init__(self):
        self.repository = CompanyRepository()

    def register(self, company_details):
        try:
            company_details['password'] = hash_password(company_details['password'])
            company = self.repository.create(company_details)

            return company
        except Exception as error:
            return str(error)

    def login(self, email, password):
        try:
            company = self.repository.get_by_email_id(email)
            if verify_password(company.password, password):
                return company
            else:
                raise Exception('Incorrect Password')
        except Exception as error:
            return str(error)

    def update(self, company_details):
        try:
            company_details['password'] = hash_password(company_details['password'])
            company = self.repository.update(company_details)

            return company
        except Exception as error:
            return str(error)

    def delete(self, email, password):
        try:
            company = self.repository.get_by_email_id(email)
            if verify_password(company.password, password):
                self.repository.delete(email)
                return None
            else:
                raise Exception('Incorrect Password')
        except Exception as error:
            return str(error)
