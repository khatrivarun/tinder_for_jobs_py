from tkinter import *
from Controllers.JoinController import JoinController
from Controllers.ApplicationController import ApplicationController


class SelectApplicant(Frame):
    def __init__(self, recTk, jobID):
        recTk.destroy()
        self.jobId = jobID
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

        for i in applications:
            frameList.append(Frame(innerFrame, bg='black', width=self.widthW, bd=1, relief='sunken'))
            frameList[-1].pack()

            nameVar = f"Name: {i['applicant'].name}"
            emailVar = f"EmailId: {i['applicant'].email_id}"
            experienceVar = f"Experience: {i['applicant'].experience}"

            Label(frameList[-1], text=nameVar, bg='black', fg='white', width=121, height=5,
                  font=('Chalet New York', 15)).grid(row=0, columnspan=2)

            Label(frameList[-1], text=emailVar, bg='black', fg='white', width=121, height=5,
                  font=('Chalet New York', 15)).grid(row=1, columnspan=2)

            Label(frameList[-1], text=experienceVar, bg='black', fg='white', width=121, height=5,
                  font=('Chalet New York', 15)).grid(row=2, columnspan=2)

            Button(frameList[-1], text='Reject', bg='#434343', fg='white',
                   activebackground='#666666', width=20, height=2).grid(row=3, column=0)

            Button(frameList[-1], text='Accept', bg='#434343', fg='white',
                   activebackground='#666666', width=20, height=2).grid(row=3, column=1)
            viewCanvas.create_window(0, 0, anchor='nw', window=innerFrame)
            viewCanvas.update_idletasks()
            viewCanvas.configure(scrollregion=viewCanvas.bbox('all'), yscrollcommand=scrollBar.set)


def createSelectApplicant(recTK, jobID):
    log = SelectApplicant(recTK, jobID)

# log = SelectApplicant()
