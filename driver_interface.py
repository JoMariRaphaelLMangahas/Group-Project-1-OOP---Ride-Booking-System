import tkinter as tk
from tkinter import ttk

class DriverInterface:
    def __init__(self, root, choose_driver_callback):
        self.root = root
        self.root.title("Driver Interface")

        self.choose_driver_callback = choose_driver_callback

        self.create_widgets()
        self.populate_drivers()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

        self.treeview = ttk.Treeview(self.frame, columns=("Driver ID", "Name", "Rating"), show="headings")
        self.treeview.heading("Driver ID", text="Driver ID")
        self.treeview.heading("Name", text="Name")
        self.treeview.heading("Rating", text="Rating")
        self.treeview.pack(side="left", expand=True, fill="both")

        # Add vertical scrollbar
        yscrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.treeview.yview)
        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.treeview.config(yscrollcommand=yscrollbar.set)

        # Add "Choose" button
        choose_button = tk.Button(self.root, text="Choose", command=self.choose_driver)
        choose_button.pack(pady=5)

    def populate_drivers(self):
        # Dummy data for demonstration
        for i in range(1, 101):
            driver_id = f"Driver {i:03}"
            driver_name = f"Driver Name {i}"
            driver_rating = f"4.{i % 10}"
            self.treeview.insert("", "end", values=(driver_id, driver_name, driver_rating))

    def choose_driver(self):
        selected_item = self.treeview.selection()
        if selected_item:
            index = self.treeview.index(selected_item)
            driver_id = self.treeview.item(selected_item, "values")[0]
            self.choose_driver_callback(driver_id)
            self.root.destroy()
        else:
            tk.messagebox.showwarning("No Selection", "Please select a driver.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DriverInterface(root, choose_driver_callback=lambda driver_id: print(driver_id))
    root.mainloop()