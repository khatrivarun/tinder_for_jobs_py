from tkinter import *


class Login(Frame):
    def __init__(self):
        # logreg.destroy()
        loginTk = Tk()
        loginTk.title("tinder For Jobs")
        w, h =loginTk.winfo_screenwidth(), loginTk.winfo_screenheight()
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
        welcomeLabel1 = Label(textFrame, text="tinder", bg='blue', fg='white', font=('Chalet New York', 50))
        welcomeLabel2 = Label(textFrame, text="for Jobs", bg='black', fg='white', font=('Chalet New York', 20))
        welcomeLabel1.place(x=20, y=30)
        welcomeLabel2.place(x=192, y=65)

        """FRAME TWO: LOGIN For Applicant"""
        applicantloginButton = Button(loginFrame, text='Login', width=20, height=2, bg='#434343', fg='white',
                                      activebackground='#666666')
        applicantloginButton.place(x=266, y=293)

        applicantLabel = Label(loginFrame, text='Applicants Fill Here: ', bg='black', fg='white',
                               font=('Chalet New York', 30))
        applicantLabel.place(x=175, y=0)

        TextLabelEmailId = Label(loginFrame, text='Email Address: ', bg='black', fg='white',
                                 font=('Chalet New York', ))
        TextLabelEmailId.place(x=240, y=175)

        TextLabelPrompt = Label(loginFrame, text='Restart Your Search By Logging In.', bg='black',
                                fg='white',
                                font=('Chalet New York', 10))
        TextLabelPrompt.place(x=235, y=350)

        """FRAME THREE FOR REGISTERING"""
        self.TextLabelFreshUser = Label(registerFrame, text='Fresher Here?', bg='black', fg='white',
                                        font=('Chalet New York', 30))
        self.TextLabelFreshUser.place(x=215, y=100)

        self.TextLabelFirstSteps = Label(registerFrame, text='Take Your First Step!', bg='black',
                                         fg='white',
                                         font=('Chalet New York', 20))
        self.TextLabelFirstSteps.place(x=206, y=175)

        self.TextLabelPrompt = Label(registerFrame, text='Register Your Details.', bg='black',
                                     fg='white',
                                     font=('Chalet New York', 10))
        self.TextLabelPrompt.place(x=277, y=350)

        self.register = Button(registerFrame, text='Register', width=20, height=2, bg='#434343', fg='white',
                               activebackground='#666666')
        self.register.place(x=266, y=293)


def createLogin():
    log = Login()


createLogin()
