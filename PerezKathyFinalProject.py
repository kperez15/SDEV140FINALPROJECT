import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from tkcalendar import Calendar

class AleBeautyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ale Beauty")

        # Set background color to pink
        self.root.configure(bg="#FFC0CB")

        # Set title color to pink
        title_style = ttk.Style(root)
        title_style.configure("TLabel", foreground="#FFC0CB")  # Set the title label's foreground color

        # Variables to store customer information
        self.customer_name = tk.StringVar()
        self.service_type = tk.StringVar()
        self.additional_notes = tk.StringVar()

        # List to store booked appointments
        self.appointments = []

        # Label and entry for customer name
        tk.Label(root, text="Client Name:", bg="#FFC0CB").grid(row=0, column=0, pady=5)
        tk.Entry(root, textvariable=self.customer_name).grid(row=0, column=1, pady=5)

        # Label and dropdown for service type
        tk.Label(root, text="Select Service Type:", bg="#FFC0CB").grid(row=1, column=0, pady=5)
        services = ["Nails", "Facial", "Massage", "Lashes", "Tooth Jems", "Waxing"]
        service_dropdown = tk.OptionMenu(root, self.service_type, *services, command=self.show_service_details)
        service_dropdown.grid(row=1, column=1, pady=5)

        # Calendar for appointment date selection
        tk.Label(root, text="Select Date:", bg="#FFC0CB").grid(row=2, column=0, pady=5)

        # Customize the style of the calendar
        style = ttk.Style(root)
        style.theme_use('clam')  # Use the 'clam' theme for ttk widgets

        style.configure("TButton", background="#FFC0CB", foreground="black")  # Pink background, black text
        style.configure("TLabel", background="#FFC0CB", foreground="black")  # Pink background, black text
        style.configure("Calendar.TButton", background="white", foreground="black")  # White background, black text
        style.map("Calendar.TButton",
                  background=[('selected', '#FFC0CB')],  # Pink background for selected date
                  foreground=[('selected', 'black')])  # Black text for selected date

        self.cal = Calendar(root, selectmode='day', year=2024, month=1, day=1, style="Calendar.TButton")
        self.cal.grid(row=2, column=1, pady=5)

        # Text area for additional notes
        tk.Label(root, text="Additional Notes:", bg="#FFC0CB").grid(row=3, column=0, pady=5)
        tk.Entry(root, textvariable=self.additional_notes).grid(row=3, column=1, pady=5)

        # Button to book an appointment
        tk.Button(root, text="Book Appointment", command=self.book_appointment, bg="#FF69B4").grid(row=4, column=0, columnspan=2, pady=10)

        # Button to open the Appointments Window
        tk.Button(root, text="View Appointments", command=self.open_appointments_window, bg="#FF69B4").grid(row=5, column=0, columnspan=2, pady=10)

        # Exit button
        tk.Button(root, text="Exit", command=root.destroy, bg="#FF69B4").grid(row=6, column=0, columnspan=2, pady=10)

    def show_service_details(self, selected_service):
        if selected_service == "Nails":
            self.show_nails_images(selected_service)
        elif selected_service == "Waxing":
            self.show_waxing_details()

    def show_waxing_details(self):
        # Create a new window for waxing details
        waxing_window = Toplevel(self.root)
        waxing_window.title("Waxing Details")

        # Set background color to pink
        waxing_window.configure(bg="#FFC0CB")

        # Label and entry for waxing details
        tk.Label(waxing_window, text="Enter Area to Wax:").pack(pady=10)
        waxing_entry = tk.Entry(waxing_window)
        waxing_entry.pack(pady=10)

        # Button to confirm and close the window
        tk.Button(waxing_window, text="Confirm", command=waxing_window.destroy).pack(pady=10)

    def show_nails_images(self, selected_service):
        # Create a new window for displaying images
        images_window = Toplevel(self.root)
        images_window.title(f"{selected_service} Images")

        # Set background color to pink
        images_window.configure(bg="#FFC0CB")

        # Example: Display some image widgets
        image1 = tk.PhotoImage(file="Nailsimages/xl.png")
        image2 = tk.PhotoImage(file="Nailsimages/short4.png")
        image3 = tk.PhotoImage(file="Nailsimages/short2.png")

        tk.Label(images_window, image=image1, bg="#FFC0CB").pack(pady=5)
        tk.Label(images_window, image=image2, bg="#FFC0CB").pack(pady=5)

    def book_appointment(self):
        # Retrieve customer name, selected date, service type, and additional notes
        customer_name = self.customer_name.get()
        selected_date = self.cal.get_date()
        selected_service = self.service_type.get()
        notes = self.additional_notes.get()

        # Validate input
        if not customer_name or not selected_date or not selected_service:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        # Add the appointment to the list
        appointment_info = f"{customer_name} - {selected_date} - {selected_service}\nNotes: {notes}"
        self.appointments.append(appointment_info)

        # Display confirmation message
        confirmation_message = f"Appointment booked for {customer_name} on {selected_date} for {selected_service}.\nNotes: {notes}"
        messagebox.showinfo("Success", confirmation_message)

    def open_appointments_window(self):
        # Create a new window for displaying appointments
        appointments_window = tk.Toplevel(self.root)
        appointments_window.title("Appointments")

        # Set background color to pink
        appointments_window.configure(bg="#FFC0CB")

        # Text widget to display booked appointments
        appointments_text = tk.Text(appointments_window, height=10, width=60)
        appointments_text.pack(pady=20)

        # Display booked appointments in the text widget
        for idx, appointment in enumerate(self.appointments, start=1):
            appointments_text.insert(tk.END, f"{idx}. {appointment}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = AleBeautyApp(root)
    root.mainloop()
