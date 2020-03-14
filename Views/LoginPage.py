from tkinter import *


class Login(Frame):
    def __init__(self, logreg):
        logreg.destroy()
        loginTk = Tk()
        loginTk.title("tinder For Jobs")
        w, h = loginTk.winfo_screenwidth(), loginTk.winfo_screenheight()
        loginTk.geometry("%dx%d+0+0" % (w, h))
        super().__init__()
        self.widthW = w
        self.heightH = h
        self.configure(background='blue')
        self.pack(fill='both', expand=True)
        self.createWidgets()
        loginTk.mainloop()

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
                                      activebackground='#666666')
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
                          activebackground='#666666')
        loginRecruiter.place(x=266, y=293)


def createLogin(logreg):
    log = Login(logreg)


