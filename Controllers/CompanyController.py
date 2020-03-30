from Utilities.HashPassword import *
from Repositories.CompanyRepository import CompanyRepository
from Controllers.StateController import *


class CompanyController:
    def __init__(self):
        self.repository = CompanyRepository()
        self.hash = HashPassword()

    def register(self, company_details):
        try:
            check = self.repository.get_by_email_id(company_details['email_id'])
            if check is None:
                company_details['password'] = self.hash.hash_password(company_details['password'])
                company = self.repository.create(company_details)

                return company
            else:
                raise Exception('Email already exists.')
        except Exception as error:
            return str(error)

    def login(self, email, password):
        try:
            company = self.repository.get_by_email_id(email)
            if company is not None:
                if self.hash.verify_password(company.password, password):
                    add_login(company)

                    return company
                else:
                    raise Exception('Incorrect Password')
            else:
                raise Exception('Email Does Not Exist')
        except Exception as error:
            return str(error)

    def update(self, company_details):
        try:
            if middleware_company():
                company_details['password'] = self.hash.hash_password(company_details['password'])
                company = self.repository.update(company_details)

                return company
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def delete(self, email, password):
        try:
            if middleware_company():
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
            if middleware_company():
                log_out()
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)
