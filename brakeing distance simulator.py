#imports
import pygame
import tkinter
import customtkinter



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
    def getlabel(self):
        return self.label

    def simulate(self):
        self.validate()
        runsimulation = simulation(self.Runtempwidgets.returnvalue, self.Ambienttempwidgets.returnvalue, self.Diskdencitywidgets.returnvalue, self.Brakemeltingpointwidgets.returnvalue, self.Disksvolumewidgets.returnvalue, self.Reacttimewidgets.returnvalue, self.Gravitywidgets.returnvalue, self.Velocitywidgets.returnvalue, self.fricitioncobrakeswidgets.returnvalue, self.frictioncoregenwidgets.returnvalue, self.Fricitioncotyreswidgets.returnvalue, self.Masswidgets.returnvalue, self.Gradewidgets.returnvalue, self.Clampforcewidgets.returnvalue, self.usemultiplierwidgets.returnvalue, self.multiplierwidgets.returnvalue)


class widgets:
    def __init__(self,screen, label):#initializes the widgets class
        self.screen = screen
        self.label = label
        self.variable = customtkinter.StringVar()

    def addslider(self, widgetfrom, widgetto, column, row): #adds a slider to the screen
        def sliderevent(value):
            self.variable.set(round(self.slider.get())) # action when slider is used
            
            # as the slider cannot take decimal values, for coefficients the output has to be converted from a percentage to a decimal 
            if self.label in ["Fricition Coefficent Brakes", "Fricition Coefficent Regen", "Fricition Coefficent Tyres"]:
                self.variable.set(str(float(self.variable.get()) / 100))  

        self.slider = customtkinter.CTkSlider(self.screen, from_=widgetfrom, to=widgetto, command=sliderevent)
        self.slider.grid(row=row, column=column, padx=10, pady=10)
        self.variable.set(round(self.slider.get(),2))
        



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

    def adddropdown(self, options, column, row, defultoption): 
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
        return self.toggle.get()
    
    def getlabel(self):
        return self.label

class simulation:
    def __init__(self,  Runtemp, Ambienttemp, Diskdencity, Brakemeltingpoint, Diskvolume, Reacttime, Gravity, Velocity, fricitioncobrakes, frictioncoregen, Fricitioncotyres, Mass, Grade, Clampforce, usemultiplier, multiplier):
        self.Runtemp = Runtemp
        self.Ambienttemp = Ambienttemp
        self.Diskdencity = Diskdencity
        self.Brakemeltingpoint = Brakemeltingpoint
        self.Diskvolume = Diskvolume
        self.Reacttime = Reacttime
        self.Gravity = Gravity
        self.Velocity = Velocity
        self.fricitioncobrakes = fricitioncobrakes
        self.frictioncoregen = frictioncoregen
        self.Fricitioncotyres = Fricitioncotyres
        self.Mass = Mass
        self.Grade = Grade
        self.Clampforce = Clampforce
        self.usemultiplier = usemultiplier
        self.multiplier = multiplier

    def conversions(self): #convets the input data to stadard units
        if self.Runtemp == True:
            self.Brakedencity = self.Diskdencity * 1000
            self.Diskvolume = self.Diskvolume * 0.000001 


    def lock(self): #checks if the wheels of the vehicle has locked
        if self.Fricitioncotyres * self.Gravity * self.Mass > 2 * self.fricitioncobrakes * self.Clampforce:
            self.lock = False 
        else:
            self.lock = True

    def stopingdistance(self): #calculates the stopping distance of the vehicle
        totalcoeficent = self.fricitioncobrakes + self.frictioncoregen

        if self.lock == False: #if the wheels have not locked
            denominator = 2 * totalcoeficent * self.Gravity
            numerator = self.Velocity ** 2
            self.stoppingdistance = numerator / denominator
        else: #if the wheels have locked
            numerator = 0.5 * self.Mass * (self.Velocity ** 2)
            denominator = totalcoeficent * self.Mass * self.Gravity
            self.stoppingdistance = numerator / denominator
    
    def tempcalclations(self): #calculates the tempature of the brake disk
        self.heatgen = self.Mass * self.Velocity *0.5 #calculates the heat generated in the brakeing process

        #relates a melting point to a heat capacity, this process is not 100% accurate but is a good estimate
        #then calculates the tempature change of the disk

        if self.Brakemeltingpoint > 500 self.Brakemeltingpoint < 660:
            self.tempchange = self.Diskdencity * self.Diskvolume * 4 * 887

        elif self.Brakemeltingpoint > 1100 and self.Brakemeltingpoint < 1200:
            self.tempchange = self.Diskdencity * self.Diskvolume * 4 * 920

        elif self.Brakemeltingpoint > 1200 and self.Brakemeltingpoint < 1800: 
            self.tempchange = self.Diskdencity * self.Diskvolume * 4 * 	554
        
        elif self.Brakemeltingpoint < 1800:
            self.tempchange = self.Diskdencity * self.Diskvolume * 4 * 850
        
        #if the tempature is not in one of the ranges above the user will be asked to input the heat capacity of the disk
        else:
            popup = customtkinter.CTk() 
            popup.eval('tk::PlaceWindow . center') #centers the window
            self.screen.title("Specifc heat capacity") #sets the title of the window

            width = 30
            height = 10
            geometry = str(width) + "x" + str(height)
            popup.geometry(geometry)
        
        self. maxtemp= self.tempchange + self.Ambienttemp # calculates the max tempature of the disk
    
    def stopingtime(self): #calculates the stopping time of the vehicle
        denominator = (self.fricitioncobrakes + self.Grade)* self.Gravity
        self.stoppingtime = self.Velocity / denominator

        
    
def main():

    dataentryscreen = inputscreen()
    dataentryscreen.display() 


main()

