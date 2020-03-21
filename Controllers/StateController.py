from Models.State import State


def add_login(account):
    State.loggedIn = True
    State.account = account


def get_account():
    return State.account


def middleware():
    return State.account is not None


def log_out():
    State.account = None
