import tkinter as tk
from tkinter import PhotoImage, messagebox

class AuthWindow(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.header_frame = tk.Frame(self, bg="#F6D2E0", height=60)
        self.header_frame.pack(fill=tk.X)

        self.header_label = tk.Label(self.header_frame, text="Z O O M E R S", font=("Candara", 25, "bold", "italic" ), fg="#000000", bg="#F6D2E0")
        self.header_label.pack(pady=10)

        self.exit_button = tk.Button(self.header_frame, text="X", font=("Helvetica", 13), bg="#C8E7F5", width=4, highlightthickness=3, command=self.master.destroy)
        self.exit_button.place(relx=0.990, rely=0.24, anchor='ne')

        self.content_frame = tk.Frame(self, bg="#C8E7F5")
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        self.center_frame = tk.Frame(self.content_frame, bg="#C8E7F5")
        self.center_frame.place(relwidth=1, relheight=0.8, rely=0.1)

        self.img = PhotoImage(file='assets/booking_front.png')
        self.image_label = tk.Label(self.center_frame, image=self.img, bg="#C8E7F5")
        self.image_label.place(relx=0.08, rely=0.1, relwidth=0.4, relheight=0.8)

        self.form_frame = tk.Frame(self.center_frame, bg="#C8E7F5")
        self.form_frame.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.8)

        self.welcome_label = tk.Label(self.form_frame, text="Hello, Co-ZOOMER!", font=("Candara", 35), bg="#C8E7F5")
        self.welcome_label.place(relx=0.55, rely=0.05, anchor='n')

        self.add_bookings_label = tk.Label(self.form_frame, text="Add your bookings now!", font=("Lucida Console", 12,), bg="#C8E7F5")
        self.add_bookings_label.place(relx=0.55, rely=0.2, anchor='n')

        self.username_label = tk.Label(self.form_frame, text="Username:", font=("Lucida Console", 12), bg="#C8E7F5")
        self.username_label.place(relx=0.3, rely=0.45, anchor='e')
        self.username_entry = tk.Entry(self.form_frame, font=("Lucida Console", 12), bg="#F6D2E0")
        self.username_entry.place(relx=0.32, rely=0.45, anchor='w', relwidth=0.6)

        self.password_label = tk.Label(self.form_frame, text="Password:", font=("Lucida Console", 12), bg="#C8E7F5")
        self.password_label.place(relx=0.3, rely=0.55, anchor='e')
        self.password_entry = tk.Entry(self.form_frame, font=("Lucida Console", 12), bg="#F6D2E0", show="*")
        self.password_entry.place(relx=0.32, rely=0.55, anchor='w', relwidth=0.6)

        self.login_button = tk.Button(self.form_frame, text="Login", font=("Lucida Console", 12), bg="#F6D2E0", width=10, highlightthickness=0, command=self.login)
        self.login_button.place(relx=0.5, rely=0.65, anchor='n')

        self.signup_button = tk.Button(self.form_frame, text="Sign Up", font=("Lucida Console", 12), bg="#F6D2E0", width=10, highlightthickness=0)
        self.signup_button.place(relx=0.5, rely=0.75, anchor='n')

        self.footer_frame = tk.Frame(self, bg="#F6D2E0", height=50)
        self.footer_frame.pack(fill=tk.X)

        self.footer_label = tk.Label(self.footer_frame, text="© 2024 RIDE BOOKING SYSTEM INC.", font=("Lucida Console", 10), bg="#F6D2E0")
        self.footer_label.pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ZOOMERS")
    root.attributes("-fullscreen", True)
    root.configure(bg="#C8E7F5")
    app = AuthWindow(root)
    app.pack(expand=True, fill='both')
    root.mainloop()
