from tkinter import *
from threading import *
import datetime
import time
from playsound3 import playsound


root = Tk() #create main window
# root.title("My firt App")
root.geometry("400x200+100+50") #set window size

# Threading 
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        #set alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        time.sleep(1)

        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)

        if current_time == set_alarm_time:
            print("Time to wake up")
            playsound("/Users/mb/Documents/GitHub/pythonRepo/PythonProject/AlarmClock/ahem_x.wav",block = False)

Label(root,text="Alarm Clock", font=("helvetica 20"),fg = "red").pack(pady=10)
Label(root,text="Set Time",font=("helvetica 15")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)

hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)

hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root,text="Set Alarm", font=("Helvetica 15"),command=Threading).pack(pady=20)

#start event loop
root.mainloop()



# lable = tk.Label(root, text ="Hello, Tkinter") #create label widget
# lable.pack(pady=20) #padding for label

# #create button widget
# def on_button_clicked():
#     lable.config(text = "button Clicked!!")

# button = tk.Button(root, text = "Click me!", command=on_button_clicked)
# button.pack()


                 
