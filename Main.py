import tkinter
from tkinter import ttk
import MyStyles
import Entities
#TO DO: make head a slightly darker colour and make sure it updates properly!
#board[20][20]
#CONSTANTS
GAMETIME=185 #in milliseconds
SNAKE_HEAD_COLOUR="#076d07"
SNAKE_COLOUR="#07ad07"
FOOD_COLOUR="red"

#GLOBALS
HEIGHT=610
WIDTH=610
direction = 's'
direction_queue = []
state = False
highest_points=0

# Setting up window and styles
root = tkinter.Tk()
root.geometry("800x900")
root.title('Snake')

style = ttk.Style()
style.theme_use("default")
MyStyles.initStyles(style)
frm = ttk.Frame(root, padding=20, style="TFrame")
frm.pack()

###game functionss---------------------------------------------------------###
    ###gameloop control functions-------------###
def start_game(event):
    global state
    if not state:
        state = True
        game_loop()


def quit_game():
    root.destroy()


def CTRL_quit(event):
    global state
    if state:
        restart()
    else:
        quit_game()


def restart():
    global snake
    global apple
    global state
    global score
    state = False
    score.configure(text="Score: 0")
    snake.reset()
    apple.reset_all()


    ###movement functions-----------------------------###
def direction_change(event=None, d='n'):
    global direction
    global direction_queue
    if len(direction_queue) == 0:
        if d== 'a' and direction != 'd':
            direction_queue.append(d)
        elif d == 'd' and direction != 'a':
            direction_queue.append(d)
        elif d == 'w' and direction != 's':
            direction_queue.append(d)
        elif d == 's' and direction != 'w':
            direction_queue.append(d)
    elif len(direction_queue) == 1:
        if d== 'a' and direction_queue[0]!= 'd':
            direction_queue.append(d)
        elif d == 'd' and direction_queue[0]!= 'a':
            direction_queue.append(d)
        elif d == 'w' and direction_queue[0]!= 's':
            direction_queue.append(d)
        elif d == 's' and direction_queue[0]!= 'w':
            direction_queue.append(d)


def forward(s, a, d): #board = b, snake = s, direction=d
    #Move snake in its direction and checks for collisions
    global score
    if s.move(d) == -1:
        return -1
    a.restricted_squares.add((s.head.xcoord, s.head.ycoord))
    if s.head.xcoord<0 or s.head.xcoord>20:
        return -1
    if s.head.ycoord<0 or s.head.ycoord>20:
        return -1
    if s.head.ycoord == a.y and s.head.xcoord == a.x:
        s.add_Block()
        score.configure(text=f"Score: {s.length}")
        a.reset()
    else:
        a.restricted_squares.remove((s.tail.xcoord, s.tail.ycoord))
    return 0

    ###gameloop function----------------------------###
def game_loop():
    global root
    global board
    global snake
    global apple
    global state
    global direction
    global direction_queue
    global highest_points
    global highscore
    global score
    if state:
        if len(direction_queue) > 0:
            direction = direction_queue.pop(0)
        if forward(snake, apple, direction)==-1:
            if snake.length>highest_points:
                highest_points = snake.length
                highscore.configure(text=f"Highscore: {highest_points}")
            restart()
            direction = 's'
            direction_queue = []
        else:

            root.after(GAMETIME, game_loop)


###-------------------------------------###

#Keys
root.bind('<Escape>', CTRL_quit)

root.bind('<w>', start_game)#W
root.bind('<a>', start_game)#A
root.bind('<s>', start_game)#S
root.bind('<d>', start_game)#D
root.bind('<w>', lambda eff: direction_change(None, d='w'), add='+')#W
root.bind('<a>', lambda eff: direction_change(None, d='a'), add='+')#A
root.bind('<s>', lambda eff: direction_change(None, d='s'), add='+')#s
root.bind('<d>', lambda eff: direction_change(None, d='d'), add='+')#D
root.bind('<Up>', start_game)#Arrow keys
root.bind('<Left>', start_game)
root.bind('<Down>', start_game)
root.bind('<Right>', start_game)
root.bind('<Up>', lambda eff: direction_change(None, d='w'), add='+')
root.bind('<Left>', lambda eff: direction_change(None, d='a'), add='+')
root.bind('<Down>', lambda eff: direction_change(None, d='s'), add='+')
root.bind('<Right>', lambda eff: direction_change(None, d='d'), add='+')

#GRAPHICS
btn2 = ttk.Button(frm, text="QUIT", style="Quit.TButton", command=quit_game, width=20)
btn2.pack(side='bottom', pady=10)
btn = ttk.Button(frm, text="RESTART", style="Quit.TButton", command=restart, width=20)
btn.pack(side='bottom')
highscore = ttk.Label(frm, text=f"Highscore: {highest_points}", style="L1.TLabel")#HIGHSCORE
highscore.pack(side="bottom", pady=5)
score = ttk.Label(frm, text="Score: 0", style="L1.TLabel")#CURRENTSCORE
score.pack(side="bottom")

board = tkinter.Canvas(frm, bg="#292e28", height = HEIGHT, width = WIDTH,
                       highlightcolor='green', highlightbackground='green',
                       highlightthickness=3)
board.pack(side="top", pady=10)
snake = Entities.Snake(SNAKE_COLOUR, SNAKE_HEAD_COLOUR, board, HEIGHT, WIDTH)
apple = Entities.Food(board, FOOD_COLOUR, WIDTH, HEIGHT)


root.mainloop()