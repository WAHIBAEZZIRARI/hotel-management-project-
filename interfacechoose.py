from tkinter import *
from PIL import Image, ImageTk
import subprocess


class lobby:
    def __init__(self, root):
        self.root = root 
        self.root.title("HOTEL EZZIRARI") 
        self.root.geometry("1200x675")
        self.root.iconbitmap("hotel.ico")
        self.root.resizable(False, False)
        self.background_image = Image.open("bgsign.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = Canvas(root, width=1200, height=900)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=NW, image=self.background_photo)

        self.b2 = Button(self.canvas, text='Reserver', font=('calibri', 20, 'bold'), fg="white", bd=1, bg="black", relief='solid', cursor='hand2',command=switch_page)
        self.b2.place(x=550, y=310)

        self.b3 = Button(self.canvas, text='Voir Ma Reservation', font=('calibri', 20, 'bold'), fg="white", bd=1, bg="black", relief='solid', cursor='hand2' ,command=switch_page2)
        self.b3.place(x=500, y=400)

def switch_page():
    root.withdraw()  # Hide the current window
    subprocess.run(["python", "reservation.py"])

def switch_page2():
    root.withdraw()  # Hide the current window
    subprocess.run(["python", "information.py"])


root = Tk()
app = lobby(root)
root.mainloop()