import sqlite3


class CreateDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')

        self.conn.execute(''' CREATE TABLE IF NOT EXISTS applicant
            (
                email_id TEXT UNIQUE,
                name CHARACTER(20) NOT NULL,
                dob DATE NOT NULL,
                gender VARCHAR(1) NOT NULL,
                age INTEGER(3) NOT NULL,
                tel_no INTEGER(11) NOT NULL,
                experience INTEGER(3) NOT NULL,
                password TEXT NOT NULL
            );
        ''')

        self.conn.execute(''' CREATE TABLE IF NOT EXISTS job
            (
                job_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                location TEXT NOT NULL,
                requirements TEXT NOT NULL,
                company_email_id REFERENCES company(email_id) NOT NULL 
            );
        ''')

        self.conn.execute(''' CREATE TABLE IF NOT EXISTS application
            (
                application_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                job_id REFERENCES job(job_id),
                company_email_id TEXT REFERENCES  company(email_id) NOT NULL,
                applicant_email_id TEXT REFERENCES  applicant(email_id) NOT NULL,
                response TEXT DEFAULT "Applied"
            );
        ''')

        self.conn.execute(''' CREATE TABLE IF NOT EXISTS company
            (
                email_id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                location TEXT NOT NULL,
                website TEXT NOT NULL,
                description TEXT,
                password TEXT NOT NULL
            );
        ''')

        self.conn.execute(''' CREATE TABLE IF NOT EXISTS domain
            (
                applicant_email REFERENCES applicant(email_id) NOT NULL,
                domain_name VARCHAR(100) NOT NULL 
            );
        ''')


if __name__ == '__main__':
    CreateDatabase()
