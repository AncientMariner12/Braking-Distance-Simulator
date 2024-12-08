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
        Runtempwidgets = widgets(self.screen, "Tempature calculation")
        Ambienttempwidgets = widgets(self.screen, "Ambient Temp (C) ")
        Diskdencitywidgets = widgets(self.screen, "Brake disk dencity (g/cm^3)")
        Disksvolumewidgets = widgets(self.screen, "Disk Volume (cm^3)")
        Reacttimewidgets = widgets(self.screen, "Reaction Time (s)")
        Gravitywidgets = widgets(self.screen, "Gravity (m/s^2)")
        Velocitywidgets = widgets(self.screen, "Velocity (m/s)")
        fricitioncobrakeswidgets = widgets(self.screen, "Fricition Coefficent Brakes")
        Fricitioncotyreswidgets = widgets(self.screen, "Fricition Coefficent Tyres")
        Masswidgets = widgets(self.screen, "Mass (kg)")
        Gradewidgets = widgets(self.screen, "Grade (%)")
        Clampforcewidgets = widgets(self.screen, "Clamp Force (N)")
        
        #add the widgets to the screen
        Runtempwidgets.addtoggle(0, 0) #adds the tempature calculation toggle

        #adds ambient tempature widgets
        Ambienttempwidgets.addlabel(0, 1)
        Ambienttempwidgets.addtextentry(1, 1)
        Ambienttempwidgets.addslider(-100, 100, 2, 1)

        #adds disk dencity widgets
        Diskdencitywidgets.addlabel(0, 2)
        Diskdencitywidgets.addtextentry(1, 2)
        Diskdencitywidgets.addslider(0, 10, 2, 2)

        #adds disk volume widgets
        Disksvolumewidgets.addlabel(0, 3)
        Disksvolumewidgets.addtextentry(1, 3)
        Disksvolumewidgets.addslider(100, 500, 2, 3)

        #adds reaction time widgets
        Reacttimewidgets.addlabel(0, 4)
        Reacttimewidgets.addtextentry(1, 4)
        Reacttimewidgets.addbutton(2, 4, "reaction time test", self.reacttest)
        
        #adds gravity widgets
        Gravitywidgets.addlabel(0, 5)
        Gravitywidgets.addtextentry(1, 5)
        Gravitywidgets.adddropdown(["Sun (274.13)", "Mercury (3.59)", "Venus (8.87)", "Earth (9.81)", "Moon (1.62)", "Mars (3.77)", "Jupiter (25.95)", "Saturn (11.08)", "Uranus (10.67)", "Neptune (14.07)", "Pluto (0.42)"], 2, 5)

        #adds velocity widgets
        Velocitywidgets.addlabel(0, 6)
        Velocitywidgets.addtextentry(1, 6)
        Velocitywidgets.addslider(1, 100, 2, 6)

        #adds fricition coefficent of the brakes widgets
        fricitioncobrakeswidgets.addlabel(0, 7)
        fricitioncobrakeswidgets.addtextentry(1, 7)
        fricitioncobrakeswidgets.addslider(0.2, 0.8, 2, 7)

        #adds fricition coefficent of the tyres widgets
        Fricitioncotyreswidgets.addlabel(0, 8)
        Fricitioncotyreswidgets.addtextentry(1, 8)
        fricitioncobrakeswidgets.adddropdown(["Dry asphalt (0.9)", "Wet asphalt(0.6)","Dry gravel(0.6)","Dry dirt (0.5)", "Wet Gravel (0.4)","loose sand (0.3)", "Snow (0.2)", "Ice (0.1)"], 2, 8)

        #adds mass widgets
        Masswidgets.addlabel(0, 9)
        Masswidgets.addtextentry(1, 9)
        Masswidgets.addslider(100, 2000, 2, 9)

        #adds grade widgets
        Gradewidgets.addlabel(0, 10)
        Gradewidgets.addtextentry(1, 10)
        Gradewidgets.addslider(-50, 50, 2, 10) 

        #adds clamp force widgets
        Clampforcewidgets.addlabel(0, 11)
        Clampforcewidgets.addtextentry(1, 11)

        #adds the simulate button
        simulatebutton = customtkinter.CTkButton(self.screen, text="Simulate", command=self.simulate) 
        simulatebutton.grid(row=12, column=0, padx=10, pady=10)

        #adds the info button
        infobutton = customtkinter.CTkButton(self.screen, text="Info", command=self.info)
        infobutton.grid(row=12, column=1, padx=10, pady=10)    

        self.screen.mainloop()  # Start the event loop
    def info(self):
        pass
    def reacttest(self):
        print("testing ur reactions :)")
        pass
    def simulate(self):
        pass

class widgets:
    def __init__(self,screen, label):#initializes the widgets class
        self.screen = screen
        self.label = label
        self.variable = customtkinter.StringVar()

    def addslider(self, widgetfrom, widgetto, column, row): #adds a slider to the screen
        self.slider = customtkinter.CTkSlider(self.screen, from_= widgetfrom, to= widgetto)
        self.slider.grid(row=row, column=column, padx=10, pady=10)
        self.placeholdertext=round(self.slider.get(), 2)
        print(round(self.slider.get(),2)) #test code

    def addtoggle(self, column, row): 
        def toggleevent():
            self.togglestate = self.toggle.get() #action when toggle is used

        #adds a toggle to the screen
        self.toggle = customtkinter.CTkSwitch(self.screen, text=self.label, command=toggleevent, onvalue=True, offvalue=False)
        self.toggle.grid(row=row, column=column, padx=10, pady=10)

    def adddropdown(self, options, column, row): 
        def dropdownevent(choice):
            self.dropdownchoice = choice #action when dropdown menu is used

        #adds a dropdown menu to the screen
        self.dropdown = customtkinter.CTkOptionMenu(self.screen, values=options, command=dropdownevent)
        self.dropdown.set("choose an option")
        self.dropdown.grid(row=row, column=column, padx=10, pady=10)

    def addbutton(self, column, row, name, action): 

        #adds a button to the screen
        self.button = customtkinter.CTkButton(self.screen, text=name, command=action)
        self.button.grid(row=row, column=column, padx=10, pady=10)

    def addtextentry(self, column, row): #adds a text entry box to the screen
        self.entry =  customtkinter.CTkEntry(self.screen, textvariable= self.variable)
        self.entry.grid(row=row, column=column, padx=10, pady=10)


    #there are no default labels in the customtkinter module for the slider or text entry widgets so they have to be created manually here
    def addlabel(self, column, row): #adds a label to the screen
        self.manuallabel = customtkinter.CTkLabel(self.screen, text=self.label, fg_color="transparent")
        self.manuallabel.grid(row=row, column=column, padx=10, pady=10)

def main():
    dataentryscreen = inputscreen()
    dataentryscreen.display() 


main()

#test code

#test =inputscreen()
#testscreen= test.getdisplay()
#testvar = "testing"
#widgets1 = widgets(testscreen, "test")
#widgets1.addslider(0,100,20,20)
# widgets1.addtextentry(20, 40)
#widgets1.addtoggle(20, 60)
#widgets1.adddropdown(20, 80)
#widgets1.addbutton(20, 100)
#testscreen.mainloop()
#print()
