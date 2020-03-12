from Utilities.HashPassword import *
from Repositories.ApplicantRepository import ApplicantRepository


class ApplicantController:
    def __init__(self):
        self.repository = ApplicantRepository()

    def register(self, applicant_details):
        try:
            applicant_details['password'] = hash_password(applicant_details['password'])
            applicant = self.repository.create(applicant_details)

            return applicant
        except Exception as error:
            return str(error)

    def login(self, email, password):
        try:
            applicant = self.repository.get_by_email_id(email)
            if verify_password(applicant.password, password):
                return applicant
            else:
                raise Exception('Incorrect Password')
        except Exception as error:
            return str(error)

    def update(self, applicant_details):
        try:
            applicant_details['password'] = hash_password(applicant_details['password'])
            applicant = self.repository.update(applicant_details)

            return applicant
        except Exception as error:
            return str(error)

    def delete(self, email, password):
        try:
            applicant = self.repository.get_by_email_id(email)
            if verify_password(applicant.password, password):
                self.repository.delete(email)
                return None
            else:
                raise Exception('Incorrect Password')
        except Exception as error:
            return str(error)
