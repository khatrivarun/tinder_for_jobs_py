from Controllers.MainController import MainController
from Models.Applicant import Applicant
from Models.Company import Company


class AuthController(MainController):
    def __init__(self):
        super().__init__()

    def login_applicant(self, email, password):
        pass

    def login_company(self, email, password):
        pass

    def register_applicant(self, applicant_details):
        """
        This function, when called, creates a record in the database of the applicant with the
        provided details and returns corresponding Applicant object.

        Args:
            applicant_details: A Dictionary corresponding to all values of the applicant.

        Returns:
            Returns an applicant object when there is  successful applicant creation else none.
        """
        try:
            applicant_details['password'] = hash(applicant_details['password'])
            applicant = Applicant()
            applicant.create_applicant(applicant_details)

            applicant_tuple = tuple(values for keys, values in applicant_details.items())

            self.conn.execute('''
                INSERT INTO applicant( email_id, name, dob, gender, age, tel_no, experience, password )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            ''', applicant_tuple)

            self.conn.commit()

            return applicant
        except Exception as exception:
            print(exception)
            return None

    def register_company(self, company_details):
        """
            This function, when called, creates a record in the database of the applicant with the
            provided details and returns corresponding Company object.

            Args:
                company_details: A Dictionary corresponding to all values of the company.

            Returns:
                Returns a company object when there is  successful company creation else none.
            """
        try:
            company_details['password'] = hash(company_details['password'])
            company = Company()
            company.create_company(company_details)

            company_tuple = tuple(values for keys, values in company_details.items())

            self.conn.execute('''
                    INSERT INTO company( email_id, name, location, website, description, password )
                    VALUES (?, ?, ?, ?, ?, ?);
            ''', company_tuple)

            self.conn.commit()

            return company
        except Exception as exception:
            print(exception)
            return None
