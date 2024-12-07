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
        pass
    def dropdown(self):
        pass
    def button(self):
        pass
    def textentry(self):
        self.entry =  customtkinter.CTkEntry(self.screen, textvariable= self.variable)
        self.entry.pack(padx=20, pady=40)
test =inputscreen()
testscreen= test.getdisplay()
testvar = "testing"
widgets1 = widgets(testscreen, "test", testvar)
widgets1.slider(0,100)
widgets1.textentry()
testscreen.mainloop()
print()