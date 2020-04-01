from tkinter import *
from tkinter import messagebox
from Views.ApplicantSelectionByRecruiter import *
from Controllers.JobController import JobController
from Controllers.StateController import *
from Views import LoginPage


class Recruiter(Frame):
    def __init__(self, recLogin, email):
        recLogin.destroy()
        self.emailId = email
        self.job = JobController()
        # print(self.emailId)
        self.recruiterTK = Tk()
        self.recruiterTK.title("tinder For Jobs")
        w, h = self.recruiterTK.winfo_screenwidth(), self.recruiterTK.winfo_screenheight()
        self.recruiterTK.geometry("%dx%d+0+0" % (w, h))
        super().__init__()
        self.widthW = w
        self.heightH = h
        self.configure(background='blue')
        self.pack(fill='both', expand=True)
        self.createWidgets()
        self.recruiterTK.mainloop()

    def logOutButton(self):
        LoginPage.createLogin(self.recruiterTK)

    def createJobListing(self):
        try:
            requirement = self.requirementsEntry.get('1.0', END)
            location = self.locationEntry.get('1.0', END)

            # print('requirement: ', requirement)
            # print('location: ', location)
            if requirement == '' or location == '':
                raise Exception('Incomplete Field')

            else:
                print(self.job.add_job(location=location, requirements=requirement, company_email_id=self.emailId))
        except Exception as error:
            messagebox.showinfo("Problem while Creating Job", str(error))

        finally:
            self.requirementsEntry.delete('1.0', 'end')
            self.locationEntry.delete('1.0', 'end')

    def createWidgets(self):
        """CREATING FRAMES"""
        textFrame = Frame(self, bg='black', width=self.widthW, height=self.heightH / 4)
        textFrame.grid(row=0, column=0, columnspan=2)

        createJobFrame = Frame(self, bg='black', width=self.widthW / 2 + 1, height=self.heightH * 0.75)
        createJobFrame.grid(row=1, column=0)

        viewJobsFrame = Frame(self, bg='black', width=self.widthW / 2, height=self.heightH * 0.75)
        viewJobsFrame.grid(row=1, column=1)

        # self.grid_columnconfigure(0, uniform='g1')
        # self.grid_columnconfigure(1, uniform='g1')
        """FRAME ONE FOR LOGO"""
        welcomeLabel1 = Label(textFrame, text="tinder", bg='black', fg='white', font=('Chalet New York', 50))
        welcomeLabel2 = Label(textFrame, text="for Jobs", bg='black', fg='white', font=('Chalet New York', 20))
        welcomeLabel1.place(x=20, y=30)
        welcomeLabel2.place(x=192, y=65)

        """FRAME TWO: Create Jobs"""

        createJobLabel = Label(createJobFrame, text='Create A Job Listing', bg='black', fg='white',
                               font=('Chalet New York', 30))
        createJobLabel.place(x=155, y=20)

        requirementsLabel = Label(createJobFrame, text='Requirements: ', bg='black', fg='white',
                                  font=('Chalet New York', 15))
        requirementsLabel.place(x=150, y=120)

        self.requirementsEntry = Text(createJobFrame, bg='#434343', fg='white', width=30, height=7)
        self.requirementsEntry.place(x=300, y=126)

        locationLabel = Label(createJobFrame, text='Location: ', bg='black', fg='white',
                              font=('Chalet New York', 15))
        locationLabel.place(x=189, y=244)

        self.locationEntry = Text(createJobFrame, bg='#434343', fg='white', width=30, height=1)
        self.locationEntry.place(x=300, y=250)

        createJobButton = Button(createJobFrame, text='Create Job', width=20, height=2, bg='#434343', fg='white',
                                 activebackground='#666666', command=self.createJobListing)
        createJobButton.place(x=266, y=293)

        logOutButton = Button(createJobFrame, text='Logout', width=6, height=1, bg='#434343', fg='white',
                              activebackground='#666666', command=self.logOutButton)

        logOutButton.place(x=0, y=0)

        """FRAME THREE: Viewing Jobs"""
        viewJobsLabel = Label(viewJobsFrame, text='Created Jobs: ', bg='black', fg='white',
                              font=('Chalet New York', 30))
        viewJobsLabel.place(x=145, y=20)

        viewCanvas = Canvas(viewJobsFrame, bg='black', width=670, height=400, bd=0, relief='ridge')
        viewCanvas.place(x=0, y=85)

        scrollBar = Scrollbar(viewCanvas, orient="vertical", command=viewCanvas.yview, bg='green')
        scrollBar.place(x=655, y=2, height=400)

        innerFrame = Frame(viewCanvas, bg='black', width=650, height=250)
        innerFrame.place(x=5, y=10)

        # Returns a list of Job objects.
        job_list = self.job.company_jobs(self.emailId)
        # for job_ in job_list:
        #     # print(job_)
        #     print(job_.location)
        #     print(job_.requirements)

        counter = 0
        frameList = []

        for job in job_list:
            frameList.append(Frame(innerFrame, bg='black', bd=1, relief='sunken'))
            frameList[-1].pack()

            jobLocationVar = f'Job Location: {job.location}'
            jobRequirementVar = f'Job Requirements: \n{job.requirements}'

            Label(frameList[-1], text=jobRequirementVar, bg='black', fg='white', width=70,
                  font=('Chalet New York', 10), anchor=W).grid(row=0, column=0)

            Label(frameList[-1], text=jobLocationVar, bg='black', fg='white', width=70,
                  font=('Chalet New York', 10), anchor=W).grid(row=1)

            Button(frameList[-1], text='Go', bg='#434343', fg='white',
                   activebackground='#666666', width=10,
                   command=lambda ID=job.job_id: self.jobsList(ID)).grid(row=0, column=1)
            counter += 1

        viewCanvas.create_window(0, 0, anchor='nw', window=innerFrame)
        viewCanvas.update_idletasks()
        viewCanvas.configure(scrollregion=viewCanvas.bbox('all'), yscrollcommand=scrollBar.set)

    def jobsList(self, jobID):
        createSelectApplicant(self.recruiterTK, jobID, self.emailId)


def createRecruiter(recLogin, email):
    log = Recruiter(recLogin, email)

# log = Recruiter()
