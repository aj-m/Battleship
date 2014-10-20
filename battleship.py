'''***********************************************************************************
Author: The Whole Class
Name: Battleship.py
Class: CSCI260 Class Project
Date: October 15, 2014
Special Thanks to: Beatrice-the Computer, StackOverflow, Wikipedia

Description: The game Battleship! The user places their ships on a board.
The AI then places their ships randomly. The user tries to guess the
location of the AI's ships. User and AI take turns until all of the ships
of one are destroyed.

Rules:

1. Players take turns to fire shots
2. When its your turn, call out the row and column of the square you want to attack
3. if hit there will be an x, if miss then there will be a -
4. once either opponent has sunk all ships, the game has been won
5. No looking at the other players board

************************************************************************************'''

#!/usr/bin/env python
import os		#For clear screen function
import random	#For ramdomly choosing locations when it is the computer's turn
import time		#For cool time delay when computer is placing ships
from collections import namedtuple	#To represent a point (x,y)

# Global variables
d_ships = {'user':{'A':0,'D':0,'P':0,'S':0,'B':0},'ai':{'A':0,'D':0,'P':0,'S':0,'B':0}}
userBoard = [[0 for j in range(8)]for i in range(8)]
AIB = [[0 for j in range(8)]for i in range(8)] #AI board
RNX = 0
RNY = 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: cls()
# Pre:  NONE
# Post: Screen has been cleared and title has been displayed
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def cls():
	os.system(['clear','cls'][os.name == 'nt'])
	print 30*("-")
	print " B A T T L E S H I P "
	print 30*("-")
# end cls()	
	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: PrintBoard() - displays appropriate playing board: user, computer hidden, or computer unhidden (for debuggung)
# Pre:  NONE
# Post: Empty board has been printed
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def PrintBoard(board,player):
	
	#Identifiers
	print "  1 2 3 4 5 6 7 8"		#Column header
	string = ""				#For user and computer board
	string1 = ""				#For blank board
	string2 = ""				#For test board
					

	if (player == "user"): 			# Userboard
		for i in range(0,8):		#Establishing row of board
			string += str(i+1)	#Incrementing through array
			for j in range(0,8):	#Establishing column of board
				string += '|' + str(board[i][j]) 
			string += "\n"
		print string
		
	elif (player == "blank"): 		#For debugging - to see computer board unhidden
		for i in range(0,8):
			string1 += str(i+1)
			for j in range(0,8):
				string1 += '|' + str(board[i][j]) 
			string1 += "\n"
		print string1
		
	else: 		#Computer Board - hidden from user
		for i in range(0,8):
			string2 += str(i+1)
			for j in range(0,8):
				if (board[i][j] == 'X' or board[i][j] == '-'): # hit or miss
					string2 += '|' + board[i][j]
				else: # ocean
					string2 += '|' + '*'
			string2 += '\n'
		print string2
