import sqlite3
from Models.Company import Company


class CompanyRepository:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

    def create(self, company_details):
        company = Company()
        company.email_id = company_details['email_id']
        company.password = company_details['password']
        company.name = company_details['name']
        company.location = company_details['location']
        company.website = company_details['website']
        company.description = company_details['description']

        company_tuple = tuple(values for keys, values in company_details.items())

        self.connection.execute(
            '''INSERT INTO company( email_id, password, name, location, website, description )VALUES (?, ?, ?, ?, ?, ?);''',
            company_tuple)

        self.connection.commit()

        return company

    def get(self, email_id, password):
        company = Company()
        self.cursor.execute('''SELECT * FROM company WHERE email_id = ? AND password = ?''', (email_id, password))
        result = self.cursor.fetchone()
        company.email_id = result[0]
        company.name = result[1]
        company.location = result[2]
        company.website = result[3]
        company.description = result[4]
        company.password = result[5]

        return company

    def get_by_email_id(self, email_id):
        company = Company()
        self.cursor.execute('''SELECT * FROM company WHERE email_id = ?''', (email_id,))
        result = self.cursor.fetchone()
        company.email_id = result[0]
        company.name = result[1]
        company.location = result[2]
        company.website = result[3]
        company.description = result[4]
        company.password = result[5]

        return company

    def update(self, company_details):
        company = Company()
        company_details['where_email_id'] = company_details['email_id']
        company_tuple = tuple(values for keys, values in company_details.items())

        self.connection.execute(
            '''UPDATE company SET email_id = ?, password = ?, name = ?, location = ?, website = ?, description = ? WHERE email_id = ?''',
            company_tuple)
        company.email_id = company_details['email_id']
        company.password = company_details['password']
        company.name = company_details['name']
        company.location = company_details['location']
        company.website = company_details['website']
        company.description = company_details['description']

        self.connection.commit()

        return company

    def delete(self, email_id):
        self.connection.execute('''DELETE FROM company WHERE email_id = ?''', email_id)
        self.connection.commit()
