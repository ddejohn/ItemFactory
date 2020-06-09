import tkinter as tk

TITLE = """\nGreetings adventurer, and welcome to...\n
     _ _|  |                     ____|             |                           
       |   __|   _ \  __ `__ \   |     _` |   __|  __|   _ \    __|  |   |     
       |   |     __/  |   |   |  __|  (   |  (     |    (   |  |     |   |     
     ___| \__| \___| _|  _|  _| _|   \__,_| \___| \__| \___/  _|    \__, |     
                                                                    ____/     \n
...A random weapon and armor generator which\nprovides richly detailed descriptions,\nunique names, and basic item stats!\n"""

def next_step():
    print("Next step!")

def previous_step():
    print("Previous step!")

root = tk.Tk()
# root.geometry("600x400")
root.resizable(0,0)
root.columnconfigure(0, weight=1)

label = tk.Label(root, text=TITLE, font='TkFixedFont', bd=2, relief="sunken")
label.grid(row=0, column=0)

mode = tk.IntVar()
mode.set(0)
tk.Radiobutton(root, text="Weapon", variable=mode, value=0).grid(row=1, pady=5)
tk.Radiobutton(root, text="Armor", variable=mode, value=1).grid(row=2, pady=5)

tk.Button(root, text="Next", padx=10, command=next_step).grid(row=1000, sticky=tk.E, padx=5, pady=5)
tk.Button(root, text="Back", padx=10, command=previous_step).grid(row=1000, sticky=tk.W, padx=5, pady=5)
root.mainloop()
