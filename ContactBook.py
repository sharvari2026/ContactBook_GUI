import datetime
import tkinter as tk
from tkinter import messagebox

# Dictionary to store Contact details
List = {9881460264: "Sharvari", 8446807392: "Radha", 9822203265: "Rucha"}
loglist = []

root = tk.Tk()
root.title("Phone Dictionary")
root.configure(bg="#7FFF00")

def add_contact():
    phn = int(phone_entry.get())
    name = name_entry.get()
    if len(str(phn)) == 10:
        List[phn] = name
        loglist.append(f"Added {phn} at {datetime.datetime.now()}")
        messagebox.showinfo("Success", "Contact added successfully.")
    else:
        messagebox.showerror("Error", "Invalid mobile number.")

def search_contact():
    mob_no = int(search_entry.get())
    if mob_no in List:
        messagebox.showinfo("Search Result", f"Found: {List[mob_no]}")
        loglist.append(f"Searched {mob_no} at {datetime.datetime.now()}")
    else:
        messagebox.showinfo("Search Result", "Not Found")

def update_contact():
    replace_no = int(replace_entry.get())
    if replace_no in List:
        name = name_update_entry.get()
        List[replace_no] = name
        loglist.append(f"Updated {replace_no} at {datetime.datetime.now()}")
        messagebox.showinfo("Success", "Contact updated successfully.")
    else:
        messagebox.showerror("Error", "This mobile number does not exist.")

def delete_contact():
    del_key = int(delete_entry.get())
    if del_key in List:
        del List[del_key]
        loglist.append(f"Deleted {del_key} at {datetime.datetime.now()}")
        messagebox.showinfo("Success", "Contact deleted successfully.")
    else:
        messagebox.showerror("Error", "This contact number does not exist.")

