#imports
import pygame
import tkinter
import customtkinter



class inputscreen:
    def __init__(self): #initializes the customtkinter screen
        self.screen = customtkinter.CTk() 

        self.screen.eval('tk::PlaceWindow . center') #centers the window
        customtkinter.set_appearance_mode("dark") #sets the window to dark mode
        self.screen.title("Braking Distance Simulator") #sets the title of the window

        #sets the window to full screen
        width = self.screen.winfo_screenwidth()
        height = self.screen.winfo_screenheight()
        geometry = str(width) + "x" + str(height)
        self.screen.geometry(geometry)

    def getdisplay(self):
        return self.screen
    def valiadate(self):
        pass
    def display(self):
        pass
    def info(self):
        pass
    def reacttest(self):
        pass
    def simulate(slef):
        pass

class widgets:
    def __init__(self,screen, label):#initializes the widgets class
        self.screen = screen
        self.label = label
        self.variable = customtkinter.StringVar()

    def addslider(self, widgetfrom, widgetto): #adds a slider to the screen
        self.slider = customtkinter.CTkSlider(self.screen, from_= widgetfrom, to= widgetto)
        self.slider.pack(padx=20, pady=20)
        self.placeholdertext=self.slider.get()
        print(self.slider.get()) #test code

    def addtoggle(self): 
        def toggleevent():
            self.togglestate = self.toggle.get() #action when toggle is used

        #adds a toggle to the screen
        self.toggle = customtkinter.CTkSwitch(self.screen, text=self.label, command=toggleevent, onvalue=True, offvalue=False)
        self.toggle.pack(padx=20, pady=60)

    def adddropdown(self): 
        def dropdownevent(choice):
            self.dropdownchoice = choice #action when dropdown menu is used

        #adds a dropdown menu to the screen
        self.dropdown = customtkinter.CTkOptionMenu(self.screen, values=["test1", "test2", "test3"], command=dropdownevent)
        self.dropdown.set("test1")
        self.dropdown.pack(padx=20, pady=80)

    def addbutton(self): 
        def buttonevent():
            print("button pressed")#action when button is pressed

        #adds a button to the screen
        self.button = customtkinter.CTkButton(self.screen, text=self.label, command=buttonevent)
        self.button.pack(padx=20, pady=100)

    def addtextentry(self): #adds a text entry box to the screen
        self.entry =  customtkinter.CTkEntry(self.screen, textvariable= self.variable)
        self.entry.pack(padx=20, pady=40)

    #there are no default labels in the customtkinter module for the slider or text entry widgets so they have to be created manually here
    def addlabel(self): #adds a label to the screen
        self.manuallabel = customtkinter.CTkLabel(self.screen, text="CTkLabel", fg_color="transparent")
        self.manuallabel.pack(padx=20, pady=20)

#test code
test =inputscreen()
testscreen= test.getdisplay()
testvar = "testing"
widgets1 = widgets(testscreen, "test")
widgets1.addslider(0,100)
widgets1.addtextentry()
widgets1.addtoggle()
widgets1.adddropdown()
widgets1.addbutton()
testscreen.mainloop()
print()