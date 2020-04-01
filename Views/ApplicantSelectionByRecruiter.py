from tkinter import *
from Controllers.JoinController import JoinController
from Controllers.ApplicationController import ApplicationController
from Views import RecruiterPage
from Views import LoginPage
from tkinter import messagebox


class SelectApplicant(Frame):
    def __init__(self, recTk, jobID, companyEmail):
        recTk.destroy()
        self.jobId = jobID
        self.companyEmailID = companyEmail
        self.join = JoinController()
        # I have added Application controller object here --------------------------------------------
        self.application = ApplicationController()
        self.selectApplicantTk = Tk()
        self.selectApplicantTk.title("tinder For Jobs")
        w, h = self.selectApplicantTk.winfo_screenwidth(), self.selectApplicantTk.winfo_screenheight()
        self.selectApplicantTk.geometry("%dx%d+0+0" % (w, h))
        super().__init__()
        self.widthW = w
        self.heightH = h
        self.configure(background='blue')
        self.pack(fill='both', expand=True)
        self.createWidgets()
        self.selectApplicantTk.mainloop()

    def accept(self, applicantEmailId):
        self.application.accept(self.jobId, applicantEmailId, self.companyEmailID)
        self.statusVar.set('Status: Accepted')
        messagebox.showinfo('Response', 'Applicant Accepted')

    def reject(self, applicantEmailId):
        self.application.reject(self.jobId, applicantEmailId, self.companyEmailID)
        self.statusVar.set('Status: Rejected')
        messagebox.showinfo('Response', 'Applicant Rejected')

    def backButton(self):
        RecruiterPage.createRecruiter(self.selectApplicantTk, self.companyEmailID)

    def logOutButton(self):
        LoginPage.createLogin(self.selectApplicantTk)

    def createWidgets(self):
        """CREATING FRAMES"""
        textFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH / 4)
        textFrame.grid(row=0, column=0, columnspan=2)

        viewJobsFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH * 0.75)
        viewJobsFrame.grid(row=1, column=1)

        # self.grid_columnconfigure(0, uniform='g1')
        # self.grid_columnconfigure(1, uniform='g1')
        """FRAME ONE FOR LOGO"""
        welcomeLabel1 = Label(textFrame, text="tinder", bg='black', fg='white', font=('Chalet New York', 50))
        welcomeLabel2 = Label(textFrame, text="for Jobs", bg='black', fg='white', font=('Chalet New York', 20))
        welcomeLabel1.place(x=20, y=30)
        welcomeLabel2.place(x=192, y=65)

        """FRAME THREE: Viewing Jobs"""
        viewJobsLabel = Label(viewJobsFrame, text='Applicants for This Job: ', bg='black', fg='white',
                              font=('Chalet New York', 30))
        viewJobsLabel.place(x=457, y=0)

        backButton = Button(viewJobsFrame, text='Back', bg='#434343', fg='white',
                            activebackground='#666666', width=6, height=1, command=self.backButton)
        backButton.place(x=0, y=0)

        logOutButton = Button(viewJobsFrame, text='Logout', width=6, height=1, bg='#434343', fg='white',
                              activebackground='#666666', command=self.logOutButton)
        logOutButton.place(x=53, y=0)

        viewCanvas = Canvas(viewJobsFrame, bg='black', width=self.widthW, height=400, bd=0, relief='ridge')
        viewCanvas.place(x=0, y=85)

        scrollBar = Scrollbar(viewCanvas, orient="vertical", command=viewCanvas.yview, bg='green')
        scrollBar.place(x=1345, y=2, height=400)

        innerFrame = Frame(viewCanvas, bg='black', width=650, height=250)
        innerFrame.place(x=5, y=10)

        frameList = []

        applications = self.join.get_applications(self.jobId)

        # For accepting and rejecting applicants:--------------------------------------------
        # application.accept(job_id, applicant_email_id, company_email_id)
        # application.reject(job_id, applicant_email_id, company_email_id)
        self.statusVar = StringVar()

        for i in applications:
            frameList.append(Frame(innerFrame, bg='black', width=self.widthW, bd=1, relief='sunken'))
            frameList[-1].pack()

            nameVar = f"Name: {i['applicant'].name}"
            emailVar = f"EmailId: {i['applicant'].email_id}"
            self.statusVar.set(f"Status: {i['application'].response}")
            experienceVar = f"Experience: {i['applicant'].experience}"

            Label(frameList[-1], text=nameVar, bg='black', fg='white', width=121, height=3,
                  font=('Chalet New York', 15)).grid(row=0, columnspan=2)

            Label(frameList[-1], text=emailVar, bg='black', fg='white', width=121, height=3,
                  font=('Chalet New York', 15)).grid(row=1, columnspan=2)

            Label(frameList[-1], text=experienceVar, bg='black', fg='white', width=121, height=3,
                  font=('Chalet New York', 15)).grid(row=2, columnspan=2)

            Label(frameList[-1], textvariable=self.statusVar, bg='black', fg='white', width=121, height=3,
                  font=('Chalet New York', 15)).grid(row=3, columnspan=2)

            Button(frameList[-1], text='Reject', bg='#434343', fg='white',
                   activebackground='#666666', width=20, height=2,
                   command=lambda appEmail=i['applicant'].email_id: self.reject(appEmail)).grid(row=4, column=0)

            Button(frameList[-1], text='Accept', bg='#434343', fg='white',
                   activebackground='#666666', width=20, height=2,
                   command=lambda appEmail=i['applicant'].email_id: self.accept(appEmail)).grid(row=4, column=1)
            viewCanvas.create_window(0, 0, anchor='nw', window=innerFrame)
            viewCanvas.update_idletasks()
            viewCanvas.configure(scrollregion=viewCanvas.bbox('all'), yscrollcommand=scrollBar.set)


def createSelectApplicant(recTK, jobID, companyEmail):
    log = SelectApplicant(recTK, jobID, companyEmail)

# log = SelectApplicant()