# End PrintBoard()
		
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: AIGen() - Generates an AI board with randomly placed ships
# Pre: AIB has been defined
# Post: A computer generated board has been made
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def AIGen(AIB): #This is the AI board 
	iShipList = [5,4,3,3,2]		#Ship List
	cNameList = ['A','D','B','S','P']	#Ship Names/ Types
	iCount = 0			 #Counter based on ship placed
	
	while (iCount <=4):
		gCount = iShipList[iCount]
		#print gCount		#Uncomment for debugging purposes
		bEmptyCheck = 1	
		RNXC = 0		#Refers to horizontal
		RNYC = 0		 #Refers to vertical
		
		while (gCount >= 1): #RNJesus
			#print "First Loop"	#Uncomment for debugging purposes
			
			if(bEmptyCheck>0):
				#print "RNJESUS"		#Uncomment for debugging purposes
				RNX = random.randint(0,7)	#Random number generation for x axis
				RNXC = RNX			#Create a copy of random number for x axis
				RNY = random.randint(0,7)	#y axis RNG
				RNYC = RNY			#Copy of y
				RND = random.randint(0,3)	#Picks a random direction
				gCount = iShipList[iCount]	#Resets length of ship  (this loop is entered if the checking of open spaces fails)
				bEmptyCheck = 0
		
			while(bEmptyCheck == 0):
				#print "Check Loop"		#Uncomment for debugging purposes
				if (RNY > 7 or RNY < 0 or RNX > 7 or RNX < 0): #Checks if the location considered is out of bounds of game board
					#print "Bounds Check Fail"	#Uncomment for debugging purposes
					bEmptyCheck = 1		#Resets the RGN initial
				elif(AIB[RNY][RNX] == 'O'):
					#print "Check OK"	#Uncomment for debugging purposes
					if(RND == 0):		#Increment/decrement based on direction
						RNY = RNY - 1
					if(RND == 1):
						RNX = RNX + 1
					if(RND == 2):
						RNY = RNY + 1
					if(RND == 3):
						RNX = RNX - 1
					gCount -= 1		#Decrement gCount
				else:
					bEmptyCheck = 1		#Reset to reroll numbers
					
		#Placement Time
		count = iShipList[iCount]
		while (count > 0 and not gCount > 0):		#Count set to current ship number
			#print cNameList[iCount]		#Uncomment for debugging purposes
			AIB[RNYC][RNXC] = cNameList[iCount]	#Write out ships name at current point
			if(RND == 0):				#Increment/decrement based on the direction chosen
				RNYC = RNYC - 1
			if(RND == 1):
				RNXC = RNXC + 1
			if(RND == 2):
				RNYC = RNYC + 1
			if(RND == 3):
				RNXC = RNXC - 1
			count -= 1				#Decrement count (length)
		iCount += 1					 #Increment iCount
#End AIGen()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: CheckWin - checks if the board passed in is a winning board
# Pre: userBoard and AIB have been defined
# Post: Returns true or false - True if win, else false
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def CheckWin(player):
	for i in 'ABSDP':
		if(d_ships[player][i] != 'sunk'):
			return False
	return True
# End CheckWin()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: PlaceShip() - Algorithm to place ship in the chosen location and display it
#		on the board.
# Pre: length and ship Type have been declared
# Post: The ship has been placed in the requested location
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def PlaceShip(length, shipType):
	#Data validation	
	inputrepeat = True
	#inputrepeat2 = True		#Uncomment for debugging purposes
	#inputrepeat3 = True		#Uncomment for debugging purposes
	#inputrepeat4 = True		#Uncomment for debugging purposes
	
	#Data validation for startPointRow
	while inputrepeat:
		try:
			startPointRow = int(raw_input("Row of start point: "))
			inputrepeat = False
			while (startPointRow < 1 or startPointRow > 8):
				try:
					startPointRow = int(raw_input("Invalid row input. Please enter a number between 1 and 8: "))
				except ValueError:
					continue
		except ValueError:
			print "Invalid input. Please enter a number between 1 and 8."
	
	#Data validation for startPointColumn
	inputrepeat = True
	while inputrepeat:
		try:
			startPointColumn = int(raw_input("Column of start point: "))
			inputrepeat = False
			while (startPointColumn < 1 or startPointColumn > 8):
				try:
					startPointColumn = int(raw_input("Invalid column input. Please enter a number between 1 and 8: "))
				except ValueError:
					continue
		except ValueError:
			print "Invalid input. Please enter a number between 1 and 8."
	
	direction = raw_input("Vertical or horizontal? Type V or H: ").upper()
	
	#Data validation for direction
	while (direction != 'V' and direction != 'H'):
		direction = raw_input("Invalid direction. Vertical or horizontal? Type V or H: ").upper()
	
	while ((direction == 'V' and (startPointRow + length) > 9) or (direction == 'H' and (startPointColumn + length) > 9)):
			#Data validation for startPointRow
			inputrepeat = True
			while inputrepeat:
				try:
					startPointRow = int(raw_input("Invalid row input. Please enter a number between 1 and 8: "))
					inputrepeat = False
					while (startPointRow < 1 or startPointRow > 8):
						try:
							startPointRow = int(raw_input("Invalid row input. Please enter a number between 1 and 8: "))
						except ValueError:
							continue
				except ValueError:
					print "Invalid row input. Please enter a number between 1 and 8."
					
			#Data validation for startPointColumn
			inputrepeat = True
			while inputrepeat:
				try:
					startPointColumn = int(raw_input('Invalid column position. Re-enter column of start point: '))
					inputrepeat = False
					while (startPointColumn < 1 or startPointColumn > 8):
						try:
							startPointColumn = int(raw_input('Invalid column position. Re-enter row of start point: '))
						except ValueError:
							continue
				except ValueError:
					print "Invalid column position. Please enter a number between 1 and 8."

			direction = raw_input("Vertical or horizontal? Type V or H: ").upper()
			
			#Data validation for direction
			while (direction != 'V' and direction != 'H'):
				direction = raw_input("Invalid direction. Vertical or horizontal? Type V or H: ").upper()

	Row = startPointRow - 1
	Column = startPointColumn - 1

	count = 0
	countRow = 0
	countColumn = 0
	while (count < length):
		while (userBoard[Row + countRow][Column + countColumn] != 'O'):
			print "Location full. Choose a new starting point"
			startPointRow = input("Row of start point: ")
			startPointColumn = input("Column of start point: ")
			direction = raw_input("Vertical or horizontal? Type V or H: ")
			direction = direction.upper()
			
			Row = startPointRow - 1
			Column = startPointColumn - 1
		
		userBoard[Row + countRow][Column + countColumn] = shipType
		#print userBoard		#Uncomment for debugging purposes
		if direction == 'V':
			countRow = countRow + 1
		if direction == 'H':
			countColumn = countColumn + 1
		count += 1
