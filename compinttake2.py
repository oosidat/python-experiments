## A Basic Compound Interest Calculator

import Tkinter

class compintapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        
        ## Title & subtitle labels ---------------------------------------
        titlelbl = Tkinter.Label(self, text="Basic Compound Interest Calculator",
                              anchor="center",fg="white",bg="red")
        titlelbl.grid(column=0,row=0,columnspan=3,sticky='EW')
        
        subtitlelbl = Tkinter.Label(self, text="By Osama Sidat",
                              anchor="center",fg="white",bg="black")
        subtitlelbl.grid(column=0,row=1,columnspan=3,sticky='EW')
        
        ## end of title & subtitle lbls ----------------------------------
        
        ## Input Labels --------------------------------------------------
        
        principallbl = Tkinter.Label(self, text="Principal :",
                              anchor="w",fg="white",bg="blue")
        principallbl.grid(column=0,row=2,columnspan=1,sticky='EW')
        
        intratelbl = Tkinter.Label(self, text="Rate of Interest (Annual) :",
                              anchor="w",fg="white",bg="blue")
        intratelbl.grid(column=0,row=3,columnspan=1,sticky='EW')
        
        timescomplbl = Tkinter.Label(self, text="Number of Times Compounded Per Year :",
                              anchor="w",fg="white",bg="blue")
        timescomplbl.grid(column=0,row=4,columnspan=1,sticky='EW')
        
        yrslbl = Tkinter.Label(self, text="Number of Years :",
                              anchor="w",fg="white",bg="blue")
        yrslbl.grid(column=0,row=5,columnspan=1,sticky='EW')
        
        ## end of input labels ------------------------------------------------
        
        ## Input Boxes --------------------------------------------------------
        principal = Tkinter.Entry(self)
        principal.grid(column=1,row=2, sticky='EW')
        p = principal.get()
        
        intrate = Tkinter.Entry(self)
        intrate.grid(column=1,row=3, sticky='EW')
        
        times = Tkinter.Entry(self)
        times.grid(column=1,row=4, sticky='EW')
        
        yrs = Tkinter.Entry(self)
        yrs.grid(column=1,row=5, sticky='EW')
        
        ## end of input boxes -------------------------------------------------
        
        ## Button
        button = Tkinter.Button(self,text="Calculate",
                                command=self.OnButtonClick)
        button.grid(column=0,row=6,columnspan=3)
        ## end of button
        
        ## Output label
        self.labelVariable = Tkinter.StringVar()
        amt = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="e",fg="red",bg="yellow")
        amt.grid(column=0,row=7,columnspan=3,sticky='EW')
        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)


    def OnButtonClick(self):
        self.labelVariable.set(p)
        
if __name__ == "__main__":
    app = compintapp_tk(None)
    app.title('Basic Compound Interest Calculator')
    app.mainloop()

    
## Notes:
## anchor for title at 'centre'