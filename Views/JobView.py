from tkinter import *
from tkinter import messagebox
from Views import LoginPage
from Views.AppliedJobs import *
from Controllers.JoinController import JoinController
from Controllers.ApplicationController import ApplicationController
from Controllers.StateController import *


class JobView(Frame):
    def __init__(self, loginTk):
        loginTk.destroy()
        self.jobviewTk = Tk()
        self.join = JoinController()
        self.application = ApplicationController()
        self.applicant_email_id = get_account().email_id
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

        """GETTING DATA FROM DATABASE"""

        # self.grid_columnconfigure(0, uniform='g1')
        # self.grid_columnconfigure(1, uniform='g1')
        """FRAME ONE FOR LOGO"""
        welcomeLabel1 = Label(textFrame, text="tinder", bg='black', fg='white', font=('Chalet New York', 50))
        welcomeLabel2 = Label(textFrame, text="for Jobs", bg='black', fg='white', font=('Chalet New York', 20))
        welcomeLabel1.place(x=20, y=30)
        welcomeLabel2.place(x=192, y=65)

        """FRAME TWO FOR JOB LISTINGS"""
        self.jobdesc = StringVar()
        self.location = StringVar()
        self.compname = StringVar()
        self.compdesc = StringVar()
        self.website = StringVar()

        try:
            self.counter = 0
            self.jobs_list = self.join.get_jobs(self.applicant_email_id)
            self.jobdesc.set(self.jobs_list[self.counter]['job'].requirements)
            self.location.set(self.jobs_list[self.counter]['job'].location)
            self.compname.set(self.jobs_list[self.counter]['company'].name)
            self.compdesc.set(self.jobs_list[self.counter]['company'].description)
            self.website.set(self.jobs_list[self.counter]['company'].website)
        except Exception as error:
            self.jobdesc.set('')
            self.location.set('')
            self.compname.set('')
            self.compdesc.set('')
            self.website.set('')
            if type(error) is IndexError:
                messagebox.showerror('Error while getting jobs', 'No jobs for you to apply. Come back later.')
            else:
                messagebox.showerror('Error while getting jobs', str(error))

        JobDescriptionLabel = Label(JobFrame, text='Job Description:', bg='black', fg='white',
                                    font=('Chalet New York', 20))
        JobDescriptionLabel.place(x=400, y=0)
        JobDescriptionTextLabel = Label(JobFrame, textvariable=self.jobdesc, bg='black', fg='white',
                                        font=('Chalet New York', 20))
        JobDescriptionTextLabel.place(x=605, y=0)

        TextLocation = Label(JobFrame, text='Job Location: ', bg='black', fg='white',
                             font=('Chalet New York', 20))
        TextLocation.place(x=400, y=50)

        TextLocationValue = Label(JobFrame, textvariable=self.location, bg='black', fg='white',
                                  font=('Chalet New York', 20))
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
                                   font=('Chalet New York', 20))
        TextCompanyWebsite.place(x=400, y=200)

        CompanyWebsitelabel = Label(JobFrame, textvariable=self.website, bg='black', fg='white',
                                    font=('Chalet New York', 20))
        CompanyWebsitelabel.place(x=515, y=200)

        LeftSwipeButton = Button(JobFrame, text='Reject', width=15, height=2, bg='#434343',
                                 fg='white',
                                 activebackground='#666666', font=('Chalet New York',), command=self.reject)
        LeftSwipeButton.place(x=500, y=310)

        RightSwipeButton = Button(JobFrame, text='Apply', width=15, height=2, bg='#434343',
                                  fg='white',
                                  activebackground='#666666', font=('Chalet New York',), command=self.accept)
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

    def accept(self):
        try:
            self.application.like(self.jobs_list[self.counter]['job'].job_id, self.applicant_email_id,
                                  self.jobs_list[self.counter]['company'].email_id)
            messagebox.showinfo('Success', 'Applied to the job successfully!')
            self.counter += 1
            self.jobdesc.set(self.jobs_list[self.counter]['job'].requirements)
            self.location.set(self.jobs_list[self.counter]['job'].location)
            self.compname.set(self.jobs_list[self.counter]['company'].name)
            self.compdesc.set(self.jobs_list[self.counter]['company'].description)
            self.website.set(self.jobs_list[self.counter]['company'].website)
        except Exception as error:
            self.jobdesc.set('')
            self.location.set('')
            self.compname.set('')
            self.compdesc.set('')
            self.website.set('')
            if type(error) is IndexError:
                messagebox.showerror('Error while getting jobs', 'No jobs for you to apply. Come back later.')
            else:
                messagebox.showerror('Error while getting jobs', str(error))

    def reject(self):
        try:
            self.counter += 1
            self.jobdesc.set(self.jobs_list[self.counter]['job'].requirements)
            self.location.set(self.jobs_list[self.counter]['job'].location)
            self.compname.set(self.jobs_list[self.counter]['company'].name)
            self.compdesc.set(self.jobs_list[self.counter]['company'].description)
            self.website.set(self.jobs_list[self.counter]['company'].website)
        except Exception as error:
            self.jobdesc.set('')
            self.location.set('')
            self.compname.set('')
            self.compdesc.set('')
            self.website.set('')
            if type(error) is IndexError:
                messagebox.showerror('Error while getting jobs', 'No jobs for you to apply. Come back later.')
            else:
                messagebox.showerror('Error while getting jobs', str(error))

    def applied(self):
        appliedjobs(self.jobviewTk)

    def logout(self):
        messagebox.showinfo('Message', 'Logout Successfull!')
        LoginPage.createLogin(self.jobviewTk)


def jobview(loginTk):
    log = JobView(loginTk)
