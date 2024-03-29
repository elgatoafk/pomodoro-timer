from tkinter import *
from constants import *
from customtkinter import *

reps = 0
timer = None

def start_timer():
    global reps
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps+=1

    

    if reps % 8 == 0:
        title_label.config(text="Long break", fg=RED)
        count_down(long_break_sec)
        
    elif reps % 2 == 0:
        title_label.config(text="Short break", fg=PINK)
        count_down(short_break_sec)
        
    else:
        title_label.config(text="Work:", fg=GREEN)
        count_down(work_sec)


def reset():
    global reps
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text=" ")
    window.after_cancel(timer)
    reps = 0
    

        


# counting down in window

def count_down(count):
    global timer
    count_min = count//60
    count_sec = count%60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
       timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark_label.config(text=CHECK_MARK*(reps//2))


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
img = PhotoImage(file=r'images\pomodoro_icon.png')
window.iconphoto(False, img)


# upper label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

# central part
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="images/tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# bottom part from left to right

start_button = CTkButton(window, text="Start", fg_color=START_COLOR, font=(FONT_NAME, 24, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = CTkButton(window, text="Reset", fg_color=RESET_COLOR, font=(FONT_NAME, 24, "bold"), command=reset)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg = GREEN, bg= YELLOW, font=(FONT_NAME, 24, "bold"))
checkmark_label.grid(column=1, row=3)






window.mainloop()