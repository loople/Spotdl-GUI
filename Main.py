import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_880=tk.Button(root)
        GButton_880["activebackground"] = "#008500"
        GButton_880["activeforeground"] = "#ffffff"
        GButton_880["bg"] = "#008000"
        ft = tkFont.Font(family='Times',size=10)
        GButton_880["font"] = ft
        GButton_880["fg"] = "#ffffff"
        GButton_880["justify"] = "center"
        GButton_880["text"] = "Button"
        GButton_880["relief"] = "flat"
        GButton_880.place(x=230,y=260,width=127,height=50)
        GButton_880["command"] = self.GButton_880_command

        GLineEdit_943=tk.Entry(root)
        GLineEdit_943["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_943["font"] = ft
        GLineEdit_943["fg"] = "#333333"
        GLineEdit_943["justify"] = "center"
        GLineEdit_943["text"] = "Enter the link"
        GLineEdit_943.place(x=50,y=180,width=508,height=59)

        GLabel_977=tk.Label(root)
        ft = tkFont.Font(family='Times',size=52)
        GLabel_977["font"] = ft
        GLabel_977["fg"] = "#333333"
        GLabel_977["justify"] = "center"
        GLabel_977["text"] = "Spotdl GUI"
        GLabel_977.place(x=90,y=70,width=403,height=65)

    def GButton_880_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
