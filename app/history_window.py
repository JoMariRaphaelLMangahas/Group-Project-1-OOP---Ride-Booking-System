import tkinter as tk
from tkinter import ttk

class HistoryWindow:
    def __init__(self, root, records):
        self.root = root
        self.records = records
        self.root.title("Booking History")

        self.create_widgets()
        self.display_history()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

        # Define columns with fixed widths
        columns = ("Booking Number", "Status", "Date", "Time", "Pick-up address", "Destination", "Vehicle Type", "Distance", "Cost", "Driver")
        self.treeview = ttk.Treeview(self.frame, columns=columns, show="headings")

        # Configure column headings and set fixed widths
        column_widths = {
            "Booking Number": 120,
            "Status": 100,
            "Date": 100,
            "Time": 100,
            "Pick-up address": 200,
            "Destination": 200,
            "Vehicle Type": 100,
            "Distance": 100,
            "Cost": 100,
            "Driver": 100
        }

        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=column_widths[col], anchor='center')

        # Pack the Treeview widget
        self.treeview.pack(side="left", expand=True, fill="both")

        # Add vertical scrollbar
        yscrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.treeview.yview)
        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.config(yscrollcommand=yscrollbar.set)

        # Add horizontal scrollbar
        xscrollbar = ttk.Scrollbar(self.frame, orient=tk.HORIZONTAL, command=self.treeview.xview)
        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.treeview.config(xscrollcommand=xscrollbar.set)

    def display_history(self):
        for record in self.records:
            if record[1] == "Completed" or record[1] == "Cancelled":
                self.treeview.insert("", "end", values=record)