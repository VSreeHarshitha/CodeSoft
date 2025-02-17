import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from JSON file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to JSON file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    email = simpledialog.askstring("Add Contact", "Enter Email (optional):")
    address = simpledialog.askstring("Add Contact", "Enter Address (optional):")

    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        update_listbox()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Warning", "Name and Phone Number are required!")

# View all contacts
def update_listbox():
    contact_listbox.delete(0, tk.END)
    for name, info in contacts.items():
        contact_listbox.insert(tk.END, f"{name} - {info['Phone']}")

# Search contact
def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter Name or Phone:")
    if query:
        for name, info in contacts.items():
            if query in name or query in info["Phone"]:
                messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}")
                return
        messagebox.showwarning("Not Found", "Contact not found!")

# Update contact
def update_contact():
    name = simpledialog.askstring("Update Contact", "Enter Name of Contact to Update:")
    if name in contacts:
        phone = simpledialog.askstring("Update Contact", "Enter New Phone Number:", initialvalue=contacts[name]["Phone"])
        email = simpledialog.askstring("Update Contact", "Enter New Email:", initialvalue=contacts[name]["Email"])
        address = simpledialog.askstring("Update Contact", "Enter New Address:", initialvalue=contacts[name]["Address"])
        
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        update_listbox()
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showwarning("Not Found", "Contact not found!")

# Delete contact
def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter Name of Contact to Delete:")
    if name in contacts:
        del contacts[name]
        save_contacts()
        update_listbox()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showwarning("Not Found", "Contact not found!")

# GUI Setup
app = tk.Tk()
app.title("Contact Book")
app.geometry("400x500")
app.config(bg="#f5f5f5")

contacts = load_contacts()

# Title
title_label = tk.Label(app, text="Contact Book", font=("Arial", 16, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

# Contact Listbox
contact_listbox = tk.Listbox(app, width=50, height=15)
contact_listbox.pack(pady=10)
update_listbox()

# Buttons
btn_frame = tk.Frame(app, bg="#f5f5f5")
btn_frame.pack()

buttons = [
    ("Add Contact", add_contact),
    ("Search Contact", search_contact),
    ("Update Contact", update_contact),
    ("Delete Contact", delete_contact)
]

for text, command in buttons:
    btn = tk.Button(btn_frame, text=text, command=command, width=20, bg="#4CAF50", fg="white")
    btn.pack(pady=5)

# Run the application
app.mainloop()
