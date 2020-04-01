from tkinter import *
from tkinter import messagebox

from Views import LoginPage
from Views.AppliedJobs import *


class JobView(Frame):
    def __init__(self,loginTk):
        loginTk.destroy()
        self.jobviewTk = Tk()
        self.jobviewTk.title("tinder For Jobs")
        w, h = self.jobviewTk.winfo_screenwidth(), self.jobviewTk.winfo_screenheight()
        self.jobviewTk.geometry("%dx%d+0+0" % (w, h))
        super().__init__()
        self.widthW = w
        self.heightH = h
        self.configure(background='blue')
        self.pack(fill='both', expand=True)
        self.createWidgets()
        self.jobviewTk.mainloop()

    def createWidgets(self):
        """CREATING FRAMES"""
        textFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH / 4)
        textFrame.grid(row=0, column=0, columnspan=2)

        JobFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH * 0.75)
        JobFrame.grid()


        # self.grid_columnconfigure(0, uniform='g1')
        # self.grid_columnconfigure(1, uniform='g1')
        """FRAME ONE FOR LOGO"""
        welcomeLabel1 = Label(textFrame, text="tinder", bg='black', fg='white', font=('Chalet New York', 50))
        welcomeLabel2 = Label(textFrame, text="for Jobs", bg='black', fg='white', font=('Chalet New York', 20))
        welcomeLabel1.place(x=20, y=30)
        welcomeLabel2.place(x=192, y=65)

        """FRAME TWO FOR JOB LISTINGS"""
        self.jobdesc=StringVar()
        self.jobdesc.set('Required Skills..................')
        self.location = StringVar()
        self.location.set('Location')
        self.compname = StringVar()
        self.compname.set('Companys Name')
        self.compdesc = StringVar()
        self.compdesc.set('Companys Description')
        self.website = StringVar()
        self.website.set('Website Link')

        JobDescriptionLabel = Label(JobFrame, text='Job Description:', bg='black', fg='white',
                               font=('Chalet New York',20))
        JobDescriptionLabel.place(x=400, y=0)
        JobDescriptionTextLabel = Label(JobFrame, textvariable=self.jobdesc, bg='black', fg='white',
                         font=('Chalet New York', 20))
        JobDescriptionTextLabel.place(x=605, y=0)

        TextLocation = Label(JobFrame, text='Job Location: ', bg='black', fg='white',
                             font=('Chalet New York', 20))
        TextLocation.place(x=400, y=50)

        TextLocationValue = Label(JobFrame, textvariable=self.location, bg='black', fg='white', font=('Chalet New York', 20))
        TextLocationValue.place(x=570, y=50)

        CompanyNameLabel = Label(JobFrame, text='Company Name:', bg='black', fg='white',
                                    font=('Chalet New York', 20))
        CompanyNameLabel.place(x=400, y=100)
        CompanyNameTextLabel = Label(JobFrame, textvariable=self.compname, bg='black', fg='white',
                                 font=('Chalet New York', 20))
        CompanyNameTextLabel.place(x=610, y=100)

        TextCompanyDescription = Label(JobFrame, text='Company Description: ', bg='black', fg='white',
                                       font=('Chalet New York', 20))
        TextCompanyDescription.place(x=400, y=150)

        TextCompanyDescriptionValue = Label(JobFrame, textvariable=self.compdesc, bg='black', fg='white',
                                            font=('Chalet New York', 20))
        TextCompanyDescriptionValue.place(x=675, y=150)

        TextCompanyWebsite = Label(JobFrame, text='Website: ', bg='black', fg='white',
                                   font=('Chalet New York',20))
        TextCompanyWebsite.place(x=400, y=200)

        CompanyWebsitelabel = Label(JobFrame,textvariable= self.website,bg='black', fg='white',font=('Chalet New York',20))
        CompanyWebsitelabel.place(x=515,y=200)

        LeftSwipeButton = Button(JobFrame, text='Reject', width=15, height=2, bg='#434343',
                                       fg='white',
                                       activebackground='#666666', font=('Chalet New York',),command=self.myfuncreject)
        LeftSwipeButton.place(x=500, y=310)

        RightSwipeButton = Button(JobFrame, text='Apply', width=15, height=2, bg='#434343',
                                 fg='white',
                                 activebackground='#666666', font=('Chalet New York',),command=self.myfuncaccept)
        RightSwipeButton.place(x=790, y=310)

        AppliedJobButton = Button(JobFrame, text='Applied Jobs', width=15, height=2, bg='#434343',
                                  fg='white',
                                  activebackground='#666666', font=('Chalet New York',), command=self.applied)
        AppliedJobButton.place(x=500, y=420)

        LogoutButton = Button(JobFrame, text='Logout', width=15, height=2, bg='#434343',
                                  fg='white',
                                  activebackground='#666666', font=('Chalet New York',),
                                  command=self.logout)
        LogoutButton.place(x=790, y=420)

    def myfuncaccept(self):
        messagebox.showinfo("Info", "Applied Succesfully")
        self.jobdesc.set('Web Developer')
        self.location.set('Australia')
        self.compname.set('Google')
        self.compdesc.set('MNC, established since 2001')
        self.website.set('website_link_for_google')

    def myfuncreject(self):
        self.jobdesc.set('Ethical Hacker')
        self.location.set('USA')
        self.compname.set('Amazon')
        self.compdesc.set('Online Shopping Platform')
        self.website.set('website_link_for_amazon')

    def applied(self):
        appliedjobs(self.jobviewTk)

    def logout(self):
        messagebox.showinfo('Message','Logout Successfull!')
        LoginPage.createLogin(self.jobviewTk)



def jobview(loginTk):
    log = JobView(loginTk)

