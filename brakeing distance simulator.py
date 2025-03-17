#imports
import pygame
import tkinter
import customtkinter
import math
import time
import threading  


class inputscreen:
    def __init__(self): #initializes the customtkinter screen
        self.screen = customtkinter.CTk() 

        self.screen.eval('tk::PlaceWindow . center') #centers the window
        customtkinter.set_appearance_mode("defult") #sets the window to th uers system mode
        self.screen.title("Braking Distance Simulator") #sets the title of the window

        #sets the window to full screen
        width = self.screen.winfo_screenwidth()
        height = self.screen.winfo_screenheight()
        geometry = str(width) + "x" + str(height)
        self.screen.geometry(geometry)

    def getdisplay(self):
        return self.screen
    def validate(self):
        #validates the input data

        #assigns the widgets to a list
        widgets = [ self.Reacttimewidgets, self.Gravitywidgets, self.Velocitywidgets, self.Masswidgets, self.Clampforcewidgets]
        tempaturewidgets = [self.Ambienttempwidgets, self.Diskdencitywidgets, self.Brakemeltingpointwidgets, self.Disksvolumewidgets]
        coefficients = [self.fricitioncobrakeswidgets, self.frictioncoregenwidgets, self.Fricitioncotyreswidgets]

        dropdownbrakemeltpoint = [["Cast iron (1150)", "AL-MMC (660)", "ceramic (1800)", "carbon composite (3000)"],[1150, 660, 1800, 3000]]
        dropdowngravity = [["Sun (274.13)", "Mercury (3.59)", "Venus (8.87)", "Earth (9.81)", "Moon (1.62)", "Mars (3.77)", "Jupiter (25.95)", "Saturn (11.08)", "Uranus (10.67)", "Neptune (14.07)", "Pluto (0.42)"], [274.13, 3.59, 8.87, 9.81, 1.62, 3.77, 25.95, 11.08, 10.67, 14.07, 0.42]]
        dropdownfricitioncotyres = [["Dry asphalt (0.9)", "Wet asphalt(0.6)","Dry gravel(0.6)","Dry dirt (0.5)", "Wet Gravel (0.4)","loose sand (0.3)", "Snow (0.2)", "Ice (0.1)"], [0.9, 0.6, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]]
        failedlist = []

        self.Runtemp = self.Runtempwidgets.returntogglestate()

        #assigns the dropdown menu values to the correct value
        for i in range(len(dropdownbrakemeltpoint[0])):
            if self.Brakemeltingpointwidgets.returnvalue() == dropdownbrakemeltpoint[0][i]:
                self.Brakemeltingpointwidgets.variable.set(dropdownbrakemeltpoint[1][i])
        
        for i in range(len(dropdowngravity[0])):
            if self.Gravitywidgets.returnvalue() == dropdowngravity[0][i]:
                self.Gravitywidgets.variable.set(dropdowngravity[1][i])
        
        for i in range(len(dropdownfricitioncotyres[0])):
            if self.Fricitioncotyreswidgets.returnvalue() == dropdownfricitioncotyres[0][i]:
                self.Fricitioncotyreswidgets.variable.set(dropdownfricitioncotyres[1][i])
    
        
        #checks that the input data is a number
        for widget in widgets:
            try:
                float(widget.returnvalue())
            except:
                failedlist.append(widget.getlabel())

        #checks that the input data is within the correct range

        for coefficient in coefficients:
                try:
                    if float(coefficient.returnvalue()) < 0 or float(coefficient.returnvalue()) > 1:
                        failedlist.append(coefficient.getlabel())
                except:
                    failedlist.append(coefficient.getlabel())

        try:
            if float(self.Gradewidgets.returnvalue()) < -100 or float(self.Gradewidgets.returnvalue()) > 100:
                failedlist.append(self.Gradewidgets.getlabel())
        except:
            failedlist.append(self.Gradewidgets.getlabel())

            #checks that the optional tempuature input data is a number if the toggle is on
        if self.Runtempwidgets.returntogglestate() == True:
            for tempaturewidget in tempaturewidgets:
                try:
                    float(tempaturewidget.returnvalue())
                except:
                    failedlist.append(tempaturewidget.getlabel())

        #checks that the optional input of multiplyer is a number if the toggle is on
        if self.usemultiplierwidgets.returntogglestate() == True:
            try:
                float(self.multiplierwidgets.returnvalue())
            except:
                failedlist.append(self.multiplierwidgets.getlabel())
            
        #creates a textbox with the failed list
        if failedlist:
            textbox = customtkinter.CTkTextbox(self.screen, width=500, height=50)
            textbox.grid(row=15, column=4)
            textbox.delete("0.0", "end")  # delete all text
            textbox.insert("0.0", "Please enter a valid number for the following fields: " + ", ".join(failedlist))  # insert at line 0 character 0
            textbox.configure(state="disabled")  # configure textbox to be read-only
            return(failedlist)

        #test code 
        for widget in widgets:
            print(widget.returnvalue())
        for coefficient in coefficients:
            print(coefficient.returnvalue())
        print(self.Runtempwidgets.returntogglestate())
        for tempaturewidget in tempaturewidgets:
            print(tempaturewidget.returnvalue())
        print(self.usemultiplierwidgets.returntogglestate())
        print(self.multiplierwidgets.returnvalue())
        print(failedlist)
        
  
    def display(self):
        #initalise all of the widgets 
        self.Runtempwidgets = widgets(self.screen, "Tempature calculation")
        self.Ambienttempwidgets = widgets(self.screen, "Ambient Temp (C) ")
        self.Diskdencitywidgets = widgets(self.screen, "Brake disk density (g/cm^3)")
        self.Brakemeltingpointwidgets = widgets(self.screen, "Brake Melting Point (C) ")
        self.Disksvolumewidgets = widgets(self.screen, "Disk Volume (cm^3)")
        self.Reacttimewidgets = widgets(self.screen, "Reaction Time (s)")
        self.Gravitywidgets = widgets(self.screen, "Gravity (m/s^2)")
        self.Velocitywidgets = widgets(self.screen, "Velocity (m/s)")
        self.fricitioncobrakeswidgets = widgets(self.screen, "Friction Coefficient Brakes")
        self.frictioncoregenwidgets = widgets(self.screen, "Friction Coefficient Regen")
        self.Fricitioncotyreswidgets = widgets(self.screen, "Friction Coefficient Tyres")
        self.Masswidgets = widgets(self.screen, "Mass (kg)")
        self.Gradewidgets = widgets(self.screen, "Grade (%)")
        self.Clampforcewidgets = widgets(self.screen, "Clamp Force (N)")
        self.usemultiplierwidgets = widgets(self.screen, "Use Multiplyer")
        self.multiplierwidgets = widgets(self.screen, "Multiplier")
        
        #add the widgets to the screen
        self.Runtempwidgets.addtoggle([self.Ambienttempwidgets, self.Diskdencitywidgets, self.Brakemeltingpointwidgets, self.Disksvolumewidgets],0, 0) #adds the tempature calculation toggle
        self.usemultiplierwidgets.addtoggle([self.multiplierwidgets], 0, 14)  #adds the multiplier toggle

        #adds ambient tempature widgets
        self.Ambienttempwidgets.addlabel(0, 1)
        self.Ambienttempwidgets.addtextentry(1, 1)
        self.Ambienttempwidgets.addslider(-100, 100, 2, 1)

       #adds brake melting point widgets
        self.Brakemeltingpointwidgets.addlabel(0, 2) 
        self.Brakemeltingpointwidgets.addtextentry(1, 2)
        self.Brakemeltingpointwidgets.adddropdown(["Cast iron (1150)", "AL-MMC (660)", "ceramic (1800)", "carbon composite (3000)"], 2, 2, "Cast iron (1150)")
        
        #adds disk dencity widgets
        self.Diskdencitywidgets.addlabel(0, 3)
        self.Diskdencitywidgets.addtextentry(1, 3)
        self.Diskdencitywidgets.addslider(0, 10, 2, 3)

        #adds disk volume widgets
        self.Disksvolumewidgets.addlabel(0, 4)
        self.Disksvolumewidgets.addtextentry(1, 4)
        self.Disksvolumewidgets.addslider(100, 500, 2, 4)

        #adds reaction time widgets
        self.Reacttimewidgets.addlabel(0, 5)
        self.Reacttimewidgets.addtextentry(1, 5)
        self.Reacttimewidgets.addbutton(2, 5, "reaction time test", self.reacttest)
        
        #adds gravity widgets
        self.Gravitywidgets.addlabel(0, 6)
        self.Gravitywidgets.addtextentry(1, 6)
        self.Gravitywidgets.adddropdown(["Sun (274.13)", "Mercury (3.59)", "Venus (8.87)", "Earth (9.81)", "Moon (1.62)", "Mars (3.77)", "Jupiter (25.95)", "Saturn (11.08)", "Uranus (10.67)", "Neptune (14.07)", "Pluto (0.42)"], 2, 6, "Earth (9.81)")

        #adds velocity widgets
        self.Velocitywidgets.addlabel(0, 7)
        self.Velocitywidgets.addtextentry(1, 7)
        self.Velocitywidgets.addslider(1, 100, 2, 7)

        #adds fricition coefficent of the brakes widgets
        self.fricitioncobrakeswidgets.addlabel(0, 8)
        self.fricitioncobrakeswidgets.addtextentry(1, 8)
        self.fricitioncobrakeswidgets.addslider(20, 80, 2, 8)

        #adds fricition coefficent of the regen widgets
        self.frictioncoregenwidgets.addlabel(0, 9)
        self.frictioncoregenwidgets.addtextentry(1, 9)
        self.frictioncoregenwidgets.addslider(10, 30, 2, 9)

        #adds fricition coefficent of the tyres widgets
        self.Fricitioncotyreswidgets.addlabel(0, 10)
        self.Fricitioncotyreswidgets.addtextentry(1, 10)
        self.Fricitioncotyreswidgets.adddropdown(["Dry asphalt (0.9)", "Wet asphalt(0.6)","Dry gravel(0.6)","Dry dirt (0.5)", "Wet Gravel (0.4)","loose sand (0.3)", "Snow (0.2)", "Ice (0.1)"], 2, 10, "Dry asphalt (0.9)")

        #adds mass widgets
        self.Masswidgets.addlabel(0, 11)
        self.Masswidgets.addtextentry(1, 11)
        self.Masswidgets.addslider(100, 2000, 2, 11)

        #adds grade widgets
        self.Gradewidgets.addlabel(0, 12)
        self.Gradewidgets.addtextentry(1, 12)
        self.Gradewidgets.addslider(-50, 50, 2, 12) 

        #adds clamp force widgets
        self.Clampforcewidgets.addlabel(0, 13)
        self.Clampforcewidgets.addtextentry(1, 13)

        #adds the use multiplyer toggle
        self.usemultiplierwidgets.addtoggle(self.multiplierwidgets,0, 14)

        #adds multiplyer widgets
        self.multiplierwidgets.addtextentry(1, 14)  

        #adds the simulate button
        simulatebutton = customtkinter.CTkButton(self.screen, text="Simulate", command=self.simulate) 
        simulatebutton.grid(row=15, column=0, padx=10, pady=10)

        #adds the info button
        infobutton = customtkinter.CTkButton(self.screen, text="Info", command=self.info)
        infobutton.grid(row=15, column=1, padx=10, pady=10) 



        self.screen.mainloop()  # Start the event loop
    def info(self):
        pass
    def reacttest(self):
        print("testing ur reactions :)")
        pass


    def simulate(self): #manages  the simulation by calling each method and class as reqired 
        print("Starting simulation")
        failedlist = self.validate()
        if failedlist is None:
            runsimulation = simulation(self.Runtemp, self.Ambienttempwidgets.returnvalue(), self.Diskdencitywidgets.returnvalue(), self.Brakemeltingpointwidgets.returnvalue(), self.Disksvolumewidgets.returnvalue(), self.Reacttimewidgets.returnvalue(), self.Gravitywidgets.returnvalue(), self.Velocitywidgets.returnvalue(), self.fricitioncobrakeswidgets.returnvalue(), self.frictioncoregenwidgets.returnvalue(), self.Fricitioncotyreswidgets.returnvalue(), self.Masswidgets.returnvalue(), self.Gradewidgets.returnvalue(), self.Clampforcewidgets.returnvalue(), self.usemultiplierwidgets.returntogglestate(), self.multiplierwidgets.returnvalue())
            runsimulation.conversions()
            runsimulation.lock()
            runsimulation.stopingdistance()
            if self.Runtempwidgets.returntogglestate() == True:
                runsimulation.tempcalclations()
            print("Before stopingtime")
            runsimulation.stopingtime()
            print("After stopingtime")
            simulatedvalues = runsimulation.returnvalues()#brakeingdistance, stoppingdistance, brakeingtime, stoppingtime, islock, maxtemp, tempchange,  heatgen, Brakemeltingpoint, stop, runtemp, initialvelocity, ambienttemp
            print(simulatedvalues)
            if self.Runtemp == True:
                outputscreen = resultsscreen(simulatedvalues[0], simulatedvalues[1], simulatedvalues[2], simulatedvalues[3], simulatedvalues[4], simulatedvalues[5], simulatedvalues[6], simulatedvalues[7], simulatedvalues[8], simulatedvalues[9], simulatedvalues[10], self.Velocitywidgets.returnvalue(), self.Ambienttempwidgets.returnvalue())
            else:
                outputscreen = resultsscreen(simulatedvalues[0], simulatedvalues[1], simulatedvalues[2], simulatedvalues[3], simulatedvalues[4], None, None, None ,None, simulatedvalues[9], simulatedvalues[10], self.Velocitywidgets.returnvalue(), None)
            simulation_thread = threading.Thread(target=outputscreen.animation)
            simulation_thread.start()
            simulation_thread.join()  # Wait for the animation thread to finish
            outputscreen.results()
            

