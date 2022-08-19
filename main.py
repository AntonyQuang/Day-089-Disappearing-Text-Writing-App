from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk


# Tk start up

root = Tk()
root.title("Keep typing and nobody gets hurt!")
root.geometry("800x800+0+0")

frame = ttk.Frame(root, padding=10)
frame.grid()

# Variables

time_limit = 5
time = time_limit


# functions
def countdown():
    global time
    time -= 1
    timer.delete(0, END)
    timer.insert(0, str(time))
    if time > 0:
        root.after(1000, countdown)
    else:
        return game_over()


def typing(event):
    # To prevent any cheating by spamming "shift" or "ctrl"
    if event.char or event.keysym == "Enter":
        if text_box.get("1.0", "1.1") == "":
            root.after(1000, countdown)
        else:
            global time
            time = time_limit
            timer.delete(0, END)
            timer.insert(0, str(time))


def game_over():
    global time
    explanation.focus()
    text_box.delete("1.0", "end")
    text_box.configure(state="disabled")
    time = 0
    timer.delete(0, END)
    timer.insert(0, str(time))


def reset():
    global time
    time = time_limit
    timer.delete(0, END)
    timer.insert(0, str(time))
    text_box.configure(state="normal")
    text_box.focus()


# Widgets
title = ttk.Label(frame, text="Keep typing and nobody gets hurt!")
title.grid(row=0, column=1)

explanation = ttk.Label(frame, text="Once you start typing, you have only 5 seconds to keep typing. Fail to keep "
                                    "typing, and the whole text will disappear!")
explanation.grid(row=1, column=1)

timer = ttk.Entry(frame)
timer.insert(0, str(time_limit))
timer.grid(row=2, column=1)

text_box = scrolledtext.ScrolledText(frame, height=40)
text_box.grid(row=3, column=1, columnspan=3)
text_box.focus()

quit_button = ttk.Button(frame, text="Quit", command=root.destroy)
quit_button.grid(row=4, column=1, sticky="W")

reset_button = ttk.Button(frame, text="Reset", command=reset)
reset_button.grid(row=4, column=2)

text_box.bind("<KeyPress>", typing)



root.mainloop()