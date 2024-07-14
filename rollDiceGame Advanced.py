import tkinter
from tkinter import ttk
from tkinter import Label, Button, Entry
import random
from PIL import Image, ImageTk
import time

class DiceSimulator(tkinter.Tk):

    def __init__(self):
        super().__init__()

        self.title("Dice Game")
        self.geometry("300x320")
        self.dice_images = [
            ImageTk.PhotoImage(Image.open(f"dice-{i}.png")) for i in range(1, 7)
        ]
        self.label = Label(self, image=self.dice_images[0])
        self.label.pack(pady=10)

        self.roll_btn = Button(self, text="Click Me 😉", command=self.roll_dice)
        self.roll_btn.pack(side="bottom", padx=10, pady=20)


    def roll_dice(self):
        # animation
        for _ in range(10):
            self.label.config(image=random.choice(self.dice_images))
            self.update()
        time.sleep(0.1)
        # main function
        dice_face = random.randint(0, 5)
        self.label.config(image=self.dice_images[dice_face])
if __name__ == "__main__":
    app = DiceSimulator()

app.mainloop()