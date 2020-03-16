from Controllers.ApplicantController import ApplicantController
from Controllers.CompanyController import CompanyController
from Repositories.JoinRepository import JoinRepository
from Repositories.DomainRepository import DomainRepository
from Repositories.JobRepository import JobRepository

if __name__ == '__main__':
    # applicant_details = {
    #     'email_id': 'varun12@varun.com',
    #     'name': 'varun',
    #     'dob': '12-12-2013',
    #     'gender': 'M',
    #     'age': '23',
    #     'tel_no': '123',
    #     'experience': '6',
    #     'password': 'varun123'
    # }
    #
    # applicant = ApplicantController()
    # applicant.register(applicant_details)
    # print(applicant.login('varun12@varun.com', 'varun123'))

    # domain = DomainRepository()
    #
    # domain.create('varun12@varun.com', 'ml')
    # domain.create('varun12@varun.com', 'ai')
    # domain.create('varun12@varun.com', 'iot')

    # jons = JoinRepository()
    # print(jons.get_applicant_with_domain('varun12@varun.com'))

    # company_details = {
    #     'email_id': 'varun12@varun.com',
    #     'password': 'varun123',
    #     'name': 'varun coma ny',
    #     'location': 'njsnd',
    #     'website': 'ndjnd',
    #     'description': 'nsnsjsm'
    # }
    #
    # company = CompanyController()
    # company.register(company_details)
    # print(company.login('varun12@varun.com', 'varun123'))

    # job = JobRepository()
    # print(job.create('njs', 'nm', 'varun12@varun.com'))

    jons = JoinRepository()
    print(jons.get_jobs_with_companies())

