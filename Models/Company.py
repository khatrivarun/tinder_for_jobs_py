class Company:
    def __init__(self):
        self.email_id = ''
        self.password = ''
        self.name = ''
        self.location = ''
        self.website = ''
        self.description = ''

    def create_company(self, company_details):
        self.email_id = company_details['email_id']
        self.password = company_details['password']
        self.name = company_details['name']
        self.location = company_details['location']
        self.website = company_details['website']
        self.description = company_details['description']
