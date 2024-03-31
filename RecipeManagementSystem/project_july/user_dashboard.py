from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import adduser
import recipe_page
import user_rating
import viewUSer
import userPAssword
import recipe
import viewrecipe


class Main:
    def __init__(self, userID, userName, userEmail):
        self.root = Tk()
        self.root.title('User Dashboard')
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


        self.UserMenu = Menu(self.rootMenu, tearoff=0)
        self.UserMenu.add_command(label='Add User', command=lambda: adduser.user())
        self.UserMenu.add_command(label='View User', command=lambda: viewUSer.ViewUser())
        self.rootMenu.add_cascade(label="User", menu=self.UserMenu)

        self.profile = Menu(self.rootMenu, tearoff=0)
        self.profile.add_command(label='Change Password', command=lambda: userPAssword.password(userEmail))
        self.profile.add_command(label='Log Out', command=lambda: self.root.destroy())
        self.rootMenu.add_cascade(label="Profile", menu=self.profile)

        self.recipeMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label="Recipe", menu=self.recipeMenu)
        self.recipeMenu.add_command(label='Add Recipe', command=lambda: recipe.Main(userID=userID))
        self.recipeMenu.add_command(label='View Recipe', command=lambda: viewrecipe.view(userID=userID))
        self.recipeMenu.add_command(label='Recipe List', command=lambda: recipe_page.Main(userid=userID))

        # self.ratingMenu = Menu(self.rootMenu, tearoff=0)
        # self.rootMenu.add_cascade(label="Recipe", menu=self.recipeMenu)
        # self.recipeMenu.add_command(label='Add Recipe', command=lambda: recipe.Main(userID=userID))

        self.ratings = Menu(self.rootMenu, tearoff =0)
        self.rootMenu.add_cascade(label="Ratings", menu=self.ratings)
        self.ratings.add_command(label='User Ratings', command=lambda: user_rating.main(userID=userID))

        self.mainLabel = Label(self.root, text=f"Welcome {userName}", font=('', 28, 'bold'), bg="#CFCCD6")
        self.mainLabel.pack(pady=20)


        self.root.mainloop()

if __name__ == '__main__':
    obj = Main()