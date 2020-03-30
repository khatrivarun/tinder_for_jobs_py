from Models.State import State
from Models.Applicant import Applicant
from Models.Company import Company


def add_login(account):
    State.loggedIn = True
    State.account = account


def get_account():
    return State.account


def middleware_general():
    return State.account is not None


def middleware_company():
    return type(State.account) is Company


def middleware_applicant():
    return type(State.account) is Applicant


def log_out():
    State.account = None
