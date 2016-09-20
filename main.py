import tkinter as tk

class App(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.pack()
        self.create_main_interface()

    def create_main_interface(self):

        # Timer Labels
        self.timer_label = tk.Label(self)
        self.timer_label['text'] = "Timer:"
        self.timer_label.pack(side='left')

        # Timer/counter
        self.timer = tk.Label(self)
        self.timer['text'] = "00:00"
        self.timer.pack(side='left')

        # Start Button
        self.start_button = tk.Button(self)
        self.start_button['text'] = "Start"
        self.start_button['command'] = self.start_recording
        self.start_button.pack(side='left')

        # Pause Button
        self.pause_button = tk.Button(self)
        self.pause_button['text'] = "Pause"
        self.pause_button['command'] = self.pause_recording
        self.pause_button.pack(side='left')

        # Reset Button
        self.stop_button = tk.Button(self)
        self.stop_button['text'] = "Reset"
        self.stop_button['command'] = self.reset_recording
        self.stop_button.pack(side='left')

    def start_recording(self):
        pass

    def pause_recording(self):
        pass

    def reset_recording(self):
        pass

root = tk.Tk()
app = App(master=root)
app.master.title = "Timely - Time Tracker"
app.mainloop()
