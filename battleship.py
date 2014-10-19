'''***********************************************************************************
Battleship.py
CSCI260 Class Project
October 15, 2014

Description: 


************************************************************************************'''

#!/usr/bin/env python
import os				#For clear screen function
import random				#For ramdomly choosing locations when it is the computer's turn
from collections import namedtuple	#To represent a point (x,y)

# Global variables
d_ships = {'user':{'A':0,'D':0,'P':0,'S':0,'B':0},'ai':{'A':0,'D':0,'P':0,'S':0,'B':0}}	#Ship types for both user and computer
userBoard = [[0 for j in range(8)]for i in range(8)]	#Set the user board
AIB = [[0 for j in range(8)]for i in range(8)]		#Set the computer board

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: cls() - Clears/resets the screen before starting a game
# Pre:  NONE
# Post: Screen has been cleared
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def cls():
	os.system(['clear','cls'][os.name == 'nt'])
	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: PrintBoard() - Formats the game board
# Pre:  NONE
# Post: Empty board has been printed
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def PrintBoard(board,player):
	
	#Identifiers
	print "  1 2 3 4 5 6 7 8"	#Column header
	string = ""			#For user and computer board
	string1 = ""			#For blank board
	string2 = ""			#For test board
					
	#Format user and computer boards
	if (player == "user" or player == "computer"):	
		for i in range(0,8):
			string += str(i+1)
			for j in range(0,8):
				string += '|' + str(board[i][j]) 
			string += "\n"	#increment and skip a line
#			row = ord(row) + 1
		print string
	
	#Format a blank board to be used when we wnat to hide placed ships
	elif (player == "blank"):		
		for i in range(0,8):
			string1 += str(i+1)
			for j in range(0,8):
				string1 += '|' + str(board[i][j]) 
			string1 += "\n" #increment and skip a line
#			row = ord(row) + 1
		print string1
	
	#If neither "user", "computer", or "blank" have been selected, print blank.
	else:
		for i in range(0,8):
			string2 = "" + str(i+1)
			for j in range(0,8):
				if (board[i][j] == 'X'):
					string2 += board[i][j] + '|'
				elif (board[i][j] == '-'):
					string2 += board[i][j] + '|'
		print string2
		
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: AIGen() - Generates the computer's turn.
# Pre: AIB has been defined
# Post: A computer generated board has been made
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def AIGen(AIB): #This is the AI board
	
	#Identifiers:
	iShipList = [5,4,3,3,2]			#Ship list
	cNameList = ['A','D','B','S','P']	#Ship names/type
	iCount = 0				#Counter
	
	while (iCount <=4):			
		gCount = iShipList[iCount]
		#print gCount
		bEmptyCheck = 1
		RNXC = 0			#Refers to horizontal
		RNYC = 0			#Refers to vertical
		
		while (gCount >= 1): 		#RNJesus	
			#print "First Loop"
			if(bEmptyCheck>0):
				#print "RNJESUS"
				RNX = random.randint(0,7)
				RNXC = RNX
				RNY = random.randint(0,7)
				RNYC = RNY
				RND = random.randint(0,3)
				gCount = iShipList[iCount]
				bEmptyCheck = 0
		
			while(bEmptyCheck == 0):
				#print "Check Loop"
				if (RNY > 7 or RNY < 0 or RNX > 7 or RNX < 0):
					#print "Bounds Check Fail"
					bEmptyCheck = 1
				elif(AIB[RNY][RNX] == 'O'):
					#print "Check OK"
					if(RND == 0):
						RNY = RNY - 1
					if(RND == 1):
						RNX = RNX + 1
					if(RND == 2):
						RNY = RNY + 1
					if(RND == 3):
						RNX = RNX - 1
					gCount -= 1
				else:
					bEmptyCheck = 1
		#Placement Time
		count = iShipList[iCount]
		while (count > 0 and not gCount > 0):
			#print cNameList[iCount]
			AIB[RNYC][RNXC] = cNameList[iCount]
			if(RND == 0):
				RNYC = RNYC - 1
			if(RND == 1):
				RNXC = RNXC + 1
			if(RND == 2):
				RNYC = RNYC + 1
			if(RND == 3):
				RNXC = RNXC - 1
			count -= 1
		iCount += 1
#End AIGen()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: CheckWin() - Checks if the user or computer has won
# Pre: userBoard and AIB have been defined
# Post: Returns true or false
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def CheckWin(board):
     for i in range (10):
          for j in range (10):
		if (board[i][j] != -1 and board[i][j] != 'X' and board[i][j] != '-'):
			return False
	return True
