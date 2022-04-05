from tkinter import *
from tkinter import messagebox

from math import sqrt
from random import shuffle

NUMBER = 15

root = Tk("Memory Game")
my_frame = Frame(root) #Frame for all the tiles
my_frame.pack()

matches = [x for x in range(NUMBER) for _ in range(2)]
shuffle(matches)
chances = 25

won = False
count = 0
answer_list = []

# Reset the Game
def reset():
    global matches, won, tiles, chances
    chances = 25
    won = False
    shuffle(matches)

    # Reset Label
    label["text"] = ' '

    tiles = []
    for i in range(len(matches)):
        tiles.append(Button(my_frame, text = ' ', 
            font = ("Helvetica", 40), height =1, width = 3,
            command = lambda i=i: onclick(i)))

    for i in range(len(tiles)):
        row = i%cols
        col = int(i/cols)
        tiles[i].grid(row= row, column = col)

def find_rows_cols(number):
    max_cols = int(sqrt(number))
    for i in range(max_cols, 0, -1):
        if number % i == 0:
            cols = i
            break
    rows = int(number/cols)
    return rows, cols

def onclick(index):
    global answer_list, label, won, NUMBER, tiles, chances, tiles
    label["text"] = f'{chances = }'

    if tiles[index]["text"] == ' ': #If the tile has been clicked 
        tiles[index]["text"] = matches[index]
        answer_list.append(index)

    else: #If it has not been clicked
        tiles[index]["text"] = ' '
        answer_list = []

    if len(answer_list) == 2: # If two tiles have been clicked
        if matches[answer_list[0]] == \
            matches[answer_list[1]]:
            tiles[answer_list[0]]["state"] = DISABLED
            tiles[answer_list[1]]["state"] = DISABLED
            label["text"] = f"It's a Match! {chances = }"
            won += 1
            if won == NUMBER:
                label["text"] = "You Won!"
        else:
            chances -= 1
            label["text"] = f"Ahhh try again {chances = }"
            messagebox.showinfo("Incorrect", "Incorrect")

            tiles[answer_list[0]]["text"] = ' '
            tiles[answer_list[1]]["text"] = ' '

        answer_list = []

    if chances == 0:
        for tile in tiles:
            tile["state"] = DISABLED
        label["text"] = "You Lost D:"

rows, cols = find_rows_cols(len(matches))

#Defining the tiles
tiles = []
for i in range(len(matches)):
    tiles.append(Button(my_frame,
       text = ' ', 
        font = ("Helvetica", 40),
        height =1, width = 3,
        command = lambda i=i: onclick(i)))

#Adding the tiles to screen
for i,tile in enumerate(tiles):
    row = i%cols
    col = int(i/cols)
    tile.grid(row= row, column = col)

label = Label(root, text= f"{chances = }", font= ("Helvetica", 30))
label.pack()

my_menu = Menu(root)
root.config(menu=my_menu)

# Create an Options Dropdown Menu
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Reset Game", command=reset)
option_menu.add_separator()
option_menu.add_command(label="Exit Game", command=root.quit)

if __name__ == "__main__":
    root.mainloop()
