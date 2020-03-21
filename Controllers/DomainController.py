from Repositories.DomainRepository import DomainRepository
from Controllers.StateController import *


class DomainController:
    def __init__(self):
        self.repository = DomainRepository()

    def register(self, email_id, domain_name):
        try:
            if middleware_applicant():
                return self.repository.create(email_id, domain_name)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def get_domains_list(self, email_id):
        try:
            if middleware_applicant():
                return self.repository.get(email_id)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def get_all_domains(self):
        try:
            if middleware_applicant():
                return self.repository.get_all()
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)

    def delete_domain(self, email_id, domain_name):
        try:
            if middleware_applicant():
                return self.repository.delete(email_id, domain_name)
            else:
                raise Exception('Not Logged In')
        except Exception as error:
            return str(error)
