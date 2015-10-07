from tkinter import *
from timeit import default_timer
import random
import matplotlib.pyplot as plt

allsolves = []
spacePressNo = 0
start = 0
lastTime = 0
solveNo = 0

def genscramble(scramblelength):
	operators = ["","'","2"]
	moves = ["R","L","U","D","F","B", "P","K"]
	thisScramble = ""
	n = "P"
	o = "K"
	while scramblelength != 0:
		if n == "R":
			o = "L"
		elif n == "L":
			o = "R"
		elif n == "D":
			o = "U"
		elif n == "U":
			o = "D"
		elif n == "F":
			o = "B"
		elif n == "B":
			o = "F"
		moves.remove(n)
		moves.remove(o)
		n = random.choice(moves)
		m = random.choice(operators)
		thisScramble += (n + m + " ") 
		moves = ["R","L","U","D","F","B"]
		scramblelength -= 1

	return(thisScramble)

def keyPress(event):

    if event.char == ' ':
    	helpText.set("")
    	start = takeTimer()

    elif event.char == 's':
    	helpText.set("")
    	currentScramble.set(genscramble(20))

    elif event.char == 'd':
    	helpText.set("")
    	popTime()
    	

    elif event.char == 'g':
    	helpText.set("")
    	genGraph()
    	

    elif event.char == 'h':
    	helpText.set("Press H to view HelpText.\nPress G to view a graph of times.\nPress S to get a new scramble.\nPress D to delete your last time.")

def popTime():
	global spacePressNo, start, allsolves, lastTime,solveNo

	try:
		allsolves.pop()
	except:
		helpText.set("No Times available to delete.")

	if solveNo != 0:
		solveNo -= 1


	currentAverage.set("Current Average: " + str(getAverage()))


	if len(allsolves) <=1:
		lastTime.set("0.00")
	else:
		lastTime.set("%0.2f" %allsolves[-1])
	numberOfSolves.set( "Number Of Solves: " + str(solveNo))
	currentScramble.set(genscramble(20))

def getAverage():

	global allsolves
	div = 0
	total = 0
	for score in allsolves:
		total += score
		div +=1
	if div != 0:
		average = total/div
		average = ("%0.2f" %average)
	else:
		average = 0.00
	return average

def takeTimer():

	global spacePressNo, start, allsolves, lastTime,solveNo

	
	if spacePressNo%2 == 0:

		start = default_timer()
		lastTime.set("Timing...")
		


	else:
		
		duration = default_timer() - start
		duration = float(duration)
		start = 0
		currentScramble.set(genscramble(20))
		allsolves.append(duration)
		currentAverage.set("Current Average: " + str(getAverage()))
		lastTime.set( "%0.2f" %duration)
		solveNo += 1
		numberOfSolves.set( "Number Of Solves: " + str(solveNo))

	spacePressNo += 1


def genGraph():
	global allsolves

	if len(allsolves) <= 1:
		helpText.set("No times available to create graph.\n(At least 2 times required)")
	else:
		plt.plot(allsolves,marker="o")
		plt.ylabel("Seconds")
		plt.xlabel("Solve")
		plt.show()


if __name__ == "__main__":

	

	root = Tk()

	currentScramble = StringVar()
	currentScramble.set(str( genscramble(20) ))

	currentAverage = StringVar()
	currentAverage.set("Current Average: 0.00")


	numberOfSolves = StringVar()
	numberOfSolves.set("Number Of Solves: 0")

	helpText = StringVar()
	helpText.set("Press H to view HelpText.\nPress G to view a graph of times.\nPress S to get a new scramble.\nPress R to delete your last time.")

	lastTime = StringVar()
	lastTime.set("0.00")

	frame = Frame(root)

	Label(frame,text=" ").grid(row=1,column=3)
	Label(frame,textvariable=currentScramble,font=18).grid(row=2,column=3)
	Label(frame,text=" ").grid(row=3,column=3)
	Label(frame,textvariable=currentAverage,font=18).grid(row=4,column=3)
	Label(frame,textvariable=numberOfSolves).grid(row=5,column=3)
	Label(frame,text=" ").grid(row=6,column=3)
	Label(frame,textvariable=lastTime,font=("bold",30)).grid(row=8,column=3)
	Label(frame,textvariable=helpText,font=16).grid(row=12,column=3)


	frame.bind("<Key>", keyPress)
	frame.focus_set()
	frame.pack()
	root.geometry('{}x{}'.format(450,270))
	root.title("Cube Timer Ver. 2.0")

	root.mainloop()	