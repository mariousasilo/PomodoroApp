import math
import tkinter as tk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

root = tk.Tk()
root.title("Pomodoro")
root.config(pady=50, padx=50, background=YELLOW)
cycle = 1
work_cycle = 0


def reset():
    root.after_cancel(count_down.job)
    button_start.config(command=start)
    background.itemconfig(countdown, text=f"00:00")


def start():
    global work_cycle
    if cycle % 2 > 0:
        label_status.config(text='Work', fg=GREEN)
        work_cycle += 1
        count_down(WORK_MIN * 60)
    elif cycle % 8 == 0:
        label_status.config(text='Rest', fg=RED)
        work_cycle = 0
        count_down(LONG_BREAK_MIN * 60)
    elif cycle % 2 == 0:
        label_status.config(text='Rest', fg =PINK)
        count_down(SHORT_BREAK_MIN * 60)


def count_down(count):
    global cycle
    button_start.config(command=pressed_start)
    work_min = math.floor(count / 60)
    work_sec = count % 60
    count_down.job = root.after(1000, count_down, count - 1)
    if work_sec > 10 and work_min > 10:
        background.itemconfig(countdown, text=f"{work_min}:{work_sec}")
    elif work_sec < 10 and work_min > 10:
        background.itemconfig(countdown, text=f"{work_min}:0{work_sec}")
    elif work_sec > 10 and work_min < 10:
        background.itemconfig(countdown, text=f"0{work_min}:{work_sec}")
    elif work_sec < 10 and work_min < 10:
        background.itemconfig(countdown, text=f"0{work_min}:0{work_sec}")
    elif work_sec > 10 and work_min == 0:
        background.itemconfig(countdown, text=f"0{work_min}:{work_sec}")
    elif work_sec < 10 and work_min == 0:
        background.itemconfig(countdown, text=f"0{work_min}:0{work_sec}")
    if count == 0:
        root.attributes("-topmost", 1)
        root.attributes("-topmost", 0)
        label_count.config(text=work_cycle * '✔')
        root.after_cancel(count_down.job)
        cycle += 1
        start()


def pressed_start():
    pass


tomato = tk.PhotoImage(file="tomato.png")
background = tk.Canvas(background=YELLOW, width=206, height=226, highlightthickness=0)
background.create_image(103, 113, image=tomato)
countdown = background.create_text(103, 130, text="00:00", font=(FONT_NAME, 24, 'bold'), fill="white")
background.grid(row=1, column=1)

button_start = tk.Button(text='Start', font=(FONT_NAME, 12, 'normal'), command=start)
button_start.grid(row=2, column=0)

button_reset = tk.Button(text='Reset', font=(FONT_NAME, 12, 'normal'), command=reset)
button_reset.grid(row=2, column=2)

label_count = tk.Label(text='', font=(FONT_NAME, 12, 'normal'), background=YELLOW, fg=GREEN)
label_count.grid(row=3, column=1)

label_status = tk.Label(text='Timer', font=(FONT_NAME, 32, 'bold'), background=YELLOW, fg=GREEN)
label_status.grid(row=0, column=1)

root.mainloop()
# ✔
