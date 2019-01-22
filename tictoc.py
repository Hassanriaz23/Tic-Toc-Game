from tkinter import *
import tkinter.messagebox

frame = [None]*9
label = [None]*9
v = [None]*9
tick = [""]*9
player = 1
player1_turns = 0
player2_turns = 0


def game_end():
    global player1_turns,player2_turns
    for x in range(0, 9):
        tick[x] = ''
        player1_turns = 0
        player2_turns = 0
        if label[x] is not None:
            label[x].destroy()
        status_text.set('Start game')


def check_tie():
    return '' not in tick


def check_win():
        if tick[0] == tick[1] == tick[2] != '':
            if tick[0] == 'X':
                status_text.set(f'Player 1 wins in {player1_turns} turns')
            else:
                status_text.set(f'Player 2 wins in {player2_turns} turns')
            return True
        elif tick[3] == tick[4] == tick[5] != '':
            if tick[3] == 'X':
                status_text.set(f'Player 1 wins in {player1_turns} turns')
            else:
                status_text.set(f'Player 2 wins in {player2_turns} turns')
            return True
        elif tick[6] == tick[7] == tick[8] != '':
            if tick[6] == 'X':
                status_text.set(f'Player 1 wins in {player1_turns} turns')
            else:
                status_text.set(f'Player 2 wins in {player2_turns} turns')
            return True
        elif tick[0] == tick[4] == tick[8] != '':
            if tick[0] == 'X':
                status_text.set(f'Player 1 wins in {player1_turns} turns')
            else:
                status_text.set(f'Player 2 wins in {player2_turns} turns')
            return True
        elif tick[2] == tick[4] == tick[6] != '':
            if tick[2] == 'X':
                status_text.set(f'Player 1 wins in {player1_turns} turns')
            else:
                status_text.set(f'Player 2 wins in {player2_turns} turns')
            return True
        elif tick[0] == tick[3] == tick[6] != '':
            if tick[0] == 'X':
                status_text.set(f'Player 1 wins in {player1_turns} turns')
            else:
                status_text.set(f'Player 2 wins in {player2_turns} turns')
            return True
        elif tick[1] == tick[4] == tick[7] != '':
            if tick[1] == 'X':
                status_text.set(f'Player 1 wins in {player1_turns} turns')
            else:
                status_text.set(f'Player 2 wins in {player2_turns} turns')
            return True
        elif tick[2] == tick[5] == tick[8] != '':
            if tick[2] == 'X':
                status_text.set(f'Player 1 wins in {player1_turns} turns')
            else:
                status_text.set(f'Player 2 wins in {player2_turns} turns')
            return True
        elif check_tie() is True:
            status_text.set('Game tie')
            return True
        else:
            return False


def change(event, x):
    global player, player1_turns, player2_turns
    label[x] = Label(frame[x], textvariable=v[x], font=("Verdana", 40))
    label[x].pack(fill=BOTH)
    if player == 1:
        v[x].set('X')
        tick[x] = 'X'
        player1_turns += 1
        player = 2
        status_text.set('Player 2 Turn')
    elif player == 2:
        v[x].set('O')
        tick[x] = 'O'
        player2_turns += 1
        player = 1
        status_text.set('Player 1 Turn')
    if check_win() is True:
        answer = tkinter.messagebox.askyesno('Game ended','Want to start new game?')
        if answer is True:
            game_end()


root = Tk(className=' Tic Toc')
root.resizable(0, 0)    # disable maximize
v[0] = StringVar()
v[1] = StringVar()
v[2] = StringVar()
v[3] = StringVar()
v[4] = StringVar()
v[5] = StringVar()
v[6] = StringVar()
v[7] = StringVar()
v[8] = StringVar()
graphic_win = Canvas(root, width=200, height=200, bg='white')
graphic_win.pack(anchor=W)
line1 = graphic_win.create_line(0, 67, 200, 67, width=3)
line2 = graphic_win.create_line(0, 134, 200, 134, width=3)
line3 = graphic_win.create_line(67, 0, 67, 200, width=3)
line4 = graphic_win.create_line(134, 0, 134, 200, width=3)

frame[0] = Frame(bg='white')
frame[0].bind('<Button-1>', lambda eff: change(eff, x=0))

frame[1] = Frame(bg='white')
frame[1].bind('<Button-1>', lambda eff: change(eff, x=1))

frame[2] = Frame(bg='white')
frame[2].bind('<Button-1>', lambda eff: change(eff, x=2))

frame[3] = Frame(bg='white')
frame[3].bind('<Button-1>', lambda eff: change(eff, x=3))

frame[4] = Frame(bg='white')
frame[4].bind('<Button-1>', lambda eff: change(eff, x=4))

frame[5] = Frame(bg='white')
frame[5].bind('<Button-1>', lambda eff: change(eff, x=5))

frame[6] = Frame(bg='white')
frame[6].bind('<Button-1>', lambda eff: change(eff, x=6))

frame[7] = Frame(bg='white')
frame[7].bind('<Button-1>', lambda eff: change(eff, x=7))

frame[8] = Frame(bg='white')
frame[8].bind('<Button-1>', lambda eff: change(eff, x=8))


window = graphic_win.create_window(0, 0, width=65, height=65, window=frame[0], anchor=N+W)
window1 = graphic_win.create_window(70, 0, width=62, height=65, window=frame[1], anchor=N+W)
window2 = graphic_win.create_window(137, 0, width=62, height=65, window=frame[2], anchor=N+W)
window3 = graphic_win.create_window(0, 70, width=65, height=62, window=frame[3], anchor=N+W)
window4 = graphic_win.create_window(70, 70, width=62, height=62, window=frame[4], anchor=N+W)
window5 = graphic_win.create_window(137, 70, width=62, height=62, window=frame[5], anchor=N+W)
window6 = graphic_win.create_window(0, 137, width=65, height=65, window=frame[6], anchor=N+W)
window7 = graphic_win.create_window(70, 137, width=62, height=65, window=frame[7], anchor=N+W)
window8 = graphic_win.create_window(137, 137, width=62, height=65, window=frame[8], anchor=N+W)

# ************* Status Bar *******************
status_text = StringVar()
status_bar = Label(root, textvariable=status_text, bd=1, relief=SUNKEN,anchor=W)
status_bar.pack(side=BOTTOM, fill=X)
status_text.set('Start game')

root.mainloop()
