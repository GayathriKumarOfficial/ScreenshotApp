import time
import pyautogui #to use screenshot() fun
import tkinter as tk #to add gui in this app

def screenshot():
    name= int(round(time.time()*1000)) # to generate random numbers for naming the img
    # store the screenshotted pics in the folder 
    name = 'E:\PythonProjects\Screenshot\screenshot_pics/{}.png'.format(name)
    
    time.sleep(5) #wait for 5s
    
    # call the screenshot() fun in pyautogui to take screenshot and save it with the name of the img
    img = pyautogui.screenshot(name)
    ''' img = pyautogui.screenshot("sample.png") -> by our custom name with img format
     one time only store if we run again the image will be over written '''
    
    img.show() # it shows screenshot pics

root = tk.Tk() # to create the main application window 
frame = tk.Frame(root,bg="lightblue") # to create frame inside the root window
frame.pack(pady=20) # add 20pixels above and below the frame

#BUTTON for take screenshots 
button = tk.Button(
    frame,
    text="Take Screenshots", #name for the button
    command = screenshot #our screenshot method 
)
button.pack(side=tk.LEFT) #pack frame to the left

#BUTTON for quitting the application
close=tk.Button(
    frame,
    text ="QUIT" ,
    command =quit # built in quit method
)
close.pack(side=tk.LEFT) #pack frame to the left

root.mainloop() # to run or start the application