class widgets:
    def __init__(self,screen, label):#initializes the widgets class
        self.screen = screen
        self.label = label
        self.variable = customtkinter.StringVar()  # Initialize variable

    def addslider(self, widgetfrom, widgetto, column, row): #adds a slider to the screen
        def sliderevent(value):
            self.variable.set(round(self.slider.get())) # type: ignore # action when slider is used
            
            # as the slider cannot take decimal values, for coefficients the output has to be converted from a percentage to a decimal 
            if self.label in ["Friction Coefficient Brakes", "Friction Coefficient Regen", "Friction Coefficient Tyres"]:
                self.variable.set(str(float(self.variable.get()) / 100))  

        self.slider = customtkinter.CTkSlider(self.screen, from_=widgetfrom, to=widgetto, command=sliderevent)
        self.slider.grid(row=row, column=column, padx=10, pady=10)
        self.variable.set(round(self.slider.get(),2)) # type: ignore
        



    def addtoggle(self, affectingvalues, column, row): 
        def toggleevent(): #action when toggle is used
            self.togglestate = self.toggle.get()
            try: #if there is only one widget that is affected by the toggle this causes an error so it is handles seperatly
                for widget in affectingvalues:
                    if not self.togglestate:
                        widget.variable.set("Not required") # Set to not required when toggle is off
                    else:
                        widget.variable.set("")  # Reset to empty when toggle is on
            except:
                if not self.togglestate:
                    affectingvalues.variable.set("Not required") # Set to not required when toggle is off

        #adds a toggle to the screen
        self.toggle = customtkinter.CTkSwitch(self.screen, text=self.label, command=toggleevent, onvalue=True, offvalue=False)
        self.toggle.grid(row=row, column=column, padx=10, pady=10)
        self.togglestate = self.toggle.get()  # Initialize the toggle state

    def adddropdown(self, options, column, row, defultoption): 
        self.dropdownchoice = 0
        def dropdownevent(choice):
            self.dropdownchoice = choice #action when dropdown menu is used

        #adds a dropdown menu to the screen
        self.dropdown = customtkinter.CTkOptionMenu(self.screen, values=options, command=dropdownevent, variable=self.variable)
        self.dropdown.set(defultoption)
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

    def returnvalue(self):
        if hasattr(self, 'slider') and self.variable.get() == "":
            return self.slider.get()
        return self.variable.get()

    def returntogglestate(self):
        return self.togglestate
    
    def getlabel(self):
        return self.label