# EndPlaceShip()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	 
# Function: Scoring()
# Pre:	To update score, caller will pass in current score (can be zero) and the occasion for the change in score.
# 	  	Pass the following in as "result" for the appropriate occasion:
# 	   	For the sinking of an AI ship: +50 points - "SunkAI" followed by the first letter of the ship name
# 	   	For the sinking of a user ship: -25 points - "SunkUser" followed by the first letter of the ship name
# 	   	For a hit on the AI board: +5 points - "H"
# 	   	For a miss on the AI board: -2 points - "M"
#		For a hit on the user board: -2 points - "M"
#	   	Remember punctuation
# Post: Score has been updated 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Scoring (score,result):
	if (result[0] == 'S'): #Sunk
		if (result[4] == 'A'): #AI
			if (result[6] == 'A'): #Aircraft Carrier
				score += 50
			elif (result[6] == 'S'): #Submarine
				score += 30
			elif (result[6] == 'B'): #Battleship
				score += 40
			elif (result[6] == 'D'): #Destroyer
				score += 30
			elif (result[6] == 'P'): #Patrol
				score += 20
		else: 			   #User
			if (result[8] == 'A'): #Aircraft Carrier
				score -= 25
			elif (result[8] == 'S'): #Submarine
				score -= 15
			elif (result[8] == 'B'): #Battleship
				score -= 20
			elif (result[8] == 'D'): #Destroyer
				score -= 15
			elif (result[8] == 'P'): #Patrol
				score -= 10
	elif (result[0] == 'H'):	#Hit
		score += 5
	else:
		score -= 2
	return score
# End Scoring()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: PrintAllBoards() - prints all boards, including the revealed computer board,
#							   for debugging purposes.
# Pre: NONE
# Post: Userboard and computerboards are updated to hit/miss
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~			
def PrintAllBoards(AIB,Userboard):
	print 'USER BOARD'
	PrintBoard(userBoard,'user')
	#print 'COMPUTER BOARD REVEALED'       #Uncomment for debugging purposes
	#PrintBoard(AIB,'blank')               #Uncomment for debugging purposes
	print 'COMPUTER BOARD'
	PrintBoard(AIB,'computer')
		
