from tkinter import *


class Register(Frame):
    def __init__(self,logReg):
        logReg.destroy()
        registerTk = Tk()
        registerTk.title("tinder For Jobs")
        w, h = registerTk.winfo_screenwidth(), registerTk.winfo_screenheight()
        registerTk.geometry("%dx%d+0+0" % (w, h))
        super().__init__()
        self.widthW = w
        self.heightH = h
        self.configure(background='blue')
        self.pack(fill='both', expand=True)
        self.createWidgets()
        registerTk.mainloop()

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

        """FRAME TWO: Registration As Applicant"""


        applicantLabel = Label(loginFrame, text='Applicants Fill Here: ', bg='black', fg='white',
                               font=('Chalet New York', 30))
        applicantLabel.place(x=175, y=0)

        TextEmailIDApplicant = Label(loginFrame, text='Email ID: ', bg='black', fg='white',
                            font=('Chalet New York',))
        TextEmailIDApplicant.place(x=195, y=85)

        TextEntryEmailIDApplicant = Entry(loginFrame, bg='#434343', fg='white', width=25,font=('Chalet New York',))
        TextEntryEmailIDApplicant.place(x=280, y=83,height=30)

        TextPasswordAppplicant = Label(loginFrame, text='Password: ', bg='black', fg='white',
                             font=('Chalet New York',))
        TextPasswordAppplicant.place(x=195, y=140)

        TextEntryPasswordApplicant = Entry(loginFrame, show='*', bg='#434343', fg='white', width=25,font=('Chalet New York',))
        TextEntryPasswordApplicant.place(x=280, y=139,height=30)

        TextLabelApplicantName = Label(loginFrame, text='Applicant\nName: ', bg='black', fg='white',
                              font=('Chalet New York',))
        TextLabelApplicantName.place(x=195, y=184)

        TextEntryApplicantName = Entry(loginFrame, bg='#434343', fg='white', width=25,font=('Chalet New York',))
        TextEntryApplicantName.place(x=280, y=193,height=30)

        MonthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                     'November', 'December']
        DayList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31]
        YearList = [1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
                    1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996,
                    1997, 1998, 1999, 2000]

        TextLabelDOB = Label(loginFrame, text='DOB: ', bg='black', fg='white',
                             font=('Chalet New York',))
        TextLabelDOB.place(x=195, y=253)

        variable1 = IntVar()
        variable1.set(DayList[13])  # default value

        variable2 = StringVar()
        variable2.set(MonthList[2])  # default value

        variable3 = IntVar()
        variable3.set(YearList[35])  # default value

        DayOption = OptionMenu(loginFrame, variable1, *DayList)
        DayOption.config(bg='#434343', fg='white',height=1,font=('Chalet New York',))
        DayOption.place(x=260, y=250)

        MonthOption = OptionMenu(loginFrame, variable2, *MonthList)
        MonthOption.config(bg='#434343', fg='white',height=1,font=('Chalet New York',))
        MonthOption.place(x=336, y=250)

        YearOption = OptionMenu(loginFrame, variable3, *YearList)
        YearOption.config(bg='#434343', fg='white',height=1,font=('Chalet New York',))
        YearOption.place(x=463, y=250)

        TextLabelGender = Label(loginFrame, text='Gender: ', bg='black', fg='white',
                             font=('Chalet New York',))
        TextLabelGender.place(x=195, y=311)

        GenderList = ['Male', 'Female', 'Others']

        variable4=StringVar()
        variable4.set(GenderList[0])

        GenderOption = OptionMenu(loginFrame, variable4, *GenderList)
        GenderOption.config(bg='#434343', fg='white',height=1,font=('Chalet New York',))
        GenderOption.place(x=275, y=308)

        TextLabelTelNo = Label(loginFrame, text='Tel No. : ', bg='black', fg='white',
                                font=('Chalet New York',))
        TextLabelTelNo.place(x=195, y=365)

        TextEntryTelNo = Entry(loginFrame, bg='#434343', fg='white', width=25,font=('Chalet New York',))
        TextEntryTelNo.place(x=275, y=363, height=30)

        TextExperience = Label(loginFrame, text='Experience: ', bg='black', fg='white',
                               font=('Chalet New York',))
        TextExperience.place(x=195, y=415)

        ExperienceList = ['None','1 yr', '2 yrs', '3 yrs', '4 yrs', '4+ yrs', '10+ yrs']

        variable5 = StringVar()
        variable5.set(ExperienceList[0])

        ExperienceOption = OptionMenu(loginFrame, variable5, *ExperienceList)
        ExperienceOption.config(bg='#434343', fg='white',height=1,font=('Chalet New York',))
        ExperienceOption.place(x=290, y=412)

        applicantRegisterButton = Button(loginFrame, text='Register As\nApplicant', width=15, height=2, bg='#434343', fg='white',
                                      activebackground='#666666',font=('Chalet New York',))
        applicantRegisterButton.place(x=266, y=476)

        # TextLabelPrompt = Label(loginFrame, text='Restart Your Search By Logging In.', bg='black',
        #                         fg='white',
        #                         font=('Chalet New York', 10))
        # TextLabelPrompt.place(x=235, y=550)

        """FRAME THREE: Registration As Company"""
        TextLabelCompanyRegister = Label(registerFrame, text='Company Fill Here:', bg='black', fg='white',
                                        font=('Chalet New York', 30))
        TextLabelCompanyRegister.place(x=170, y=0)

        TextEmailIDCompany = Label(registerFrame, text='Email ID: ', bg='black', fg='white',
                            font=('Chalet New York',))
        TextEmailIDCompany.place(x=185, y=85)

        TextEntryEmailIDCompany = Entry(registerFrame, bg='#434343', fg='white', width=25, font=('Chalet New York',))
        TextEntryEmailIDCompany.place(x=270, y=83, height=30)

        TextPasswordCompany = Label(registerFrame, text='Password: ', bg='black', fg='white',
                             font=('Chalet New York',))
        TextPasswordCompany.place(x=185, y=140)

        TextEntryPasswordCompany = Entry(registerFrame, show='*', bg='#434343', fg='white', width=25, font=('Chalet New York',))
        TextEntryPasswordCompany.place(x=270, y=139, height=30)

        TextLabelCompanyName = Label(registerFrame, text='Company\nName: ', bg='black', fg='white',
                              font=('Chalet New York',))
        TextLabelCompanyName.place(x=185, y=184)

        TextEntryCompanyName = Entry(registerFrame, bg='#434343', fg='white', width=25, font=('Chalet New York',))
        TextEntryCompanyName.place(x=270, y=193, height=30)

        TextCompanyWebsite = Label(registerFrame, text='Website: ', bg='black', fg='white',
                                   font=('Chalet New York',))
        TextCompanyWebsite.place(x=185, y=253)

        TextEntryCompanyWebsite = Entry(registerFrame, bg='#434343', fg='white', width=25, font=('Chalet New York',))
        TextEntryCompanyWebsite.place(x=270, y=251, height=30)

        TextCompanyLocation = Label(registerFrame, text='Location: ', bg='black', fg='white',
                                   font=('Chalet New York',))
        TextCompanyLocation.place(x=185, y=311)

        TextEntryCompanyLocation = Entry(registerFrame, bg='#434343', fg='white', width=25, font=('Chalet New York',))
        TextEntryCompanyLocation.place(x=270, y=309, height=30)

        TextCompanyDescription = Label(registerFrame, text='Description: ', bg='black', fg='white',
                                    font=('Chalet New York',))
        TextCompanyDescription.place(x=180, y=365)

        TextEntryCompanyDescription = Entry(registerFrame, bg='#434343', fg='white', width=25,font=('Chalet New York',))
        TextEntryCompanyDescription.place(x=270, y=363, height=30)

        # TextLabelFirstSteps = Label(registerFrame, text='Take Your First Step!', bg='black',
        #                                  fg='white',
        #                                  font=('Chalet New York', 20))
        # TextLabelFirstSteps.place(x=206, y=400)

        CompanyRegisterButton = Button(registerFrame, text='Register As\nCompany', width=15, height=2, bg='#434343', fg='white',
                                         activebackground='#666666', font=('Chalet New York',))
        CompanyRegisterButton.place(x=266, y=476)

        # TextLabelPrompt = Label(registerFrame, text='Register Your Details.', bg='black',
        #                              fg='white',
        #                              font=('Chalet New York', 10))
        # TextLabelPrompt.place(x=277, y=500)


def register(logReg):
    log = Register(logReg)



