from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Progressbar
import sys

p1, p2 = 'Player1', 'Player2'
Z = 0
sX, sO = 0, 0
player = 'X'


def playAgain():
	global  stop_game
	stop_game = False
	enableAllButton()
	for i in range(3):
		for j in range(3):
			states[i] [j] = 0
			b [i] [j].configure(text= " ", bg="brown")


def score():
	global scoreX
	global winner
	global player, Z, sX, sO, root
	won = Z
	nextPlay.config(state=DISABLED)
	if won == "X":
		sX += 1
		scoreX.config(text="{} [X]:   {}".format(p1, sX))
	elif won == "O":
		sO += 1
		scoreO.config(text="{} [O]:   {}".format(p2, sO))
	if sX ==3 or sO == 3:
		stop_game = True
		winner = messagebox.askyesno('Game Over', 'Highest Score:\n\t{}\n\t{}\nDo you want to play again?'.format(scoreX.cget('text'), scoreO.cget('text')))
	if winner == True:
		playAgain()
		scoreX, sO = 0, 0
		scoreX.config(text="{} [X]:  {}".format(p1, sX))
		scoreO.config(text="{} [O]:  {}".format(p2, sO))
	elif winner == False:
		exiting = messagebox.showinfo("Come Soon", "Hope! you have enjoyed the game.\n game is Exiting.....")
		root.destroy()


def desableAllButton():
	for i in range(3):
		for j in range(3):
			b[i] [j].config(state=DISABLED)

def enableAllButton():
	for i in range(3):
		for j in range(3):
			b[i] [j].config(state=NORMAL)


def getName():
	global player, p1, p2, player1E, player2E
	p1 = player1E.get()
	p2 = player2E.get()
	print('Player1:  ',  p1,  "    Player2:   ", p2)
	scoreX.config(text="{} [X] : 0".format(p1))
	scoreO.config(text="{} [O] : 0".format(p2))
	root.deiconify()
	mainWindow.destroy()


def load():
	global i, progress, loadingLabel
	loadingLabel = Label(mainWindow, text=" ", font='deansgate 10 bold', fg='yellow', bg='teal')
	loadingLabel.place(x=418, y=418, height=25)
	progress = Progressbar(mainWindow, orient='horizontal', length=245, mode='determinate')
	progress.place(x=170, y=418, height=25)
	if i <= 10:
		txt = str(10 * i) + '%'
		loadingLabel.config(text=txt)
		loadingLabel.after(1600, load)
		progress['value']= int(10 * i)
		i += 1
	if progress['value'] == 100:
		getName()


def mode2():
	global player1E, player2E
	mode.destroy()
	singleMode.destroy()
	twoMode.destroy()
	player1 = Label(mainWindow, text="Player 1 Name:  ", bg='teal', font='deansgate 15', fg='yellow')
	player1.place(x=40, y=232)
	player1E = Entry(mainWindow, fg='blue', font='deansgate', highlightbackground='blue' , highlightthickness=2, width=27)
	player1E.place(x=200, y=230, height=33)
	player1E.focus()

	Player2 = Label(mainWindow, text="Player 2 Name:  ", bg='teal', font='deansgate 15', fg='yellow')
	Player2.place(x=40, y=302)
	player2E = Entry(mainWindow, fg='blue', font='deansgate', highlightbackground='blue', highlightthickness=2, width=27)
	player2E.place(x=200, y=300, height=33)
	submit = Button(mainWindow, text="Player Game", font='deansgate 10', bg='blue', fg='white', width=15, command=load)
	submit.place(x=260, y=350, )

def exitWindow(e):
	try:
		mainWindow.wm_attributes('topmost', False)
		msg = messagebox.askyesno(title='Exit Game', message='Do you really want to exit Game')
	except:
		msg =  messagebox.askyesno(title='Exit Game', message="Do you really want to exit Game")
	if msg == True:
		sys.exit(root.destroy())


def callback(r, c):
	global player
	global winner
	if player == 'X' and states[r] [c] == 0 and stop_game == False:
		b[r] [c]. configure(text='X', fg='blue', bg='white')
		states [r] [c] = 'X'
		player = 'O'
	if player == "O" and states[r] [c]== 0 and stop_game == False:
		b[r] [c]. configure(text="O", fg='orange', bg='black')
		states[r] [c] = 'O'
		player = 'X'
	check_for_winner()


