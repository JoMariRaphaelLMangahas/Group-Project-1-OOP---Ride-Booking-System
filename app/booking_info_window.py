import customtkinter as ctk
import tkinter as tk
import pickle

class BookingInfoWindow(tk.Toplevel):
    def __init__(self, master=None, vehicle_type=""):
        super().__init__(master)
        self.title(f"{vehicle_type} Booking Window")
        self.geometry("500x500")
        self.resizable(False, False)
        self.configure(background="#C8E7F5")
        self.records = self.load_data()

        font2 = ctk.CTkFont(family="Inter", size=20)

        self.booking_window_frame = ctk.CTkFrame(self, width=449, height=434, border_width=2, fg_color="#F6D2E0")
        self.booking_window_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Center the booking window
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def load_data(self):
        try:
            with open("booking_data.dat", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []