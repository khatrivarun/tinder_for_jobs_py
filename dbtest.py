from Controllers.ApplicantController import ApplicantController
from Controllers.StateController import *
from Controllers.ApplicationController import ApplicationController
from Controllers.CompanyController import CompanyController
from Controllers.JobController import JobController
from Repositories.JoinRepository import JoinRepository
from Repositories.DomainRepository import DomainRepository
from Repositories.JobRepository import JobRepository
from Utilities.HashPassword import HashPassword
from Utilities.CreateDatabase import CreateDatabase
# from Views.LoginRegisterPage import *
import os.path

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
#
# company_details = {
#     'email_id': 'varun@varun.com',
#     'password': 'varun123',
#     'name': 'varun company',
#     'location': 'nj',
#     'website': 'vc.com',
#     'description': 'varun'
# }
#
# company = CompanyController()
# company.register(company_details)
# print(company.login('varun@varun.com', 'varun123'))

# jons = JoinRepository()
# print(jons.get_jobs_with_companies())

# hash = HashPassword()
# print(hash.verify_password(hash.hash_password('varun'), 'varuN'))
#
applicant_details = {
    'email_id': 'daksh@daksh.com',
    'name': 'daksh',
    'dob': '12-12-2013',
    'gender': 'M',
    'age': '23',
    'tel_no': '123',
    'experience': '5',
    'password': 'daksh123'
}
#
applicant = ApplicantController()
# application = ApplicationController()
print(applicant.register(applicant_details))
# print(applicant.login(applicant_details['email_id'], applicant_details['password']))
# print(get_account())
# application.like(1, 'varun1@varun.com', 'varun12@varun.com')
# job = JobController()
# print(job.add_job('njs', 'nm', 'varun12@varun.com'))
# logRegister = LoginRegister()

# join = JoinRepository()
# print(join.get_applications_with_applicants(1))
