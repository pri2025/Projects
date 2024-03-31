from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import addcatg
import viewcatg
import addadmin
import viewadmin
import changePassword
import adminRating

class Main:
    def __init__(self,ID,adminname,adminemail,adminrole):
        self.root = Tk()
        self.root.title('Admin Dashboard')
        self.root.state('zoomed')
        self.root.configure(bg="#AD9BAA")

        self.rootMenu = Menu(self.root) # Initializes a Main Menu
        # Configure root window to use rootMenu as its Main Menu
        self.root.configure(menu=self.rootMenu)
        '''
        # File Menu
        self.fileMenu = Menu(self.rootMenu, tearoff=0) # Initializing File Menu
        # Creating an option(button) in rootMenu with name 'file' and linked fileMenu with it.
        self.rootMenu.add_cascade(label='File', menu=self.fileMenu)
        # Adding Buttons in the File Menu
        self.fileMenu.add_command(label="New Project")
        self.fileMenu.add_command(label="New")
        self.fileMenu.add_command(label="New Scratch File")
        '''

        self.mainlabel = Label(self.root, text=f"Welcome {adminname}", font=('arial', 28, 'bold'), bg="#CFCCD6")
        self.mainlabel.pack(pady=20, ipadx=20, ipady=20)

        if adminrole == "super admin":
            self.adminMenu = Menu(self.rootMenu, tearoff=0)
            self.adminMenu.add_command(label='Add Admin', command=lambda: addadmin.main())
            self.adminMenu.add_command(label='View Admin', command=lambda: viewadmin.Main())
            self.rootMenu.add_cascade(label="Admin", menu=self.adminMenu)

        self.catMenu = Menu(self.rootMenu, tearoff=0)
        self.catMenu.add_command(label='Add Category', command=self.openCategory)
        self.catMenu.add_command(label='View Category', command=lambda : viewcatg.view())
        self.rootMenu.add_cascade(label="Category", menu=self.catMenu)

        # self.adminMenu = Menu(self.rootMenu, tearoff=0)
        # self.adminMenu.add_command(label='Add Admin', command=lambda: addadmin.main())
        # self.adminMenu.add_command(label='View Admin', command=lambda: viewadmin.Main())
        # self.rootMenu.add_cascade(label="Admin", menu=self.adminMenu)

        self.profile = Menu(self.rootMenu, tearoff=0)
        self.profile.add_command(label='Change Password', command=lambda: changePassword.password(adminemail))
        self.profile.add_command(label='Log Out', command=lambda: self.root.destroy())
        self.rootMenu.add_cascade(label="Profile", menu=self.profile)

        self.rate = Menu(self.rootMenu, tearoff=0)
        self.rate.add_command(label='Ratings', command=lambda: adminRating.main())
        self.rootMenu.add_cascade(label="Ratings", menu=self.rate)





        self.root.mainloop()

    def openCategory(self):
        obj = addcatg.category()

if __name__ == '__main__':
    obj = Main()