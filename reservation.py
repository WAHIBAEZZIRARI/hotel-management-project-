import tkinter as tk
from tkinter import messagebox, Radiobutton, Checkbutton, Entry, Button, IntVar
import mysql.connector
from PIL import Image, ImageTk
from datetime import datetime
import subprocess

class FirstInterface:
    def __init__(self, root):
        self.root = root
        self.root.title('HOTEL EZZIRARI')
        self.root.geometry("1200x900")
        self.root.resizable(False, False)

        self.background_image = Image.open("bgsign.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = tk.Canvas(root, width=1200, height=900)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor='nw', image=self.background_photo)

        self.label = tk.Label(self.canvas, font=('calibri', 20, 'bold'), text='Your Email :', foreground='white', background='black')
        self.label.place(x=350, y=230)

        self.en = tk.Entry(self.canvas, justify='center', bg="white", fg="black", bd=1, relief='solid', width="25")
        self.en.place(x=600, y=230, width=300, height=40)

        self.label1 = tk.Label(self.canvas, font=('calibri', 20, 'bold'), text='Nombre de nuit :', foreground='white', background='black')
        self.label1.place(x=350, y=280)

        self.en1 = tk.Entry(self.canvas, justify='center', bg="white", fg="black", bd=1, relief='solid', width="25")
        self.en1.place(x=600, y=280, width=300, height=40)

        self.label2 = tk.Label(self.canvas, font=('calibri', 20, 'bold'), text='Room :', foreground='white', background='black')
        self.label2.place(x=350, y=320)

        self.radio_var = tk.StringVar() 
        self.radio_var.set("Economic")  
        self.radio_button1 = Radiobutton(self.canvas, text="Economic", variable=self.radio_var, value="Economic", command=self.update_price)
        self.radio_button2 = Radiobutton(self.canvas, text="Premium", variable=self.radio_var, value="Premium", command=self.update_price)
        self.radio_button3 = Radiobutton(self.canvas, text="Businesses", variable=self.radio_var, value="Businesses", command=self.update_price)

        self.radio_button1.place(x=450, y=370)
        self.radio_button2.place(x=550, y=370)
        self.radio_button3.place(x=650, y=370)

        self.label3 = tk.Label(self.canvas, font=('calibri', 20, 'bold'), text='Meals :', foreground='white', background='black')
        self.label3.place(x=350, y=420)

        self.checkbox_vars_meals = [IntVar() for _ in range(3)]
        self.checkbox_vars_meals[1].set(1)  # hna 3etina wahed l default value l dok lmakla 

        self.checkbox1 = Checkbutton(self.canvas, text="Breakfast (+$20)", variable=self.checkbox_vars_meals[0], onvalue=20, offvalue=0, command=self.update_price)
        self.checkbox2 = Checkbutton(self.canvas, text="Lunch (+$30)", variable=self.checkbox_vars_meals[1], onvalue=30, offvalue=0, command=self.update_price)
        self.checkbox3 = Checkbutton(self.canvas, text="Dinner (+$30)", variable=self.checkbox_vars_meals[2], onvalue=30, offvalue=0, command=self.update_price)

        self.checkbox1.place(x=450, y=470)
        self.checkbox2.place(x=570, y=470)
        self.checkbox3.place(x=675, y=470)

        self.label4 = tk.Label(self.canvas, font=('calibri', 20, 'bold'), text='Activities :', foreground='white', background='black')
        self.label4.place(x=350, y=520)

        self.checkbox_vars_activities = [IntVar() for _ in range(3)]
        self.checkbox_vars_activities[0].set(1)  # Setting default value for Gym

        self.checkbox4 = Checkbutton(self.canvas, text="Gym (+$20)", variable=self.checkbox_vars_activities[0], onvalue=20, offvalue=0, command=self.update_price)
        self.checkbox5 = Checkbutton(self.canvas, text="Yoga (+$15)", variable=self.checkbox_vars_activities[1], onvalue=15, offvalue=0, command=self.update_price)
        self.checkbox6 = Checkbutton(self.canvas, text="Piscine (+$20)", variable=self.checkbox_vars_activities[2], onvalue=20, offvalue=0, command=self.update_price)

        self.checkbox4.place(x=450, y=570)
        self.checkbox5.place(x=550, y=570)
        self.checkbox6.place(x=650, y=570)

        self.label5 = tk.Label(self.canvas, font=('calibri', 20, 'bold'), text='Booking date (DD/MM/YYYY):', foreground='white', background='black')
        self.label5.place(x=350, y=620)

        self.en2 = Entry(self.canvas, justify='center', bg="white", fg="black", bd=1, relief='solid', width="25")
        self.en2.place(x=450, y=670, width=300, height=40)

        self.b1 = Button(self.canvas, text='Confirmer', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief='solid', cursor='hand2', command=self.submit_form)
        self.b1.place(x=450, y=740, width=300, height=40)

        self.total_price_label = tk.Label(self.canvas, font=('calibri', 20), text="Total Price: $0", foreground='white', background='black')
        self.total_price_label.place(x=550, y=160)

        self.b2 = Button(self.canvas, text='Back to Menu', font=('calibri', 20, 'bold'), fg="black", bd=1, bg="white", relief='solid', cursor='hand2', command=self.switch_page2)
        self.b2.place(x=450, y=800, width=300, height=40)


        # hna connectina database
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wahiba2004wahiba",
            database="hotel_ezzirari"
        )
        self.cursor = self.conn.cursor()

    def update_price(self):
        total_price = 0
        selected_room_price = 0
        selected_meals_price = 0
        selected_activities_price = 0
        email = ""

        # kan7sebo taman dial les room li 3endna 
        if self.radio_var.get() == "Economic":
            selected_room_price = 100
        elif self.radio_var.get() == "Premium":
            selected_room_price = 250
        elif self.radio_var.get() == "Businesses":
            selected_room_price = 450

        # kan7esbo taman dial les makla
        selected_meals_price = sum(var.get() for var in self.checkbox_vars_meals)

        # kan7esdbo taman dial dok les supliment li kaynin 
        selected_activities_price = sum(var.get() for var in self.checkbox_vars_activities)

        total_price = (selected_room_price + selected_meals_price + selected_activities_price) *  int(self.en1.get())

        self.total_price_label.config(text=f"Total Price: ${total_price}")

    def submit_form(self):

        email = self.en.get()  # Get the email entered by the user

        # Check if the email exists in the client table
        self.cursor.execute("SELECT COUNT(*) FROM client WHERE email = %s", (email,))
        result = self.cursor.fetchone()

        if result[0] == 0:  # If the count is zero, the email doesn't exist
            messagebox.showerror("Error", "EMAIL DOESN'T EXIST")
            return
        
        nombre_nuit = int(self.en1.get())  # Get the number of nights
        selected_room = self.radio_var.get()  # Get the selected room
        selected_meals_price = sum(var.get() for var in self.checkbox_vars_meals)  # Get the total price for meals
        selected_activities_price = sum(var.get() for var in self.checkbox_vars_activities)  # Get the total price for activities
        booking_date = datetime.strptime(self.en2.get(), "%d/%m/%Y").strftime("%Y-%m-%d")  # Get the booking date and format it
        email = self.en.get()  # Get the email entered by the user

        total_price = self.total_price_label.cget('text').split('$')[1]  # Get the total price from the label

        try:
            # Insert the user selections into the database
            self.cursor.execute("INSERT INTO user_selections (nombre_de_nuit, room, meal, activity, booking_date, total_price, email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                (nombre_nuit, selected_room, selected_meals_price, selected_activities_price, booking_date, total_price, email))
            self.conn.commit()  # Commit the transaction
            messagebox.showinfo("Success", "Selections saved successfully!")
        except mysql.connector.Error as e:
            if e.errno == 1265:  # Data Truncated for Column
                messagebox.showerror("Error", "Data too long for one of the columns. Please review your input.")
            else:
                messagebox.showerror("Error", f"Error occurred: {e}")


    def switch_page2(self):
        root.withdraw()  # Hide the current window
        subprocess.run(["python", "interfacechoose.py"])

root = tk.Tk()
app = FirstInterface(root)
root.mainloop()