def display_loglist():
    log_window = tk.Toplevel(root)
    log_window.title("Log List")
    
    scrollbar = tk.Scrollbar(log_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    log_text = tk.Text(log_window, wrap=tk.WORD, yscrollcommand=scrollbar.set,bg="#97FFFF")
    log_text.pack()
    for log in loglist:
        log_text.insert(tk.END, log + "\n")
    scrollbar.config(command=log_text.yview)

def display_contacts():
    contacts_window = tk.Toplevel(root)
    contacts_window.title("Contacts List")
    scrollbar = tk.Scrollbar(contacts_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    contact_text = tk.Text(contacts_window, wrap=tk.WORD, yscrollcommand=scrollbar.set,bg="#97FFFF")
    contact_text.pack()

    for phone, name in List.items():
        contact_text.insert(tk.END, f"Phone: {phone}, Name: {name}\n")

    scrollbar.config(command=contact_text.yview)

def welcome_page():
    def add_contact_page():
        add_contact_window = tk.Toplevel(root)
        add_contact_window.title("Add Contact")

        def add_contact():
            phn = int(phone_entry.get())
            name = name_entry.get()
            if len(str(phn)) == 10:
                List[phn] = name
                loglist.append(f"Added {phn} at {datetime.datetime.now()}")
                messagebox.showinfo("Success", "Contact added successfully.")
            else:
                messagebox.showerror("Error", "Invalid mobile number.")

        name_label = tk.Label(add_contact_window, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(add_contact_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        phone_label = tk.Label(add_contact_window, text="Phone Number:")
        phone_label.grid(row=1, column=0, padx=10, pady=10)
        phone_entry = tk.Entry(add_contact_window)
        phone_entry.grid(row=1, column=1, padx=10, pady=10)

        add_button = tk.Button(add_contact_window, text="Add Contact", command=add_contact)
        add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def search_contact_page():
        search_contact_window = tk.Toplevel(root)
        search_contact_window.title("Search Contact")

        def search_contact():
            mob_no = int(search_entry.get())
            if mob_no in List:
                messagebox.showinfo("Search Result", f"Found: {List[mob_no]}")
                loglist.append(f"Searched {mob_no} at {datetime.datetime.now()}")
            else:
                messagebox.showinfo("Search Result", "Not Found")

        search_label = tk.Label(search_contact_window, text="Enter Phone Number:")
        search_label.grid(row=0, column=0, padx=10, pady=10)
        search_entry = tk.Entry(search_contact_window)
        search_entry.grid(row=0, column=1, padx=10, pady=10)

        search_button = tk.Button(search_contact_window, text="Search", command=search_contact)
        search_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def update_contact_page():
        update_contact_window = tk.Toplevel(root)
        update_contact_window.title("Update Contact")

        def update_contact():
            replace_no = int(replace_entry.get())
            if replace_no in List:
                name = name_update_entry.get()
                List[replace_no] = name
                loglist.append(f"Updated {replace_no} at {datetime.datetime.now()}")
                messagebox.showinfo("Success", "Contact updated successfully.")
            else:
                messagebox.showerror("Error", "This mobile number does not exist.")

        replace_label = tk.Label(update_contact_window, text="Enter Phone Number to Update:")
        replace_label.grid(row=0, column=0, padx=10, pady=10)
        replace_entry = tk.Entry(update_contact_window)
        replace_entry.grid(row=0, column=1, padx=10, pady=10)

        name_update_label = tk.Label(update_contact_window, text="New Name:")
        name_update_label.grid(row=1, column=0, padx=10, pady=10)
        name_update_entry = tk.Entry(update_contact_window)
        name_update_entry.grid(row=1, column=1, padx=10, pady=10)

        update_button = tk.Button(update_contact_window, text="Update Contact", command=update_contact)
        update_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def delete_contact_page():
        delete_contact_window = tk.Toplevel(root)
        delete_contact_window.title("Delete Contact")

        def delete_contact():
            del_key = int(delete_entry.get())
            if del_key in List:
                del List[del_key]
                loglist.append(f"Deleted {del_key} at {datetime.datetime.now()}")
                messagebox.showinfo("Success", "Contact deleted successfully.")
            else:
                messagebox.showerror("Error", "This contact number does not exist.")

        delete_label = tk.Label(delete_contact_window, text="Enter Phone Number to Delete:")
        delete_label.grid(row=0, column=0, padx=10, pady=10)
        delete_entry = tk.Entry(delete_contact_window)
        delete_entry.grid(row=0, column=1, padx=10, pady=10)

        delete_button = tk.Button(delete_contact_window, text="Delete Contact", command=delete_contact)
        delete_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    

    welcome_label = tk.Label(root, text="Welcome to Phone Dictionary", font=("Helvetica", 20))
    welcome_label.pack(pady=20)
    options_label = tk.Label(root, text="Select an option:", font=("Helvetica", 16))
    options_label.pack()

    options_frame = tk.Frame(root)
    options_frame.pack(pady=10)

    add_contact_button = tk.Button(options_frame, text="Add a Contact", command=add_contact_page)
    add_contact_button.grid(row=0, column=0, padx=10)

    search_contact_button = tk.Button(options_frame, text="Search a Contact", command=search_contact_page)
    search_contact_button.grid(row=0, column=1, padx=10)

    update_contact_button = tk.Button(options_frame, text="Update a Contact", command=update_contact_page)
    update_contact_button.grid(row=0, column=2, padx=10)

    delete_contact_button = tk.Button(options_frame, text="Delete a Contact", command=delete_contact_page)
    delete_contact_button.grid(row=1, column=0, padx=10)

    display_loglist_button = tk.Button(options_frame, text="Display Loglist", command=display_loglist)
    display_loglist_button.grid(row=1, column=1, padx=10)

    display_contacts_button = tk.Button(options_frame, text="Display all contacts", command=display_contacts)
    display_contacts_button.grid(row=1, column=2, padx=10)

    exit_button = tk.Button(options_frame, text="Exit", command=root.destroy)
    exit_button.grid(row=2, column=1, pady=10)

    root.mainloop()

welcome_page()
