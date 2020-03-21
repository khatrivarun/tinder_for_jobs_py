from Utilities.HashPassword import *
from Repositories.CompanyRepository import CompanyRepository
from Controllers.StateController import *


class CompanyController:
    def __init__(self):
        self.repository = CompanyRepository()
        self.hash = HashPassword()

    def register(self, company_details):
        try:
            company_details['password'] = self.hash.hash_password(company_details['password'])
            company = self.repository.create(company_details)

            return company
        except Exception as error:
            return str(error)

    def login(self, email, password):
        try:
            company = self.repository.get_by_email_id(email)
            if self.hash.verify_password(company.password, password):
                add_login(company)

                return company
            else:
                raise Exception('Incorrect Password')
        except Exception as error:
            return str(error)

    def update(self, company_details):
        try:
            if middleware():
                company_details['password'] = self.hash.hash_password(company_details['password'])
                company = self.repository.update(company_details)

                return company
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def delete(self, email, password):
        try:
            if middleware():
                company = self.repository.get_by_email_id(email)
                if self.hash.verify_password(company.password, password):
                    self.repository.delete(email)
                    return None
                else:
                    raise Exception('Incorrect Password')
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def logout(self):
        try:
            if middleware():
                log_out()
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)
