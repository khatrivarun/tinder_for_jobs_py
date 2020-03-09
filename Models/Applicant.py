class Applicant:
    def __init__(self):
        self.email_id = ''
        self.password = ''
        self.name = ''
        self.dob = None
        self.gender = ''
        self.age = ''
        self.tel_no = None
        self.CV = None
        self.experience = None

    def create_applicant(self, applicant_details):
        self.email_id = applicant_details['email_id']
        self.password = applicant_details['password']
        self.name = applicant_details['name']
        self.dob = applicant_details['dob']
        self.gender = applicant_details['gender']
        self.age = applicant_details['age']
        self.tel_no = applicant_details['tel_no']
        self.experience = applicant_details['experience']
