from tkinter import *
from tkinter import messagebox
from re import match
from Controllers.ApplicantController import ApplicantController
from Controllers.CompanyController import CompanyController
from Controllers.StateController import *
from Models.Company import Company
from Models.Applicant import Applicant
from Views.JobView import *


class Login(Frame):
    def __init__(self, logreg):
        self.applicant = ApplicantController()
        self.company = CompanyController()
        self.email_regex = "^[a-zA-Z0-9._]+@[a-z]+\.(com|co\.in|org|in)$"
        logreg.destroy()
        self.loginTk = Tk()
        self.loginTk.title("tinder For Jobs")
        w, h = self.loginTk.winfo_screenwidth(), self.loginTk.winfo_screenheight()
        self.loginTk.geometry("%dx%d+0+0" % (w, h))
        super().__init__()
        self.widthW = w
        self.heightH = h
        self.configure(background='blue')
        self.pack(fill='both', expand=True)
        self.createWidgets()
        self.loginTk.mainloop()

    def applicant_login(self):
        try:
            email = self.emailIdEntryApplicant.get()
            email_match = match(self.email_regex, email)
            password = self.passwordEntryApplicant.get()
            if email == '' or password == '':
                raise Exception('Incomplete Fields')
            elif email_match is None and email != '':
                raise Exception('Invalid Email ID')
            else:
                account = self.applicant.login(email_match.group(0), password)
                if type(account) is str:
                    raise Exception(account)
                elif type(account) is Applicant:
                    # SUCCESS CASE FOR APPLICANT --------------------------------------------------------------------------------------
                    messagebox.showinfo('Message','Login Successfull!')
                    jobview(self.loginTk)
                else:
                    raise Exception('Some weird error is happening')
        except Exception as error:
            messagebox.showinfo("Problem During Login", str(error))

    def company_login(self):
        try:
            email = self.emailIdEntryRecruiter.get()
            email_match = match(self.email_regex, email)
            password = self.passwordEntryRecruiter.get()
            if email == '' or password == '':
                raise Exception('Incomplete Fields')
            elif email_match is None and email != '':
                raise Exception('Invalid Email ID')
            else:
                account = self.company.login(email_match.group(0), password)
                if type(account) is str:
                    raise Exception(account)
                elif type(account) is Company:
                    print(get_account())
                    print(account.email_id)
                    print('Success')
                else:
                    raise Exception('Some weird error is happening')
        except Exception as error:
            messagebox.showinfo("Problem During Login", str(error))

    def createWidgets(self):
        """CREATING FRAMES"""
        textFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH / 4)
        textFrame.grid(row=0, column=0, columnspan=2)

        loginFrame = Frame(self, bg='black', width=self.widthW / 2 + 1, height=self.heightH * 0.75)
        loginFrame.grid(row=1, column=0)

        registerFrame = Frame(self, bg='black', width=self.widthW / 2, height=self.heightH * 0.75)
        registerFrame.grid(row=1, column=1)

        # self.grid_columnconfigure(0, uniform='g1')
        # self.grid_columnconfigure(1, uniform='g1')
        """FRAME ONE FOR LOGO"""
        welcomeLabel1 = Label(textFrame, text="tinder", bg='black', fg='white', font=('Chalet New York', 50))
        welcomeLabel2 = Label(textFrame, text="for Jobs", bg='black', fg='white', font=('Chalet New York', 20))
        welcomeLabel1.place(x=20, y=30)
        welcomeLabel2.place(x=192, y=65)

        """FRAME TWO: LOGIN For Applicant"""

        applicantLabel = Label(loginFrame, text='Applicants Login Here', bg='black', fg='white',
                               font=('Chalet New York', 30))
        applicantLabel.place(x=155, y=20)

        textLabelEmailIdApplicant = Label(loginFrame, text='Email Address: ', bg='black', fg='white',
                                          font=('Chalet New York', 15))
        textLabelEmailIdApplicant.place(x=150, y=120)

        self.emailIdEntryApplicant = Entry(loginFrame, bg='#434343', fg='white', width=40)
        self.emailIdEntryApplicant.place(x=300, y=126)

        textLabelPasswordApplicant = Label(loginFrame, text='Password: ', bg='black', fg='white',
                                           font=('Chalet New York', 15))
        textLabelPasswordApplicant.place(x=189, y=195)

        self.passwordEntryApplicant = Entry(loginFrame, bg='#434343', fg='white', width=40, show='*')
        self.passwordEntryApplicant.place(x=300, y=201)

        applicantloginButton = Button(loginFrame, text='Login', width=20, height=2, bg='#434343', fg='white',
                                      activebackground='#666666', command=self.applicant_login)
        applicantloginButton.place(x=266, y=293)

        """FRAME THREE: Login For Company"""
        recruiterLabel = Label(registerFrame, text='Recruiters Login Here', bg='black', fg='white',
                               font=('Chalet New York', 30))
        recruiterLabel.place(x=145, y=20)

        textLabelEmailIdRecruiter = Label(registerFrame, text='Email Address: ', bg='black', fg='white',
                                          font=('Chalet New York', 15))
        textLabelEmailIdRecruiter.place(x=150, y=120)

        self.emailIdEntryRecruiter = Entry(registerFrame, bg='#434343', fg='white', width=40)
        self.emailIdEntryRecruiter.place(x=300, y=126)

        textLabelPasswordRecruiter = Label(registerFrame, text='Password: ', bg='black', fg='white',
                                           font=('Chalet New York', 15))
        textLabelPasswordRecruiter.place(x=189, y=195)

        self.passwordEntryRecruiter = Entry(registerFrame, bg='#434343', fg='white', width=40, show='*')
        self.passwordEntryRecruiter.place(x=300, y=201)

        loginRecruiter = Button(registerFrame, text='Login', width=20, height=2, bg='#434343', fg='white',
                                activebackground='#666666', command=self.company_login)
        loginRecruiter.place(x=266, y=293)


def createLogin(logreg):
    log = Login(logreg)
