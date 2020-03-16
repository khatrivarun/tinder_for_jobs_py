import sqlite3
from Models.Domain import Domain


class DomainRepository:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()

    def create(self, email_id, domain_name):
        domain = Domain()
        domain.applicant_email = email_id
        domain.domain_name = domain_name

        self.connection.execute('''INSERT INTO domain (applicant_email, domain_name) VALUES (?, ?)''', (email_id, domain_name))
        self.connection.commit()

        return domain

    def get(self, email_id):
        domains = list()

        self.cursor.execute('''SELECT * FROM domain WHERE applicant_email = ?''', email_id)
        for row in self.cursor:
            domain = Domain()
            domain.applicant_email = row[0]
            domain.domain_name = row[1]
            domains.append(domain)

        return domains

    def get_all(self):
        domain_list = list()

        self.cursor.execute('''SELECT DISTINCT domain_name FROM domain''')
        for row in self.cursor:
            domain_list.append(row[0])

        return domain_list

    def update(self, new_email_id, old_email_id, old_domain_name, new_domain_name):
        domain = Domain()

        self.connection.execute(
            '''UPDATE domain set applicant_email = ?, domain_name = ? WHERE domain_name = ? AND applicant_email = ?''',
            (new_email_id, new_domain_name, old_domain_name, old_email_id))

        self.connection.commit()
        domain.domain_name = new_domain_name
        domain.applicant_email = new_email_id

    def delete(self, email_id, domain):
        self.connection.execute('''DELETE FROM domain WHERE applicant_email = ? AND domain_name = ?''',
                                (email_id, domain))
        self.connection.commit()
