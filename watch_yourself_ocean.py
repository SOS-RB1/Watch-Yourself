from pygame import mixer
from tkinter import *
from tkinter import ttk, messagebox

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.pack(anchor = CENTER)
        self.createWidgets()
        self._alarm_id = None
        self._paused = False
        self._STARTtime = 1680
    def createWidgets(self):
        self.timerVariable = StringVar()
        self.timerVariable.set(None)      
        self.timerLabel = Label(self, bg = "#595959", fg = "#35E9B0", font = ("Digital Dismay", 23), text = "28:00")
        self.timerLabel.pack(padx = 8, side = LEFT)

        self.firstButtonFrame = Frame(self, bg = "#595959")
        self.sevenButton = Radiobutton(self.firstButtonFrame, activebackground = "#4d4d4d", activeforeground = "#35E9B0", bg = "#666666", fg = "#35E9B0", indicatoron = 0, font = ("Arial", 7, "bold"), selectcolor = "#4d4d4d", text = "7", value = "7", width = "5", variable = self.timerVariable, command = self.STARTClock)
        self.sevenButton.pack(side = LEFT)
        self.fourteenkButton = Radiobutton(self.firstButtonFrame, activebackground = "#4d4d4d", activeforeground = "#35E9B0", bg = "#666666", fg = "#35E9B0", indicatoron = 0, font = ("Arial", 7, "bold"), selectcolor = "#4d4d4d", text = "14", value = "14", width = "5", variable = self.timerVariable, command = self.STARTClock)
        self.fourteenkButton.pack(side = LEFT)
        self.twentyoneButton = Radiobutton(self.firstButtonFrame, activebackground = "#4d4d4d", activeforeground = "#35E9B0", bg = "#666666", fg = "#35E9B0", indicatoron = 0, font = ("Arial", 7, "bold"), selectcolor = "#4d4d4d", text = "21", value = "21", width = "5", variable = self.timerVariable, command = self.STARTClock)
        self.twentyoneButton.pack(side = LEFT)
        self.firstButtonFrame.pack(side = TOP)

        self.secondButtonFrame = Frame(self, bg = "#595959")
        self.STARTButton = Button(self.secondButtonFrame, activebackground = "#4d4d4d", activeforeground = "#35E9B0", bg = "#666666", fg = "#35E9B0", font = ("Arial", 7, "bold"), text = "START", width = "5", command = self.STARTTime)
        self.STARTButton.pack(side = LEFT)
        self.STOPButton = Button(self.secondButtonFrame, activebackground = "#4d4d4d", activeforeground = "#35E9B0", bg = "#666666", fg = "#35E9B0", font = ("Arial", 7, "bold"), text = "STOP", width = "5", command = self.STOPTime)
        self.STOPButton.pack(side = LEFT)
        self.RESETButton = Button(self.secondButtonFrame, activebackground = "#4d4d4d", activeforeground = "#35E9B0", bg = "#666666", fg = "#35E9B0", font = ("Arial", 7, "bold"), text = "RESET", width = "5", command = self.RESETTime)
        self.RESETButton.pack(side = LEFT)
        self.secondButtonFrame.pack(side = TOP)

    def STARTClock(self):
        timerToSTART = self.timerVariable.get()
        if timerToSTART == "7":
            if self._alarm_id is not None:
                self.master.after_cancel(self._alarm_id)
            self._paused = False
            self.countdown(420)
        elif timerToSTART == "14":
            if self._alarm_id is not None:
                self.master.after_cancel(self._alarm_id)
            self._paused = False
            self.countdown(840)
        elif timerToSTART == "21":
            if self._alarm_id is not None:
                self.master.after_cancel(self._alarm_id)
            self._paused = False
            self.countdown(1260)
    def STARTTime(self):
        self._paused = False
        if self._alarm_id is None:
            self.countdown(self._STARTtime)
    def STOPTime(self):
        if self._alarm_id is not None:
            self._paused = True
    def RESETTime(self):
        self.master.after_cancel(self._alarm_id)
        self._alarm_id = None
        self._paused = False
        self.countdown(self._STARTtime)
        self._paused = True
    def countdown(self, timeInSeconds, START = True):
        if timeInSeconds >= 0:
            if START:
                self._STARTtime = timeInSeconds
            if self._paused:
                self._alarm_id = self.master.after(1000, self.countdown, timeInSeconds, False)
            else:
                mins, secs = divmod(timeInSeconds, 60)
                timeformat = "{0:02d}:{1:02d}".format(mins, secs)
                app.timerLabel.configure(text = timeformat)
                self._alarm_id = self.master.after(1000, self.countdown, timeInSeconds - 1, False)
        else:
            mixer.init()
            recording = mixer.Sound("bell.wav")
            recording.play()
            messagebox.showwarning("Watch yourself", "Easy man, slow down")
        
if __name__ == "__main__":
    root = Tk()
    root.title("Timer")
    root.resizable(0, 0)
    app=Application(root)
    app.configure(background = "#595959")
    root.mainloop()