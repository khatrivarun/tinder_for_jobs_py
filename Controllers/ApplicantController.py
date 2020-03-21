from Utilities.HashPassword import *
from Repositories.ApplicantRepository import ApplicantRepository
from Controllers.StateController import *


class ApplicantController:
    def __init__(self):
        self.repository = ApplicantRepository()
        self.hash = HashPassword()

    def register(self, applicant_details):
        try:
            applicant_details['password'] = self.hash.hash_password(applicant_details['password'])
            applicant = self.repository.create(applicant_details)

            return applicant
        except Exception as error:
            return str(error)

    def login(self, email, password):
        try:
            applicant = self.repository.get_by_email_id(email)
            if self.hash.verify_password(applicant.password, password):
                return applicant
            else:
                raise Exception('Incorrect Password')
        except Exception as error:
            return str(error)

    def update(self, applicant_details):
        try:
            if middleware():
                applicant_details['password'] = self.hash.hash_password(applicant_details['password'])
                applicant = self.repository.update(applicant_details)

                return applicant
            else:
                raise Exception('NOT LOGGED IN')
        except Exception as error:
            return str(error)

    def delete(self, email, password):
        try:
            applicant = self.repository.get_by_email_id(email)
            if self.hash.verify_password(applicant.password, password):
                self.repository.delete(email)
                return None
            else:
                raise Exception('Incorrect Password')
        except Exception as error:
            return str(error)