# End PrintAllBoards

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: Turn() - User turn: Fires on AI board and returns the result of turn (returned result 
#					 instead of direct print so result can be displayed in proper order).
#				   - Uses a dictionary of ships (array located at top) to keep track of hits 
#				     so sinking can be displayed
# Pre: player ('user' or 'ai'), userBoard, AIB, RNX, RNY have been assigned
# Post: Enemy board is updated to hit/miss, result and score have been returned 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~				

def Turn(player,opponentBoard,RNX,RNY,score):
	if(player == 'user'):
		opponent = 'ai'
	else:
		opponent = 'user'
	#aiWin = False		#Uncomment for debugging purposes
	#userWin = False	#Uncomment for debugging purposes
	currentType = opponentBoard[RNX][RNY]
	while(currentType == 'X' or currentType == '-'):
		random.seed()
		RNX = random.randint(0,7)
		RNY = random.randint(0,7)
		currentType = opponentBoard[RNX][RNY]

	x = RNX
	y = RNY
		
	#Ask for/recieve coordinates, store coordinates, and perform data validation
	while (player == 'user'):
		try:
			print 'Your turn:'
			guess = raw_input("Fire at which position (row column): ").upper()
			if (len(guess) <= 0): 
				raise Exception('No input given.')
			g_arr = guess.split()
			if(len(g_arr) > 2):
				raise Exception('Input too large.')
			#x = (ord(g_arr[0])-ord('A')) 	#For alphabetical rows in future game designing
			x = int(g_arr[0]) - 1
			y = int(g_arr[1]) - 1
			currentType = opponentBoard[x][y]
			if(currentType == 'X' or currentType == '-'):
				print "Already guessed - please guess again"
				continue
		except Exception as e:
			if(e.args[0] == 'No input given.'):
				print e.args[0]
			elif(e.args[0] == 'Input too large.'):
				print e.args[0]
			continue			
		break
	#If a hit occurs	
	if(currentType != 'O'):
		opponentBoard[x][y] = 'X'
		try:
			d_ships[opponent][currentType] += 1 #Increment the hit counter on the opponent's ship
			cls()			#Clear Screen
			#returnAllBoards(AIB,userBoard)		#Uncomment for debugging purposes			
			#Check each ship to see if sunk
			if(currentType == 'A' and d_ships[opponent][currentType] >= 5):		#Aircraft Carrier
				score = Scoring(score,'SunkAIA')
				d_ships[opponent][currentType] = 'sunk'
				cls()
				#returnAllBoards(AIB,userBoard)			#Uncomment for debugging purposes
				if(player == 'user'): return "You destroyed their aircraft carrier!",score
				else: return "Aircraft carrier destroyed!",score

			if(currentType == 'B' and d_ships[opponent][currentType] >= 3):		#Battleship
				score = Scoring(score,'SunkAIB')
				d_ships[opponent][currentType] = 'sunk'
				cls()
				#returnAllBoards(AIB,userBoard)			#Uncomment for debugging purposes
				if(player == 'user'): return "You destroyed their battleship!",score
				else: return "Battleship destroyed!",score

			if(currentType == 'S' and d_ships[opponent][currentType] >= 3):		#Submarine
				score = Scoring(score,'SunkAIS')
				d_ships[opponent][currentType] = 'sunk'
				cls()
				#returnAllBoards(AIB,userBoard)			#Uncomment for debugging purposes
				if(player == 'user'): return "You destroyed their submarine!",score
				else: return "Submarine destroyed!",score

			if(currentType == 'D' and d_ships[opponent][currentType] >= 4):		#Destroyer
				score = Scoring(score,'SunkAID')
				d_ships[opponent][currentType] = 'sunk'
				cls()
				#returnAllBoards(AIB,userBoard)			#Uncomment for debugging purposes
				if(player == 'user'): return "You destroyed their destroyer!",score
				else: return "Destroyer destroyed!",score

			if(currentType == 'P' and d_ships[opponent][currentType] >= 2):		#Patrol Boat
				score = Scoring(score,'SunkAIP')
				d_ships[opponent][currentType] = 'sunk'
				cls()
				#returnAllBoards(AIB,userBoard)			#Uncomment for debugging purposes
				if(player == 'user'): return "You destroyed their patrol boat!",score
				else: return "Patrol boat destroyed!",score
				
				
			#Display 'Hit!' if no sinking occurs
			score = Scoring(score,'H')
			if(player == 'user'):
				return 'Hit!',score
			elif(player == 'ai'):
				score = Scoring(score,'M')
				return 'You\'ve been hit!',score

		except TypeError: #Increment operation failed, meaning that ship is sunk already - would imply duplicate guess though
			return "That ship is destroyed, you shouldn't be seeing this",score
		
	#If control gets to here, a miss has occurred		
	else:
		opponentBoard[x][y] = '-'		
		#returnAllBoards(AIB,userBoard)		#Uncomment for debugging purposes
		if (player == 'user'):
			score = Scoring(score,'M')
			return "You missed!",score	
		else:
			return 'Computer missed!',score
# End Turn()	

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: main() - Handles Battleship game by calling appropriate functions and handling user input. 
#					 Begins with setting up user and AI boards, and handles guessing with a while loop
# 					 that runs until one side has won.
# Pre: None
# Post: Updated boards have been displayed according to user input and winner has been announced
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main ():
	cls()
	
	#Initialize both boards to all O's 
	for i in range(0,8):
		for j in range(0,8):
			userBoard[i][j] = 'O' 
	for i in range(0,8):
		for j in range(0,8):
			AIB[i][j] = 'O'
	
	#Place user ships
	PrintBoard(userBoard,"user")
	print "\nUser's turn to place ships \n"
	print "Place your aircraft carrier. 5 units long."
	length = 5
	shipType = 'A'
	PlaceShip(length, shipType)
	cls()
	PrintBoard(userBoard,"user")
	
	print "Place your submarine. 3 units long."
	length = 3
	shipType = 'S'
	PlaceShip(length, shipType)
	cls()
	PrintBoard(userBoard,"user")
	
	print "Place your battleship. 4 units long."
	length = 4
	shipType = 'B'
	PlaceShip(length, shipType)
	cls()
	PrintBoard(userBoard,"user")
	
	print "Place your destroyer. 3 units long."
	length = 3
	shipType = 'D'
	PlaceShip(length, shipType)
	cls()
	PrintBoard(userBoard,"user")
	
	print "Place your patrol boat. 2 units long."
	length = 2
	shipType = 'P'
	PlaceShip(length, shipType)
	cls()
	PrintBoard(userBoard,"user")
	
	print "Computer is placing ships..."
	AIGen(AIB)	#Place computer ships
	time.sleep(3) 	#Delays for 3 seconds for realistic effect
	
	#Initialize score, clear screen, and print boards to prep guessing stage
	cls()
	score = 0
	PrintAllBoards(AIB,userBoard)
	
	#Begin guessing phase: user --> AI --> user --> etc. until winner
	while ((CheckWin('user') != True) or (CheckWin('ai') != True)):
		random.seed() #Use system time to set a pseudo random seed.
		RNX = random.randint(0,7)
		RNY = random.randint(0,7)
		outputUser,score = Turn('user',AIB,RNX,RNY,score)
		if (CheckWin('ai')):
			PrintAllBoards(AIB,userBoard)
			print "Enemy fleet destroyed: You won!"
			break
		outputAI,score = Turn('ai',userBoard,RNX,RNY,score)
		if (CheckWin('user')):
			PrintAllBoards(AIB,userBoard)
			print "Computer wins!"
			break		
		cls()	#Clear screen		
		PrintAllBoards(AIB,userBoard)
		print outputUser
		time.sleep(1)
		print outputAI		
		#print "Score: ",score
		
	print 'Thanks for playing!'
main()
#End main()
