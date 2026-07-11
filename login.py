import tkinter as tk
from tkinter import messagebox

# Demo users
users = {
    "admin": "password123",
    "user": "userpass"
}

# Login Function
def login():
    username = entry_username.get().strip()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror(
            "Error",
            "Please enter username and password"
        )
        return

    if username in users and users[username] == password:
        messagebox.showinfo(
            "Login",
            "Login Successful!"
        )

        window.withdraw()  # Hide login window
        open_dashboard()

    else:
        messagebox.showerror(
            "Error",
            "Invalid username or password"
        )


# Dashboard Function
def open_dashboard():

    dashboard = tk.Toplevel(window)
    dashboard.title("IntelliPark Dashboard")
    dashboard.geometry("400x350")

    tk.Label(
        dashboard,
        text="IntelliPark Dashboard",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(
        dashboard,
        text="Parking Slot Status",
        font=("Arial", 12, "bold")
    ).pack(pady=5)

    slots = {
        "A1": "Occupied",
        "A2": "Vacant",
        "A3": "Occupied",
        "A4": "Vacant",
        "B1": "Vacant",
        "B2": "Occupied"
    }

    for slot, status in slots.items():

        color = "green" if status == "Vacant" else "red"

        tk.Label(
            dashboard,
            text=f"{slot}: {status}",
            fg=color,
            font=("Arial", 10)
        ).pack()

    def logout():
        dashboard.destroy()
        window.deiconify()

    tk.Button(
        dashboard,
        text="Logout",
        command=logout,
        bg="lightblue"
    ).pack(pady=15)


# Main Window
window = tk.Tk()
window.title("IntelliPark Login")
window.geometry("300x250")

tk.Label(
    window,
    text="IntelliPark Login",
    font=("Arial", 14, "bold")
).pack(pady=10)

label_username = tk.Label(
    window,
    text="Username:"
)
label_username.pack(pady=5)

entry_username = tk.Entry(window)
entry_username.pack(pady=5)

label_password = tk.Label(
    window,
    text="Password:"
)
label_password.pack(pady=5)

entry_password = tk.Entry(
    window,
    show="*",
    width=25
)
entry_password.pack(pady=5)

login_button = tk.Button(
    window,
    text="Login",
    command=login,
    width=15
)
login_button.pack(pady=15)

window.mainloop()