class simulation:
    def __init__(self,  Runtemp, Ambienttemp, Diskdencity, Brakemeltingpoint, Diskvolume, Reacttime, Gravity, Velocity, fricitioncobrakes, frictioncoregen, Fricitioncotyres, Mass, Grade, Clampforce, usemultiplier, multiplier):
        #initaliseation method
        self.Runtemp = Runtemp
        print(self.Runtemp)
        if self.Runtemp == True:
            print("true")
            #print(Diskdencity)
            self.Ambienttemp = float(Ambienttemp)
            self.Diskdencity = float(Diskdencity)
            self.Diskvolume = float(Diskvolume)
            self.Brakemeltingpoint = float(Brakemeltingpoint)
        self.Reacttime = float(Reacttime)
        self.Gravity = float(Gravity)
        self.Velocity = float(Velocity)
        self.fricitioncobrakes = float(fricitioncobrakes)
        self.frictioncoregen = float(frictioncoregen)
        self.Fricitioncotyres = float(Fricitioncotyres)
        self.Mass = float(Mass)
        self.Grade = float(Grade)
        self.Clampforce = float(Clampforce)
        self.usemultiplier = usemultiplier
        self.tempchange = 0
        self.stop = True
        if usemultiplier == True:
            self.multiplier = float(multiplier)

    def conversions(self): #convets the input data to stadard units
        if self.Runtemp == True:
            self.Diskdencity = self.Diskdencity * 1000 #coverts the brake disk dencity to kg/m^3
            self.Diskvolume = self.Diskvolume * 0.000001 # coverts the disk volume to m^3
        self.Grade = self.Grade / 100 #coverts the grade to a decimal


    def lock(self): #checks if the wheels of the vehicle has locked
        if ((self.Fricitioncotyres + self.Grade)* self.Gravity * self.Mass) >= (2 * (self.fricitioncobrakes + self.frictioncoregen) *self.Clampforce):
            self.islock = False 
        else:
            self.islock = True

    def stopingdistance(self): #calculates the brakeing and stopping distance of the vehicle
        totalcoeficent = self.fricitioncobrakes + self.frictioncoregen

        if self.islock == False: #if the wheels have not locked
            print("not locked")
            denominator = 2 * self.Gravity * (totalcoeficent  + self.Grade)
            if denominator <= 0: #if the denominator is 0 the vehicle will not stop
                self.stop = False
            numerator = self.Velocity ** 2
            self.brakeingdistance = numerator / denominator
        else: #if the wheels have locked
            print("locked")
            numerator = 0.5 * self.Mass * (self.Velocity ** 2)
            denominator = (totalcoeficent + self.Grade) * self.Mass * self.Gravity
            if denominator <= 0: #if the denominator is 0 the vehicle will not stop
                self.stop = False
            self.brakeingdistance = numerator / denominator

        #applys the multiplyer if it is enabled 
        if self.usemultiplier == True:
            self.brakeingdistance = self.brakeingdistance * self.multiplier

        self.stoppingdistance = self.brakeingdistance + (self.Reacttime * self.Velocity)


    
    def tempcalclations(self): #calculates the tempature of the brake disk
        self.heatgen = self.Mass * self.Velocity * 0.5 #calculates the heat generated in the brakeing process

        #relates a melting point to a heat capacity, this process is not 100% accurate but is a good estimate
        #then calculates the tempature change of the disk

        if self.Brakemeltingpoint > 500 and self.Brakemeltingpoint <= 660:
            self.tempchange = self.heatgen / (self.Diskdencity * self.Diskvolume * 4 * 887)

        elif self.Brakemeltingpoint > 1100 and self.Brakemeltingpoint <= 1200:
            self.tempchange = self.heatgen / (self.Diskdencity * self.Diskvolume * 4 * 920)

        elif self.Brakemeltingpoint > 1200 and self.Brakemeltingpoint <= 1800: 
            self.tempchange = self.heatgen / (self.Diskdencity * self.Diskvolume * 4 * 554)

        #if the tempature is not in one of the ranges above the user will be asked to input the heat capacity of the disk
        else:
            self.popup_done = threading.Event()  # Event to wait for popup submission

            def popupevent(): # button event loop
                try:
                    entered_value = popuptextentry.get()
                    print(f"Entered value: {entered_value}")
                    self.tempchange = self.heatgen / (self.Diskdencity * self.Diskvolume * 4 * float(entered_value)) # calculates the tempature change of the disk
                    self.popup_done.set()  # Signal that the popup is done
                    popup.destroy()  # Close the popup window
                    popup.quit()  # Quit the popup event loop

                except Exception as e:
                    print(f"Error: {e}")
                    # destroy the error label if it already exists and creates a new one
                    if hasattr(popupevent, 'error_label'):
                        popupevent.error_label.destroy()
                    popupevent.error_label = customtkinter.CTkLabel(popup, text="Please enter a valid number", fg_color="transparent")
                    popupevent.error_label.grid(row=3, column=0, padx=10, pady=10)

            popup = customtkinter.CTk() # creates window
            popup.eval('tk::PlaceWindow . center') # centers the window
            popup.title("Specific heat capacity") # sets the title of the window

            # sets the size of the window
            width = 700
            height = 100
            geometry = str(width) + "x" + str(height)
            popup.geometry(geometry)

            # adds the widgets to the screen
            self.specificheatcapacity = customtkinter.StringVar() 
            
            label = customtkinter.CTkLabel(popup, text="Material not recognized, please enter its specific heat capacity", fg_color="transparent")
            label.grid(row=0, column=0, padx=10, pady=10)
            popuptextentry = customtkinter.CTkEntry(popup, textvariable=self.specificheatcapacity)
            popuptextentry.grid(row=0, column=1, padx=10, pady=10)
            
            #adds a button to the screen
            button = customtkinter.CTkButton(popup, text="Submit", command=lambda: popupevent())
            button.grid(row=0, column=2, padx=10, pady=10)

            popup.mainloop()  # Start the popup event loop
            self.popup_done.wait()  # Wait for the popup to be submitted


        self.maxtemp = self.tempchange + self.Ambienttemp # calculates the max tempature of the disk

    def stopingtime(self): #calculates the stopping time of the vehicle
        denominator = (self.fricitioncobrakes + self.frictioncoregen + self.Grade)* self.Gravity
        self.brakeingtime = self.Velocity / denominator
        
        #applies the multiplier if it is enabled
        if self.usemultiplier == True:
            self.brakeingtime = self.brakeingtime * self.multiplier
        self.stoppingtime = self.brakeingtime + self.Reacttime
    
    def returnvalues(self): #returns the results of the simulation
        if self.Runtemp == True:
            return(self.brakeingdistance, self.stoppingdistance, self.brakeingtime, self.stoppingtime, self.islock, self.maxtemp, self.tempchange,  self.heatgen, self.Brakemeltingpoint, self.stop, self.Runtemp)
        else:
            return(self.brakeingdistance, self.stoppingdistance, self.brakeingtime, self.stoppingtime, self.islock, None, None, None, None, self.stop, self.Runtemp)

        
