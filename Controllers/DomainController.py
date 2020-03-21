from Repositories.DomainRepository import DomainRepository
from Models.Domain import Domain


class DomainController:
    def __init__(self):
        self.repository = DomainRepository()

    def register(self, email_id, domain_name):
        try:
            return self.repository.create(email_id, domain_name)
        except Exception as error:
            return str(error)

    def get_domains_list(self, email_id):
        try:
            return self.repository.get(email_id)
        except Exception as error:
            return str(error)

    def get_all_domains(self):
        try:
            return self.repository.get_all()
        except Exception as error:
            return str(error)

    def delete_domain(self, email_id, domain_name):
        try:
            return self.repository.delete(email_id, domain_name)
        except Exception as error:
            return str(error)
