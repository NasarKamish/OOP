from tkinter import *
from tkinter import messagebox
Ticket = Tk()
Ticket.title("Ticket Sales")
Ticket.geometry("600x500")
Ticket.resizable(False, False)
Ticket.config(bg="white")


class TicketSales:
    def __init__(self, window):
        # Labels
        self.lbl_number = Label(window, text="Please enter cell number: ", bg="white")
        self.lbl_number.place(x=50, y=50)
        self.lbl_category = Label(window, text="Select the ticket type you'd like: ", bg="white")
        self.lbl_category.place(x=50, y=100)
        self.lbl_ticket_number = Label(window, text="How many tickets would you like?: ", bg="white")
        self.lbl_ticket_number.place(x=50, y=150)
        # Entries
        self.en_Cell = Entry(window)
        self.en_Cell.place(x=350, y=50, width=200)
        # OptionMenu
        self.options = ["Soccer", "Movie", "Theatre"]
        self.default_txt = StringVar(window)
        self.default_txt.set("Select Ticket")
        self.menu_Categories = OptionMenu(window, self.default_txt, *self.options)
        self.menu_Categories.place(x=350, y=95, width=200)
        # SpinBox
        self.spn_ticket_number = Spinbox(window, from_=1, to=100, width=3)
        self.spn_ticket_number.place(x=350, y=150, width=200)
        # Buttons
        self.btn_cal = Button(window, text="Calculate Price", borderwidth="5", command=self.calculate, bg="red", fg="black")
        self.btn_cal.place(x=50, y=250, width=200)
        self.btn_clear = Button(window, text="Clear", borderwidth="5", command=self.clear, bg="red", fg="black")
        self.btn_clear.place(x=350, y=250, width=200)
        # Results
        self.lbl_rescalc = Label(Ticket, text="", bg="white")
        self.lbl_ticket_res = Label(Ticket, text="", bg="white")
        self.lbl_cell_txt = Label(Ticket, text="", bg="white")
        self.lbl_rescalc.place(x=100, y=320)
        self.lbl_ticket_res.place(x=100, y=380)
        self.lbl_cell_txt.place(x=100, y=440)

    def calculate(self):
        # Constant variables
        tcktno = int(self.spn_ticket_number.get())
        vat = float(0.14)
        try:
            # Error Parameters
            int(self.en_Cell.get())
            if len(self.en_Cell.get()) > 10 or len(self.en_Cell.get()) < 10:
                raise ValueError

            elif self.default_txt.get() == "Select Ticket":
                raise ValueError

            elif int(self.spn_ticket_number.get()) == 0:
                raise ValueError

            # Soccer
            elif self.default_txt.get() == "Soccer":
                price = 40
                amount = tcktno * (price + vat)
                result = ("Total Amount: R{}".format(amount))
                self.lbl_rescalc.config(text=result)

            # Movie
            elif self.default_txt.get() == "Movie":
                price = 75
                amount = tcktno * (price + vat)
                result = ("Total Amount: R{}".format(amount))
                self.lbl_rescalc.config(text=result)

            # Theatre
            elif self.default_txt.get() == "Theatre":
                price = 100
                amount = tcktno * (price + vat)
                result = ("Total Amount: R{}".format(amount))
                self.lbl_rescalc.config(text=result)
            # Results
            tickets = "{} ticket(s) reserved : {} ".format(self.default_txt.get(), tcktno)
            cell = "Reservations made by: {}".format(self.en_Cell.get())
            self.lbl_ticket_res.config(text=tickets)
            self.lbl_cell_txt.config(text=cell)

        except ValueError:
            messagebox.showerror("ERROR", "Please enter all relevant information")

    # Defining clear button
    def clear(self):
        self.en_Cell.delete(0, END)
        self.lbl_rescalc.config(text="")
        self.lbl_ticket_res.config(text="")
        self.lbl_cell_txt.config(text="")


# Run Program
TicketSales(Ticket)
Ticket.mainloop()
