import sqlite3
import os.path


class CreateDatabase:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "../database.db")
        self.conn = sqlite3.connect(db_path)

        self.conn.execute(''' CREATE TABLE IF NOT EXISTS applicant
            (
                email_id TEXT UNIQUE,
                name CHARACTER(20) NOT NULL,
                dob DATE NOT NULL,
                gender TEXT NOT NULL,
                age INTEGER(3) NOT NULL,
                tel_no INTEGER(11) NOT NULL,
                experience TEXT NOT NULL,
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

        self.conn.commit()


if __name__ == '__main__':
    CreateDatabase()
