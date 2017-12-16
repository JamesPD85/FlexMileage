import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure

LARGE_FONT = ("Verdana",12)

class FlexMileageApp(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        tk.Tk.iconbitmap(self,default="sheet.ico")
        tk.Tk.wm_title(self,"Flex Mileage Tracker")

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label="New", command=None, accelerator="Ctrl+N") # accelerator = hot key
        filemenu.add_command(label="Open", command=None, accelerator="Ctrl+O")
        filemenu.add_command(label="Save", command=None, accelerator="Ctrl+S")
        filemenu.add_command(label="Save As...", command=None, accelerator="Ctrl+Shift+S")
        filemenu.add_command(label="Close", command=quit, accelerator="")

        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=quit, accelerator="Ctrl+Q")
        menubar.add_cascade(label="File",menu=filemenu)

        editmenu = tk.Menu(menubar,tearoff=0)
        editmenu.add_command(label="Undo", command=lambda: messagebox.showinfo("MessageBox","Not supported yet!"), accelerator="Ctrl+Z")
        editmenu.add_command(label="Redo", command=None, accelerator="Ctrl+Y")
        editmenu.add_command(label="Cut", command=None, accelerator="Ctrl+X")
        editmenu.add_command(label="Copy", command=None, accelerator="Ctrl+C")
        editmenu.add_command(label="Paste", command=None, accelerator="Ctrl+V")
        editmenu.add_command(label="Delete", command=None, accelerator="Delete")
        editmenu.add_command(label="Select All", command=None, accelerator="Ctrl+A")
        menubar.add_cascade(label="Edit",menu=editmenu)

        helpmenu = Menu(menubar,tearoff=0)
        helpmenu.add_command(label="Index", command=None)
        helpmenu.add_command(label="About", command=None)
        menubar.add_cascade(label="Help",menu=helpmenu)

        tk.Tk.config(self,menu=menubar)

        self.frames = {}

        for F in (HomePage,History,EnterMileage,LoginPage,Costs):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Home Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self,text="History", command=lambda: controller.show_frame(History))
        button.pack()

        button2 = ttk.Button(self,text="Enter Mileage",command=lambda: controller.show_frame(EnterMileage))
        button2.pack()

        button3 = ttk.Button(self,text="Login",command=lambda: controller.show_frame(LoginPage))
        button3.pack()

        button4 = ttk.Button(self,text="Costs",command=lambda: Costs(Costs.show_graph(self,controller)))
        button4.pack()


class History(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="History", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,text="Home Page",command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = ttk.Button(self,text="Enter Mileage",command=lambda: controller.show_frame(EnterMileage))
        button2.pack()


class EnterMileage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Enter Mileage", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,text="Home Page",command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = ttk.Button(self,text="History",command=lambda: controller.show_frame(History))
        button2.pack()


class LoginPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Login Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,text="Home Page",command=lambda: controller.show_frame(HomePage))
        button1.pack()

        button2 = ttk.Button(self,text="Login",command=lambda: controller.show_frame(HomePage))
        button2.pack()


class Costs(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Cost Graph Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self,text="Fuel Costs",command=lambda: controller.show_frame(LoginPage))
        button1.pack()

        button2 = ttk.Button(self,text="Miles per Gallon Chart",command=lambda: controller.show_frame(LoginPage))
        button2.pack()



    def show_graph(self,controller):

        a = {"daysOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
             "Miles": [20,25,18,23,36]}

        b = a['daysOfWeek']
        c = a['Miles']

        plt.plot(c)
        plt.xticks(range(len(c)),b)
        plt.show()

        f = Figure(figsize=(5,5),dpi=100)
        a = f.add_subplot(111)

        canvas = FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)








app = FlexMileageApp()
app.mainloop()
