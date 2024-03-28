from tkinter import *
import subprocess
from PIL import Image, ImageTk

def switch_page():
    root.withdraw()  
    subprocess.run(["python", "log-in.py"])

root = Tk()
root.title("HOTEL EZZIRARI") 
root.geometry("1200x675")
root.resizable(False, False)

# Load and set the icon
try:
    root.iconbitmap("hotel.ico")
except:
    pass  # If the icon loading fails, continue without setting the icon

# Load the background image
    background_image = Image.open("HotEZZIRARI.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    
    # Create a canvas and display the image
    canvas = Canvas(root, width=1200, height=675)
    canvas.pack()
    canvas.create_image(0, 0, anchor=NW, image=background_photo)

    
fr1 = Frame(root, bg="black", bd=0)
fr1.place(x=900, y=610, width="210", height=35)
b2 = Button(fr1, text='WELCOME', font="stencil", fg="white", bd=1, bg="#271016", relief=SOLID, cursor='hand2', command=switch_page)
b2.place(x=0, y=0, width=209 , height=33) 

root.mainloop()
