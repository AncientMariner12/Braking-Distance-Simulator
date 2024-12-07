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
        #initalise all of the widgets 
        Runtempwidgets = widgets(self.screen, "toggle tmpeture calc")
        Ambienttempwidgets = widgets(self.screen, "Ambient Temp")
        Diskdencitywidgets = widgets(self.screen, "Disk Dencity")
        disksvolumewidgets = widgets(self.screen, "Disks Volume")
        Reacttimewidgets = widgets(self.screen, "React Time")
        Gravitywidgets = widgets(self.screen, "Gravity")
        Velocitywidgets = widgets(self.screen, "Velocity")
        fricitioncobrakeswidgets = widgets(self.screen, "Fricition Co Brakes")
        Fricitioncotyreswidgets = widgets(self.screen, "Fricition Co Tyres")
        Masswidgets = widgets(self.screen, "Mass")
        Gradewidgets = widgets(self.screen, "Grade")
        Clampforcewidgets = widgets(self.screen, "Clamp Force")
        
        widgetlist =[Runtempwidgets, Ambienttempwidgets, Diskdencitywidgets, disksvolumewidgets, Reacttimewidgets, Gravitywidgets, Velocitywidgets, fricitioncobrakeswidgets, Fricitioncotyreswidgets, Masswidgets, Gradewidgets, Clampforcewidgets]
    def info(self):
        pass
    def reacttest(self):
        pass
    def simulate(self):
        pass

class widgets:
    def __init__(self,screen, label):#initializes the widgets class
        self.screen = screen
        self.label = label
        self.variable = customtkinter.StringVar()

    def addslider(self, widgetfrom, widgetto, x,y): #adds a slider to the screen
        self.slider = customtkinter.CTkSlider(self.screen, from_= widgetfrom, to= widgetto)
        self.slider.pack(padx=x, pady=y)
        self.placeholdertext=self.slider.get()
        print(self.slider.get()) #test code

    def addtoggle(self,x,y): 
        def toggleevent():
            self.togglestate = self.toggle.get() #action when toggle is used

        #adds a toggle to the screen
        self.toggle = customtkinter.CTkSwitch(self.screen, text=self.label, command=toggleevent, onvalue=True, offvalue=False)
        self.toggle.pack(padx=x, pady=y)

    def adddropdown(self,x,y): 
        def dropdownevent(choice):
            self.dropdownchoice = choice #action when dropdown menu is used

        #adds a dropdown menu to the screen
        self.dropdown = customtkinter.CTkOptionMenu(self.screen, values=["test1", "test2", "test3"], command=dropdownevent)
        self.dropdown.set("test1")
        self.dropdown.pack(padx=x, pady=y)

    def addbutton(self,x,y): 
        def buttonevent():
            print("button pressed")#action when button is pressed

        #adds a button to the screen
        self.button = customtkinter.CTkButton(self.screen, text=self.label, command=buttonevent)
        self.button.pack(padx=x, pady=y)

    def addtextentry(self,x,y): #adds a text entry box to the screen
        self.entry =  customtkinter.CTkEntry(self.screen, textvariable= self.variable)
        self.entry.pack(padx=x, pady=y)

    #there are no default labels in the customtkinter module for the slider or text entry widgets so they have to be created manually here
    def addlabel(self,x,y): #adds a label to the screen
        self.manuallabel = customtkinter.CTkLabel(self.screen, text="CTkLabel", fg_color="transparent")
        self.manuallabel.pack(padx=x, pady=y)

def main():
    dataentryscreen = inputscreen()
    dataentryscreen.display() 

main()

#test code
test =inputscreen()
testscreen= test.getdisplay()
testvar = "testing"
widgets1 = widgets(testscreen, "test")
widgets1.addslider(0,100,20,20)
widgets1.addtextentry(20, 40)
widgets1.addtoggle(20, 60)
widgets1.adddropdown(20, 80)
widgets1.addbutton(20, 100)
testscreen.mainloop()
print()