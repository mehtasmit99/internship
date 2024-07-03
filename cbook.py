import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        # Header Label
        header_label = tk.Label(self.root, text="Contact Book", font=('Helvetica', 24, 'bold'), bg="#4285f4", fg="white", pady=10)
        header_label.pack(fill=tk.X)

        # Name Entry
        ttk.Label(self.root, text="Name:", font=('Arial', 14), background="#f0f0f0").pack(pady=5)
        self.name_entry = ttk.Entry(self.root, font=('Arial', 12))
        self.name_entry.pack(pady=5, padx=10, ipadx=10, ipady=5, fill=tk.X)

        # Phone Entry
        ttk.Label(self.root, text="Phone:", font=('Arial', 14), background="#f0f0f0").pack(pady=5)
        self.phone_entry = ttk.Entry(self.root, font=('Arial', 12))
        self.phone_entry.pack(pady=5, padx=10, ipadx=10, ipady=5, fill=tk.X)

        # Add Button
        add_button = ttk.Button(self.root, text="Add Contact", command=self.add_contact,style="TButton" )
        add_button.pack(pady=10, padx=10, ipadx=10, ipady=5, )

        # Contact Listbox
        self.contacts_listbox = tk.Listbox(self.root, font=('Arial', 12), height=10, selectmode=tk.SINGLE, selectbackground="#a6a6a6", background="#f0f0f0")
        self.contacts_listbox.pack(pady=10, padx=10, ipadx=10, ipady=5, fill=tk.X)

        # Delete Button
        delete_button = ttk.Button(self.root, text="Delete Contact", command=self.delete_contact, style="TButton")
        delete_button.pack(pady=10, padx=10, ipadx=10, ipady=5, )

        # Style
        
        style = ttk.Style()
        style.configure("TButton", background="#4285f4", font=('Arial', 12), width=20, foreground="black")
        style.map("TButton", background=[('active', '#3367d6')])

        # Populate Listbox
        self.update_contact_list()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and self.is_valid_phone(phone):
            contact = f"{name} - {phone}"
            self.contacts.append(contact)
            self.update_contact_list()
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid phone number with a maximum of 10 digits.")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()

        if selected_index:
            self.contacts.pop(selected_index[0])
            self.update_contact_list()

    def update_contact_list(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, contact)

    def is_valid_phone(self, phone):
        # Validate that the phone contains only numeric characters and has a maximum of 10 digits
        return phone.isdigit() and len(phone) <= 10

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