class resultsscreen():
    def __init__(self, brakeingdistance, stoppingdistance, brakeingtime, stoppingtime, islock, maxtemp, tempchange,  heatgen, Brakemeltingpoint, stop, runtemp, initialvelocity, ambienttemp):
        # define varables 
        self.brakeingdistance = brakeingdistance
        self.stoppingdistance = stoppingdistance
        self.brakeingtime = brakeingtime
        self.stoppingtime = stoppingtime
        self.islock = islock
        self.initalvelocity = initialvelocity
        self.runtemp = runtemp
        if self.runtemp == True:
            self.maxtemp = float(maxtemp)  
            self.ambianttemp = float(ambienttemp)
            self.brakemeltingpoint = float(Brakemeltingpoint)
            self.tempchange = float(tempchange)
            self.heatgen = float(heatgen)
        else:
            self.maxtemp = None
            self.ambianttemp = None
            self.brakemeltingpoint = None
        self.stop = stop


       # Set up the display
        self.screenwidth = 1800
        self.screenheight = 1000
        self.screen = pygame.display.set_mode((self.screenwidth, self.screenheight))
        pygame.display.set_caption("Braking Distance Simulator")
        self.paused = False
        self.restart = False
        pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONDOWN])  # Allow specific events

    def toggle_pause(self):
        self.paused = not self.paused

    def restart_animation(self):
        self.restart = True

    def animation(self):
 
        frame = 0
        # Load images
        car = pygame.image.load("car.png")
        background = pygame.image.load("background.jpg")
        leftwheel = pygame.image.load("wheel.png")
        rightwheel = pygame.image.load("wheel.png")

        # Scale images
        car = pygame.transform.scale_by(car, 0.5)
        leftwheel = pygame.transform.scale_by(leftwheel, 0.5)
        rightwheel = pygame.transform.scale_by(rightwheel, 0.5)

        # Clock setup
        clock = pygame.time.Clock()

        # Background scrolling variables
        bg_x = 0
        #scroll_speed = 5  test code
        deceliration = float(self.initalvelocity) / float(self.brakeingtime) #calculates the deceliration of the car per second
        deceliration = deceliration / 60 #converts the deceliration to per frame

        reactionframes = round((self.stoppingtime - self.brakeingtime)*60)  # Calculate the number of frames for the reaction time

        # Initialize font
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 30)

        distancetraveled = 0  # Initialize distance traveled
        starttime = pygame.time.get_ticks()  # Initialize start time

        # calculate tempature change per frame 
        if self.maxtemp is not None:
            tempchangeperframe = ((self.maxtemp - self.ambianttemp) / self.brakeingtime) / 60 # type: ignore

        # Initialize buttons
        button_width = 100
        button_height = 50  
        pause_button = pygame.Rect(self.screenwidth - button_width - 20, self.screenheight - button_height - 20, button_width, button_height)
        restart_button = pygame.Rect(self.screenwidth - 2 * button_width - 40, self.screenheight - button_height - 20, button_width, button_height)

        running = True
        wheelspeed = None  # Initialize wheelspeed to avoid reference before assignment
        bufferframe = 0  # Initialize bufferframe to avoid reference before assignment

        #Car constants
        car_x = 500
        car_y = self.screenheight - car.get_height() - 450  # Place the car on the road
        leftwheel_x = 580
        rightwheel_x = 1033
        leftwheel_y = self.screenheight - car.get_height() - 146
        rightwheel_y = self.screenheight - car.get_height() - 146 #
        circumference = rightwheel.get_height() * math.pi

        #car attributes  
        while running:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if pause_button.collidepoint(mouse_pos):
                        self.toggle_pause()
                    elif restart_button.collidepoint(mouse_pos):
                        self.restart_animation()

            if self.restart:
                frame = 0
                distancetraveled = 0
                starttime = pygame.time.get_ticks()
                self.restart = False

            if not self.paused and self.stop:
                #update the deceliration of the car
                if frame > reactionframes:
                    currentvelocity = float(self.initalvelocity) - (deceliration * (frame - reactionframes))
                    if currentvelocity <= 0:
                        currentvelocity = 0 #stops the car if it has reached 0 velocity so it dosent go into negative velocity
                else:
                    currentvelocity = float(self.initalvelocity)
                # Update background position
                bg_x -= currentvelocity
                if bg_x <= -background.get_width():
                    bg_x = 0

                # Calculate distance traveled
                distancetraveled += currentvelocity / 60  # Assuming 60 FPS

                # Draw background (two instances for scrolling)
                self.screen.fill((255, 255, 255))
                self.screen.blit(background, (bg_x, -200))
                self.screen.blit(background, (bg_x + background.get_width(), -200))

                # Draw car

                self.screen.blit(car, (car_x, car_y))
                if self.islock == False:
                    #calculate the rotation of the wheels
                    rotationangle = 360 *  (currentvelocity / circumference) 

                    # Make the wheels rotate
                    rightwheelrotated = pygame.transform.rotate(rightwheel, rotationangle* (frame-reactionframes))
                    leftwheelrotated = pygame.transform.rotate(leftwheel, rotationangle* (frame - reactionframes))

                    # Calculate new positions to keep the wheels centered
                    rightwheelrect = rightwheelrotated.get_rect(center=(rightwheel_x + rightwheel.get_width() // 2, rightwheel_y + rightwheel.get_height() // 2))
                    leftwheelrect = leftwheelrotated.get_rect(center=(leftwheel_x + leftwheel.get_width() // 2, leftwheel_y + leftwheel.get_height() // 2))
                    # create  wheel speed meter
                    wheelspeed = font.render(f'Speedometer: {currentvelocity:.2f} m/s', True, (0, 0, 0))

                    self.screen.blit(leftwheelrotated, leftwheelrect.topleft)
                    self.screen.blit(rightwheelrotated, rightwheelrect.topleft)
                else:
                    wheelvelcoity = 0 
                    wheelspeed = font.render(f'Speedometer: {wheelvelcoity:.2f} m/s', True, (0, 0, 0))
                    self.screen.blit(leftwheel, (leftwheel_x, leftwheel_y))
                    self.screen.blit(rightwheel, (rightwheel_x, rightwheel_y))
                    # Display lock warning
                    lockwarning = font.render('Warning: Wheels Locked!', True, (255, 0, 0))
                    self.screen.blit(lockwarning, (10, self.screenheight - 220))

                
                self.screen.blit(wheelspeed, (10, self.screenheight - 100)) #wheels speed meter

                # create Ground speed meter
                speedtext = font.render(f'Ground Speed: {currentvelocity:.2f} m/s', True, (0, 0, 0))
                self.screen.blit(speedtext, (10, self.screenheight - 70))

                # Render the distance traveled text
                distancetext = font.render(f'Distance Traveled: {distancetraveled:.2f} m', True, (0, 0, 0))
                self.screen.blit(distancetext, (10, self.screenheight - 130))

                elapsedtime = (pygame.time.get_ticks() - starttime) / 1000  # Calculate elapsed time in seconds

                # Render the timer text
                timertext = font.render(f'Time Elapsed: {elapsedtime:.2f} s', True, (0, 0, 0))
                self.screen.blit(timertext, (10, self.screenheight - 160))


                # the temperature meter if temperature calculations were done
                if self.maxtemp is not None and currentvelocity > 0 and frame > reactionframes:
                    currenttemp = tempchangeperframe * (frame - reactionframes) + self.ambianttemp
                    if self.islock == True: # if the wheels have locked the tempature dosnt change 
                        currenttemp = self.maxtemp
                    temptext = font.render(f'Temperature: {currenttemp:.2f} °C', True, (0, 0, 0))
                    self.screen.blit(temptext, (10, self.screenheight - 190))
                    # check if brakes have failed due to tempature
                    if currenttemp > self.brakemeltingpoint: # type: ignore
                        self.screen.blit(font.render('Warning: Brakes have failed due to high temperature!', True, (255, 0, 0)), (10, self.screenheight - 250)) 
                        self.stop = False
                else:
                    if currentvelocity <= 0 and self.maxtemp is not None: #checks if the car has stooped
                        currenttemp = self.maxtemp #if it has sets the current tempature to the maximum tempature reached 
                    else:
                        currenttemp = self.ambianttemp
                    if self.maxtemp is not None: #renders the tempaturre meter to the screen if the tempature calculations are done.
                        temptext = font.render(f'Temperature: {currenttemp:.2f} °C', True, (0, 0, 0))
                        self.screen.blit(temptext, (10, self.screenheight - 190))
            

                #stops the simulation if the car has stopped
                if distancetraveled >= self.stoppingdistance:
                    # bufferframe is used to stop the simulation after the car has stopped for 2 seconds,
                    #  the 2 seconds is reqired to make sure the animation has finished as there is a delay of all of the  objects being added to the screen on lower end devices.
                    bufferframe = bufferframe +1
                    if bufferframe >= 120:
                        self.paused = True
                        print("Car has stopped")
                        return()
                else:
                    bufferframe = 0
                
            if not self.stop: #handles if the car wont stop 
                self.screen.fill((255, 255, 255))  # Clear the screen
                stoppingwarning = font.render("Warning: Car will not stop. Simulation paused, please input different values.", True, (255, 0, 0))
                self.screen.blit(stoppingwarning, (10, self.screenheight - 250))
                self.paused = True
                pygame.display.update()
                return()
            
            # Draw buttons
            pygame.draw.rect(self.screen, (0, 255, 0), pause_button)
            pygame.draw.rect(self.screen, (255, 0, 0), restart_button)
            pause_text = font.render('Pause' if not self.paused else 'Play', True, (0, 0, 0))
            restart_text = font.render('Restart', True, (0, 0, 0))
            pause_text_rect = pause_text.get_rect(center=pause_button.center)
            restart_text_rect = restart_text.get_rect(center=restart_button.center)
            self.screen.blit(pause_text, pause_text_rect)
            self.screen.blit(restart_text, restart_text_rect)

            # Draw text
            if wheelspeed:
                self.screen.blit(wheelspeed, (10, self.screenheight - 100))  # wheels speed meter
            self.screen.blit(speedtext, (10, self.screenheight - 70))  # ground speed meter
            self.screen.blit(distancetext, (10, self.screenheight - 130))  # distance traveled text
            self.screen.blit(timertext, (10, self.screenheight - 160))  # timer text
            if self.maxtemp is not None:
                self.screen.blit(temptext, (10, self.screenheight - 190))  # temperature text

            frame += 1
            # Update the display
            pygame.display.update()
            pygame.event.clear() #clears the event queue
            clock.tick(60)


    def results(self):
        print("results")
        # Set up the display
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, self.screenwidth, self.screenheight))  # Clear the screen
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 30)
        # Adds the results to arrays 
        outputs = [self.brakeingdistance, self.stoppingdistance, self.brakeingtime, self.stoppingtime, self.islock, self.maxtemp, self.tempchange, self.heatgen, self.brakemeltingpoint, self.stop, self.runtemp, self.initalvelocity, self.ambianttemp]
        outputtext = ["Braking Distance", "Stopping Distance", "Braking Time", "Stopping Time", "Wheels Locked", "Max Temperature", "Temperature Change", "Heat Generated", "Brake Melting Point", "Stop", "Run Temperature", "Initial Velocity", "Ambient Temperature"]
        position = [[10, self.screenheight - 30 * (i + 1)] for i in range(len(outputs))]
        # itterates through the array and displays the results
        for i in range(len(outputs)):
            text = font.render(f'{outputtext[i]}: {outputs[i]}', True, (0, 0, 0))
            self.screen.blit(text, (position[i][0], position[i][1]))
        
        pygame.display.update()

def main():


    dataentryscreen = inputscreen()
    dataentryscreen.display() 



main()


