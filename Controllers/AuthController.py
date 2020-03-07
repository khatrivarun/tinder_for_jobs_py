from .MainController import MainController


class AuthController(MainController):
    def __init__(self):
        super().__init__()

    def login(self, email, password):
        pass

    def register_applicant(self, applicant_details):
        pass

    def register_company(self, company_details):
        pass
