import Tkinter
import passwords
import os
import subprocess

class simpleapp_tk(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        # Label for Tx IP Address
        self.TxLabelVariable = Tkinter.StringVar()
        self.TxLabelVariable.set(u"Tx IP Address:")
        self.TxLabel = Tkinter.Label(self, textvariable=self.TxLabelVariable,
                                        anchor="w",fg="white",bg="blue")
        self.TxLabel.grid(column=0,row=0,columnspan=1,sticky="EW")

        # Entry field for Tx IP Address
        self.TxVariable = Tkinter.StringVar()
        self.TxVariable.set(u"IP Address")
        self.Tx = Tkinter.Entry(self, textvariable=self.TxVariable)
        self.Tx.grid(column=0,row=1,sticky="EW")

        # Label for Rx IP Address
        self.RxLabelVariable = Tkinter.StringVar()
        self.RxLabelVariable.set(u"Rx IP Address:")
        self.RxLabel = Tkinter.Label(self, textvariable=self.RxLabelVariable,
                                        anchor="w",fg="white",bg="blue")
        self.RxLabel.grid(column=0,row=2,columnspan=1,sticky="EW")

        # Entry field for Rx IP Address
        self.RxVariable = Tkinter.StringVar()
        self.RxVariable.set(u"IP Address")
        self.Rx = Tkinter.Entry(self,textvariable=self.RxVariable)
        self.Rx.grid(column=0,row=4,sticky="EW")

        # Label for local file to send
        self.FileLabelVariable = Tkinter.StringVar()
        self.FileLabelVariable.set(u"Enter local file to send:")
        self.FileLabel = Tkinter.Label(self,textvariable=self.FileLabelVariable,
                                        anchor="w",fg="white",bg="blue")
        self.FileLabel.grid(column=0,row=5,sticky="EW")

        # Entry field for local file
        self.FileVariable = Tkinter.StringVar()
        self.FileVariable.set(u"File Name")
        self.File = Tkinter.Entry(self,textvariable=self.FileVariable)
        self.File.grid(column=0,row=6,sticky="EW")

        # Button to initialize System
        self.CommandButton = Tkinter.Button(self,text=u"Transfer File",
                                            command=self.CommandButtonClick)
        self.CommandButton.grid(column=0,row=7)

        # Textbox for output to user
        self.Output = Tkinter.Text(self)
        self.Output.grid(column=0,row=8,columnspan=1,sticky="EW")

        # Just make the window behave nicer.
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()
        self.geometry(self.geometry())
        self.Output.insert(Tkinter.END, "==> GUI Initiated.\n")
        self.Tx.focus_set()
        self.Tx.selection_range(0, Tkinter.END)

    def CommandButtonClick(self):
        self.Output.insert(Tkinter.END,"Starting File Transfer System:\n")

        # Copy the local file to the Tx RPI
        self.Output.insert(Tkinter.END,"1.) Copying <"
                            + self.FileVariable.get() + "> to <"
                            + self.TxVariable.get() + ">...")
        #os.system("sshpass -p \"" + passwords.TxPassword + "\" scp " +
        #            self.FileVariable.get() + " pi@"
        #            + self.TxVariable.get() + ":~/")
        self.Output.insert(Tkinter.END, "DONE.\n")

        # Start the Rx side
        print("sshpass -p " + str(passwords.RxPassword) + " ssh "
                    + "pi@" + str(self.RxVariable.get()) +
                    " \"/~/sat-comms/src/basicsystem/basicrecv\"")
        os.system("sshpass -p " + str(passwords.RxPassword) + " ssh "
                    + "pi@" + str(self.RxVariable.get()) +
                    " \"/~/sat-comms/src/basicsystem/basicrecv\"")

def main():
    app = simpleapp_tk(None)
    app.title("Sat-Comms Remote Command System")
    app.mainloop()

if __name__ == "__main__":
    main()