#End CheckWin()
	 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: isSunk() - Check if a ship has been sunk
# Pre: NONE
# Post: True has been returned if the ship was sunk or 
# False has been returned if the ship was not sunk
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def isSunk(aircraftHits, submarineHits, battleshipHits, destroyerHits, patrolHits, player):
	if player == 'user':
		if aircraftHits == 5:
			print "The computer has sunk your Aircraft Carrier"
		if submarineHits == 3:
			print "The computer has sunk your Submarine"
		if battleshipHits == 4:
			print "The computer has sunk your Battleship"
		if destroyerHits == 3:
			print "The computer has sunk your Destroyer"
		if patrolHits == 5:
			print "The computer has sunk your Patrol Boat"
	else:
		if aircraftHits == 5:
			print "You sunk the Aircraft Carrier"
		if submarineHits == 3:
			print "You sunk the Submarine"
		if battleshipHits == 4:
			print "You sunk the Battleship"
		if destroyerHits == 3:
			print "You sunk the Destroyer"
		if patrolHits == 5:
			print "You sunk the Patrol Boat"
# End isSunk()
	 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# Function: Scoring() - A scoring system for the game
# Pre:	To update score, caller will pass in current score (can be zero) and the
#	occasion for the change in score.
# 	  Pass the following in as "result" for the appropriate occasion:
# 	   For the sinking of an AI ship: "SunkAI" followed by the 1st letter of the ship name
# 	   For the sinking of a user ship: "SunkUser" followed by the 1st letter of the ship name
# 	   For a hit on the AI board: "H"
# 	   For a miss on the AI board: "M"
#	   Remember punctuation
# Post: Score has been updated 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Scoring (score,result):
	if (result[0] == 'S'): #sunk
		if (result[4] == 'A'): #AI
			if (result[6] == 'A'): #aircraft carrier
				score += 50
			elif (result[6] == 'S'): #submarine
				score += 30
			elif (result[6] == 'B'): #Battleship
				score += 40
			elif (result[6] == 'D'): #Destroyer
				score += 30
			elif (result[6] == 'P'): #Patrol
				score += 20
		else: 			   #User
			if (result[8] == 'A'): #aircraft carrier
				score -= 25
			elif (result[8] == 'S'): #submarine
				score -= 15
			elif (result[8] == 'B'): #Battleship
				score -= 20
			elif (result[8] == 'D'): #Destroyer
				score -= 15
			elif (result[8] == 'P'): #Patrol
				score -= 10
	elif (result[0] == 'H'):
		score += 5
	else:
		score -= 2
	return score
