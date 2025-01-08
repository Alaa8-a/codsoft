import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Name and phone number are required.")

# Function to update the contact listbox
def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name, details in contacts.items():
        listbox_contacts.insert(tk.END, f"{name} - {details['phone']}")

# Function to clear entry fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Function to search for a contact
def search_contact():
    search_term = entry_search.get()
    listbox_contacts.delete(0, tk.END)
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            listbox_contacts.insert(tk.END, f"{name} - {details['phone']}")

# Function to update a contact
def update_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        if name in contacts:
            contacts[name] = {
                "phone": entry_phone.get(),
                "email": entry_email.get(),
                "address": entry_address.get()
            }
            update_contact_list()
            clear_entries()
        else:
            messagebox.showwarning("Warning", "Contact not found.")
    else:
        messagebox.showwarning("Warning", "No contact selected.")

# Function to delete a contact
def delete_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        if name in contacts:
            del contacts[name]
            update_contact_list()
            clear_entries()
        else:
            messagebox.showwarning("Warning", "Contact not found.")
    else:
        messagebox.showwarning("Warning", "No contact selected.")

# Create the main window
root = tk.Tk()
root.title("Contact Manager")

# Create and place the widgets
tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Phone:").pack(pady=5)
entry_phone = tk.Entry(root)
entry_phone.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

tk.Label(root, text="Address:").pack(pady=5)
entry_address = tk.Entry(root)
entry_address.pack(pady=5)

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

tk.Label(root, text="Search:").pack(pady=5)
entry_search = tk.Entry(root)
entry_search.pack(pady=5)
tk.Button(root, text="Search", command=search_contact).pack(pady=5)

listbox_contacts = tk.Listbox(root, width=50, height=10)
listbox_contacts.pack(pady=10)

# Start the main event loop
root.mainloop()