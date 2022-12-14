from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk


# Tk start up

root = Tk()
root.title("Keep typing and nobody gets hurt!")
root.geometry("644x740+0+0")
root.configure(background="#C3B5CF")

frame = ttk.Frame(root, padding=10, style="custom.TFrame")
frame.grid()

# Tk Styles
style = ttk.Style(root)
style.configure('.', background='#C3B5CF')
style.configure('title.TLabel', font=('Calibri', 30, "bold"), foreground="#5F3027")
style.configure('text.TLabel', font=('Calibri', 15), foreground="#5F3027")
style.configure('custom.TButton', font=('Calibri', 11), foreground="#5F3027", bg="#88768C")
style.configure('timer.TEntry', font=('Courier', "52"))

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
    text_box.delete("1.0", "end")
    text_box.focus()


# Widgets
title = ttk.Label(frame, text="Keep Typing and Nobody Gets Hurt!", style="title.TLabel", justify="center")
title.grid(row=0, column=0, columnspan=2, pady=10)

explanation = ttk.Label(frame, text="Once you start typing, you have only 5 seconds to keep typing. Fail to keep "
                                    "typing, and the whole text will disappear!", style="text.TLabel", wraplength=600,
                        justify="center")
explanation.grid(row=1, column=0, columnspan=2)

timer = ttk.Entry(frame, justify="center")
timer.configure(font=('Calibri', "30"), width=3)
timer.insert(0, str(time_limit))
timer.grid(row=2, column=0, columnspan=2, pady=10)

text_box = scrolledtext.ScrolledText(frame, height=20, width=60)
text_box.grid(row=3, column=0, columnspan=2, pady=10)
text_box.configure(font=('Calibri', "14"), wrap=WORD)
text_box.focus()

quit_button = ttk.Button(frame, text="Quit", command=root.destroy, style="custom.TButton")
quit_button.grid(row=4, column=0, sticky="W")

reset_button = ttk.Button(frame, text="Reset", command=reset, style="custom.TButton")
reset_button.grid(row=4, column=1, sticky="E")

text_box.bind("<KeyPress>", typing)



root.mainloop()