# End Scoring()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: PlaceShip() - Algorithm to place ship in the chosen location and display it
#		on the board.
# Pre: length and ship Type have been declared
# Post: The ship has been placed in the requested location
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''THIS IS NOT WORKING PROPERLY, HELP!'''
def PlaceShip(length, shipType):
	startPointRow = input("Row of start point: ")
	startPointColumn = input("Column of start point: ")
	direction = raw_input("Vertical or horizontal? Type V or H: ").upper()
	
	# data validation
	if (direction != 'V' and direction != 'H'):
		direction = raw_input("Invalid direction. Vertical or horizontal? Type V or H: ").upper()
	
	# check if ship will go off board
	while ((direction == 'V' and (startPointRow + length) > 8) or (direction == 'H' and (startPointColumn + length) > 8)):
			startPointRow = input('Invalid starting position. Re-enter row of start point: ')
			startPointColumn = input("Column of start point: ")
			direction = raw_input("Vertical or horizontal? Type V or H: ").upper()
			
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
		#print userBoard
		if direction == 'V':
			countRow = countRow + 1
		if direction == 'H':
			countColumn = countColumn + 1
		count += 1
	#print userBoard
# EndPlaceShip()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: Turn() - Loops through computer and user turns until the end of the game
# Pre: NONE
# Post: Userboard and computerboards are updated to hit/miss
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~				
def Turn(player,userBoard):
	if(player == 'user'):
		opponent = 'ai'
	else:
		opponent = 'user'
	#aiWin = False
	#userWin = False
	x = 0
	y = 0
	currentType = ''
	while True:
		try:
			guess = raw_input("Fire at which position: ").upper()
			if (len(guess) <= 0): 
				raise Exception('No input given.')
			g_arr = guess.split()
			#x = (ord(g_arr[0])-ord('A'))
			x = int(g_arr[0]) - 1
			y = int(g_arr[1]) - 1
			currentType = userBoard[x][y]
			if(currentType == 'X' or currentType == '-'):
				print "Already guessed - please guess again"
				continue
		except Exception as e:
			if(e.args[0] == 'No input given.'):
				print e.args[0]
				continue
			else: continue
		break
	if(currentType != 'O'):
		userBoard[x][y] = 'X'
		try:
			d_ships[opponent][currentType] += 1 #increment the hit counter on the opponent's ship

			if(currentType == 'A' and d_ships[opponent][currentType] >= 5):
				d_ships[opponent][currentType] = 'sunk'
				if(player == 'user'): print "You destroyed their aircraft carrier!"
				else: print "Aircraft carrier destroyed!"

			if(currentType == 'B' and d_ships[opponent][currentType] >= 4):
				d_ships[opponent][currentType] = 'sunk'
				if(player == 'user'): print "You destroyed their battleship!"
				else: print "Battleship destroyed!"

			if(currentType == 'S' and d_ships[opponent][currentType] >= 3):
				d_ships[opponent][currentType] = 'sunk'
				if(player == 'user'): print "You destroyed their submarine!"
				else: print "Submarine destroyed!"

			if(currentType == 'D' and d_ships[opponent][currentType] >= 3):
				d_ships[opponent][currentType] = 'sunk'
				if(player == 'user'): print "You destroyed their destroyer!"
				else: print "Destroyer destroyed!"

			if(currentType == 'P' and d_ships[opponent][currentType] >= 2):
				d_ships[opponent][currentType] = 'sunk'
				if(player == 'user'): print "You destroyed their patrol boat!"
				else: print "Patrol boat destroyed!"
		except TypeError: #Increment operation failed, meaning that ship is sunk already - would imply duplicate guess though
			print "That ship is destroyed, you shouldn't be seeing this"

		victory = True
		for i in "ADBSDP":
			if(d_ships[opponent][i] != 'sunk'):
				victory = False
				break

		if(victory):
			#call Victory(player) ?
			if(player == 'user'):
				userWin == True
				aiWin == False
			else:
				userWin == False
				aiWin == True


	else:
		userBoard[x][y] = '-'
		print "You missed!"			
# End Turn()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: main() - Execution of Battleship game
# Pre: 
# Post: Battleship has been executed successfully--User and computer have taken turns;
#	ships have been placed; score has been recorded; sinked ships have been recorded;
#	and, wins have been identified.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main ():
	cls()
	
	for i in range(0,8):
		for j in range(0,8):
			userBoard[i][j] = 'O'
	for i in range(0,8):
		for j in range(0,8):
			AIB[i][j] = 'O'
	
	print 30*("-")
	print " B A T T L E S H I P "
	print 30*("-")
	
	#place user ships
	PrintBoard(userBoard,"user")
	print "\nUser's turn to place ships \n"
	print "Place your aircraft carrier. 5 units long."
	length = 5
	shipType = 'A'
	PlaceShip(length, shipType)
	PrintBoard(userBoard,"user")
	
	print "Place your submarine. 3 units long."
	length = 3
	shipType = 'S'
	PlaceShip(length, shipType)
	PrintBoard(userBoard,"user")
	
	print "Place your battleship. 4 units long."
	length = 4
	shipType = 'B'
	PlaceShip(length, shipType)
	PrintBoard(userBoard,"user")
	
	print "Place your destroyer. 3 units long."
	length = 3
	shipType = 'D'
	PlaceShip(length, shipType)
	PrintBoard(userBoard,"user")
	
	print "Place your patrol boat. 2 units long."
	length = 2
	shipType = 'P'
	PlaceShip(length, shipType)
	PrintBoard(userBoard,"user")
	
	print "Computer is placing ships..."
	AIGen(AIB)	# Place computer ships
	
	cls()
	print 30*("-")
	print " B A T T L E S H I P "
	print 30*("-")
	
	print "YOUR BOARD"
	PrintBoard(userBoard, "user")
	print "COMPUTER BOARD"
	PrintBoard(userBoard, "blank")
	
	while CheckWin(userBoard) != True or CheckWin(AIB) != True:
		Turn("user")
		CheckWin (userBoard)
		if CheckWin == True:
			print "User wins!"
			break
		Turn("computer")
		CheckWin (AIB)
		if CheckWin == True:
			print "Computer wins!"
			break
	
	# Print board for debugging	
	#PrintBoard(AIB, "computer")
	
main()
#Main()