import subprocess
from tkinter import Tk, Canvas, Label, Entry, Button, messagebox
import mysql.connector
from PIL import Image, ImageTk

class LoginFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title('HOTEL EZZIRARI')
        self.root.geometry("1200x675")
        self.root.resizable(False, False)

        self.background_image = Image.open("bgsign.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = Canvas(root, width=1200, height=900)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor='nw', image=self.background_photo)

        self.label1 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Email :', foreground='white', background='black')
        self.label1.place(x=450, y=270)

        self.en1 = Entry(self.canvas, justify='center', bg="white", fg="black", bd=1, relief='solid', width="25")
        self.en1.place(x=450, y=320, width=300, height=40)

        self.label2 = Label(self.canvas, font=('calibri', 20, 'bold'), text='Password :', foreground='white', background='black')
        self.label2.place(x=450, y=370)

        self.en2 = Entry(self.canvas, justify='center', bg="white", fg="black", bd=1, relief='solid', width="25")
        self.en2.place(x=450, y=420, width=300, height=40)

        self.b1 = Button(self.canvas, text='Submit', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief='solid', cursor='hand2', command=self.submit_form)
        self.b1.place(x=450, y=490, width=300, height=40)

        self.b2 = Button(self.canvas, text='Sign in', font=('calibri', 20, 'bold'), fg="white", bd=1, bg="black", relief='solid', cursor='hand2', command=self.switch_page2)
        self.b2.place(x=450, y=560, width=300, height=40)

    def switch_page2(self):
            root.withdraw()  # Hide the current window
            subprocess.run(["python", "sign-up.py"])
        
    def submit_form(self):
        email = self.en1.get()
        psd = self.en2.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wahiba2004wahiba",
            database="hotel_ezzirari"
        )
        mycursor = mydb.cursor()

        query = "SELECT * FROM client WHERE email = %s AND password = %s"
        mycursor.execute(query, (email, psd))
        user = mycursor.fetchone()

        if user:
            email = self.en1.get()
            sql = "INSERT INTO connexion(email)  VALUES (%s)"
            val = ( email,)
            mycursor.execute(sql, val)
            mydb.commit()
       
            messagebox.showinfo("Success", "Login successful!")
            self.hide_login_page()
            subprocess.run(["python", "interfacechoose.py"])  # Only switch page if login is successful
        else:
            messagebox.showerror("Error", "Invalid email or password!")

        self.en2.delete(0, 'end')  

    def hide_login_page(self):
        self.root.withdraw()

root = Tk()

app = LoginFormApp(root)

root.mainloop()
