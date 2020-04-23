from tkinter import *
from functools import partial


class Start:
    def __init__(self, parent):

        background_color = "white"

        self.start_frame = Frame(bg=background_color, pady=10)
        self.start_frame.grid()

        self.temp_Converter_label = Label(self.start_frame,
                                          text="Mystery Box Game",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_Converter_label.grid(row=0)

        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=1)

        self.lowstakes_button = Button(self.start_frame,
                                       text="Low($5)",
                                       padx=10,
                                       pady=10,
                                       command=lambda: self.to_game(1))
        self.lowstakes_button.grid(row=2)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()
        Game(self, stakes, starting_balance)


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        partner.lowstakes_button.config(state=DISABLED)

        self.balance = IntVar()

        self.balance.set(starting_balance)

        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        #Heading Row
        self.heading_label = Label(self.game_frame, text="Heading",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        #Balance Label
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)

        self.balance_label = Label(self.game_frame, text="Balance...")
        self.balance_label.grid(row=3)

        self.play_button = Button(self.game_frame, text="Gain",
                                   padx=10, pady=10, command=self.reveal_boxes)
        self.play_button.grid(row=4)

    def reveal_boxes(self):
        # retrieval the balance from the initial function
        current_balance = self.balance.get()

        #adjust balance
        current_balance +=2

        #set balance to new balance
        self.balance.set(current_balance)

        #Edit label so user can see balance
        self.balance_label.configure(text="Balance: {}".format(current_balance))


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()