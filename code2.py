from tkinter import *

# Basic Setup
root = Tk()
root.title("Tic Tac Toe")
root.geometry("300x400")
root.configure(bg="#A1FFEF")


# Colors
bg_color = "#f0f0f0"  # Background color
button_color = "#ffffff"  # Button color
text_color = "#000000"  # Text color
frame1_color = "#d3d3d3"  # Frame color
frame2_color = "#A1FFEF"
highlight_color = "#6495ED"  # Highlight color for winning combination
win_color = "lime"


# Frames
frame1 = LabelFrame(root, padx=10, pady=10, bg=frame1_color)
frame1.pack(padx=5, pady=5)

frame2 = Frame(root, padx=10, pady=10, bg=frame2_color)
frame2.pack(padx=10, pady=5)


# Frame 1 - Tic Tac Toe Grid
buttons = [[None for _ in range(3)] for _ in range(3)]
current_player = "X"
xstate = [[0, 0, 0] for _ in range(3)]  # Initialize as separate instances
ostate = [[0, 0, 0] for _ in range(3)]  # Initialize as separate instances

def sum1(a, b, c):
    return a+b+c


def winner(result,winning_combination):
    if result == 1:
        for win in winning_combination:
            buttons[win[0]][win[1]]["bg"] = win_color
            buttons[win[0]][win[1]]["fg"] = text_color
            buttons[win[0]][win[1]]["activeforeground"] = text_color

    elif result == 0:
        for win in winning_combination:
            buttons[win[0]][win[1]]["bg"] = win_color
            buttons[win[0]][win[1]]["fg"] = text_color
            buttons[win[0]][win[1]]["activeforeground"] = text_color
    else:
        for i in range(3):
            for j in range(3):
                buttons[i][j]["bg"] = "yellow"
                buttons[i][j]["fg"] = text_color
                buttons[i][j]["activeforeground"] = text_color


def check_winner():
    global xstate, ostate
    d = {0: [0, 0], 1: [0, 1], 2: [0, 2], 3: [1, 0], 4: [1, 1], 5: [1, 2], 6: [2, 0], 7: [2, 1], 8: [2, 2]}
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        xsum = sum1(xstate[d[win[0]][0]][d[win[0]][1]], xstate[d[win[1]][0]][d[win[1]][1]], xstate[d[win[2]][0]][d[win[2]][1]])
        osum = sum1(ostate[d[win[0]][0]][d[win[0]][1]], ostate[d[win[1]][0]][d[win[1]][1]], ostate[d[win[2]][0]][d[win[2]][1]])
        if xsum == 3:
            winner(1,[d[win[0]], d[win[1]], d[win[2]]])
            return
        elif osum == 3:
            winner(0,[d[win[0]], d[win[1]], d[win[2]]])
            return

    tsum = sum(sum(x) for x in xstate) + sum(sum(x) for x in ostate)
    if tsum == 9:
        winner(-1,[[]])
        return

def state(row, col):
    global xstate, ostate, current_player
    if current_player == "X":
        xstate[row][col] = 1
    else:
        ostate[row][col] = 1
    check_winner()

def on_button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        state(row, col)
        current_player = "O" if current_player == "X" else "X"

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(frame1, text="", font=("Arial", 20), width=4, height=2,
                               command=lambda i=i, j=j: on_button_click(i, j))
        buttons[i][j]["bg"] = highlight_color
        buttons[i][j]["fg"] = text_color
        buttons[i][j]["activeforeground"] = text_color

        buttons[i][j].grid(row=i, column=j)

# Frame 2
def restart():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["bg"] = highlight_color

    global current_player
    current_player = "X"
    global xstate, ostate
    xstate = [[0, 0, 0] for _ in range(3)]  # Reset as separate instances
    ostate = [[0, 0, 0] for _ in range(3)]  # Reset as separate instances

def quit_game():
    root.destroy()

restart_button = Button(frame2, text="RESTART", command=restart, padx=10, pady=10, bg="#FFA07A", fg="navy", font=("Arial", 10, "bold"))
restart_button.grid(row=0, column=0, padx=15, pady=5)
quit_button = Button(frame2, text="QUIT", command=quit_game, padx=17, pady=10, bg="#F08080", fg="navy", font=("Arial", 10, "bold"))
quit_button.grid(row=0, column=1, padx=15, pady=5)

# main loop
root.mainloop()
