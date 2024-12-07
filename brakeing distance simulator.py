import pygame
import tkinter
import customtkinter



class inputscreen:
    def __init__(self):
        self.screen = customtkinter.CTk() 

        self.screen.eval('tk::PlaceWindow . center')
        customtkinter.set_appearance_mode("dark")
        self.screen.title("Braking Distance Simulator")
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
    def __init__(self,screen, label, variable,):
        self.screen = screen
        self.label = label
        self.variable = customtkinter.StringVar()
        self.placeholdertext = 0

    def slider(self, widgetfrom, widgetto):

        self.slider1 = customtkinter.CTkSlider(self.screen, from_= widgetfrom, to= widgetto)
        self.slider1.pack(padx=20, pady=20)
        self.placeholdertext=self.slider1.get()
        print(self.slider1.get())

    def toggle(self):
        def toggleevent():
            self.togglestate = self.toggle.get()
        self.toggle = customtkinter.CTkSwitch(self.screen, text=self.label, command=toggleevent, onvalue=True, offvalue=False)
        self.toggle.pack(padx=20, pady=60)

    def dropdown(self):
        def dropdownevent(choice):
            self.dropdownchoice = choice
        self.dropdown = customtkinter.CTkOptionMenu(self.screen, values=["test1", "test2", "test3"], command=dropdownevent)
        self.dropdown.set("test1")
        self.dropdown.pack(padx=20, pady=80)

    def button(self):
        def buttonevent():
            print("button pressed")
        self.button = customtkinter.CTkButton(self.screen, text=self.label, command=buttonevent)
        self.button.pack(padx=20, pady=100)

    def textentry(self):
        self.entry =  customtkinter.CTkEntry(self.screen, textvariable= self.variable)
        self.entry.pack(padx=20, pady=40)

test =inputscreen()
testscreen= test.getdisplay()
testvar = "testing"
widgets1 = widgets(testscreen, "test", testvar)
widgets1.slider(0,100)
widgets1.textentry()
widgets1.toggle()
widgets1.dropdown()
widgets1.button()
testscreen.mainloop()
print()