def check_for_winner():
	global winner
	global stop_game, Z
	for i in range(3):
		if states[i] [0] == states[i][1] ==states[i][2] !=0:
			b[i][0].configure(bg='grey')
			b[i][1].configure(bg='grey')
			b[i][2].configure(bg='grey')
			stop_game = True
			Z =states[i][0]#.......................
			winner = messagebox.showinfo('Winner', states[i][0] + "Won!", icon='info')
			desableAllButton()
			score()
			break

		elif states[0][i] ==states[1][i] == states[2][i] !=0:
			b[0][i].configure(bg='grey')
			b[1][i].configure(bg='grey')
			b[2][i].configure(bg='grey')
			stop_game = True
			Z = states[0][i]
			winner = messagebox.showinfo('Winner', states[1] [i] + "Won!")
			desableAllButton()
			score()
			break

		elif states[0] [0] ==states[1] [1] == states[2] [2]!=0:
			b[0] [0].configure(bg='grey')
			b[1] [1].configure(bg='grey')
			b[2] [2].configure(bg='grey')
			stop_game = True
			Z = states[0] [0]

		elif states[2] [0] ==states[1] [1] == states[0] [2]!=0:
			b[2] [0].configure(bg='grey')
			b[1] [1].configure(bg='grey')
			b[0] [2].configure(bg='grey')
			stop_game = True
			Z = states[2] [0]

			winner = messagebox.showinfo('Winner', states[1] [1] + "Won!")
			desableAllButton()
			score()
			break

	nextPlay.config(text='Play Again', fg='white', font='deansgate 10',  bg='teal', state=NORMAL)


root  = Tk()
root.title('Version 2 Advance  [ Tic Tac Toe ]')
root.resizable(0,0)
#root.geometry('600x600')
#root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icons/cn.png'))
root.bind('<Escape>', exitWindow)
bg = PhotoImage(file='icons/game.png')
bgImage = Label(root, image=bg).place(x=-60, y=0)

b = [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]]

states = [[0, 0, 0],
					[0, 0, 0],
					[0, 0, 0]] 
for i in range(3):
	for j in range(3):
		b [i] [j] = Button(font='deansgate 60', width=3, bg='teal', command=lambda r=i, c=j: callback(r, c))
		b [i] [j].grid(row=i, column=j)



mainWindow = Toplevel(root)
mainWindow.title('tic tac toe [version 2]  [Main Menu')
mainWindow.resizable(0, 0)
mainWindow.wm_iconbitmap('icons/KM.ico')
mainWindow.config(bg='green')
mainWindow.bind('<Escape>', exitWindow)

height = 650
width = 650
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 3) - (height // 3)
mainWindow.geometry("{}x{}+{}+{}".format(width, height,    x,  y)) 
mainWindow.overrideredirect(1)
mainWindow.wm_attributes("-topmost", True)


bgImage = Label(mainWindow, image=bg).place(x=-30, y=0)

devBy = Label(mainWindow, text='Tic Tac Toe version 2  [From kennartfoundation]', font='deansgate 18', fg='white', bg='black', width=150)
devBy.pack(side=TOP)

mode = Label(mainWindow, text='CHOSE MODE', bg='teal',  fg='white', font='deansgate 15 bold', width=20)
mode.place(x=168, y=180)


def onButtonS(e):
	singleMode['bg'] = 'teal'

def leaveButtonS(e):
	singleMode['bg'] ='goldenrod1'

def onButtonT(e):
	twoMode['bg'] ='goldenrod3'

def leaveButtonT(e):
	twoMode['bg'] ='goldenrod1'


singleMode = Button(mainWindow, text='Single player', font='deansgate 12 bold', fg='white', bg='goldenrod1', width=20, activebackground='goldenrod3', activeforeground='blue')
singleMode.place(x=190, y=230)	
singleMode.bind('<Enter>', onButtonS)
singleMode.bind('<Enter>', leaveButtonS)

twoMode = Button(mainWindow, text='Two player', bg='goldenrod1', font='deansgate 12 bold', fg='white', width=20, activebackground='goldenrod3', activeforeground='blue', command=mode2)
twoMode.place(x=190, y=280)
twoMode.bind('<Enter>', onButtonT)

nextPlay = Button(root, text=" ", width=20, height=2,  bg='black', command=playAgain)
nextPlay.grid(row=4, column=1, )

scoreX = Label(root, text="Score X:   ", font='deansgate 12')
scoreX.grid(row=4, column=0)

scoreO = Label(root, text="Score O:   ", font='deansgate 12')
scoreO.grid(row=4, column=2)
stop_game = False

copyri8 = Label(root, text="Developed by Kennartfoundation:   ", font='deansgate 14', fg='white', bg='teal', width=70)
copyri8.grid(row=5, columnspan=3)

 
root.withdraw()
root.mainloop()
 