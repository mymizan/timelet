import tkinter as tk
import pyscreenshot as ImageGrab
import time
import os
import threading
import requests


class App(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.grid()
        self.create_main_interface()
        self.stop_timer = False
        self.last_tracked = (0,0,0)
        self.take_screenshot_interval =  1 # minutes
        self.last_screenshot_taken = 1 # minutes unit
        self.upload_url = 'http://localhost/a.php'

    def create_main_interface(self):

        # Timer Labels
        self.timer_label = tk.Label(self)
        self.timer_label['text'] = "Timer:"
        self.timer_label.grid(row=0,column=0)

        # Timer/counter
        self.timer = tk.Label(self)
        self.timer['text'] = "00:00:00"
        self.timer.grid(row=0,column=1)

        # Start Button
        self.start_button = tk.Button(self)
        self.start_button['text'] = "Start"
        self.start_button['command'] = self.start_recording
        self.start_button.grid(row=1,column=0)

        # Pause Button
        self.pause_button = tk.Button(self)
        self.pause_button['text'] = "Pause"
        self.pause_button['command'] = self.pause_recording
        self.pause_button.grid(row=1,column=1)

        # Reset Button
        self.stop_button = tk.Button(self)
        self.stop_button['text'] = "Reset"
        self.stop_button['command'] = self.reset_recording
        self.stop_button.grid(row=1,column=2)

        # Quit Button
        self.quit_button = tk.Button(self)
        self.quit_button['text'] = "Quit"
        self.quit_button['command'] = root.destroy
        self.quit_button.grid(row=1,column=3)

    def start_recording(self):
        self.stop_timer = False
        while True:
            if self.stop_timer:
                self.take_screenshot
                break

            if self.last_tracked[2] == 59: #increment minutes
                self.last_tracked = (self.last_tracked[0],self.last_tracked[1]+1,0)
            else:
                self.last_tracked = (self.last_tracked[0],self.last_tracked[1],self.last_tracked[2]+1)

            if self.last_tracked[1] == 60: #increment hour
                self.last_tracked = (self.last_tracked[0]+1,0,self.last_tracked[2])
                self.last_screenshot_taken = 1

            self.timer['text'] = '{:02d}:{:02d}:{:02d}'.format(*self.last_tracked)

            #take screenshot
            if self.last_tracked[1] - self.last_screenshot_taken >= self.take_screenshot_interval:
                self.take_screenshot()
                self.last_screenshot_taken = self.last_tracked[1]
            root.update()
            time.sleep(1)

    def pause_recording(self):
        self.stop_timer = True

    def reset_recording(self):
        self.last_tracked = (0,0,0)
        self.timer['text'] = '{:02d}:{:02d}:{:02d}'.format(*self.last_tracked)
        root.update()

    def take_screenshot(self):
        ImageGrab.grab_to_file('tracker_data/' + str(time.time()).replace('.','__') + '.png')
        print("Taking Screehshot: " , self.last_tracked[0] , ' ' , self.last_tracked[1] , ' ' , self.last_tracked[2])
        self.upload_images

    def upload_images(self):
        #read files in images
        #upload each one
        #delete uploaded files
        print("Uploading image started... ")
        for i in os.listdir('tracker_data/'):
            try:
                r = requests.post(self.upload_url, files={i:open(i, 'rb')})
                if r.status_code == 200:
                    print("Uploaded Image: ", i)
                    os.remove('tracker_data/',i)
                else:
                    print("Upload Failed: ", r.status_code)
            except Exception:
                print("Upload Error. HTTP request failed.")

    def record_mouse_activity(self):
        pass

    def record_keystrokes_count(self):
        pass

root = tk.Tk()
app = App(master=root)
app.master.title = "Timely"
app.mainloop()
