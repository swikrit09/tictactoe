board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ' ]
status="goingOn"
play=1
print("\n\n=========WELCOME TO ========\n =========TIC-TAC-TOE==========\n ===========GAME========== ")
def Draw():
	print("  %c  |  %c  |  %c  "%(board[1],board[2],board[3]))
	print("_____|_____|_____")
	print("  %c  |  %c  |  %c  "%(board[4],board[5],board[6]))
	print("_____|_____|_____")
	print("  %c  |  %c  |  %c "%(board[7],board[8],board[9]))
	print("     |     |     ")
def Check(x):
	if board[x]!=' ':
		return False
	else:
		return True
def checkWin():
	global status
	if board[1]==board[2] and board[2]==board[3] and board[1]!=' ':
		status="Win"
	elif board[1]==board[4] and board[4]==board[7] and board[5]!=' ':
		status="Win" 
	elif board[4]==board[5] and board[5]==board[6] and board[6]!=' ':
		status="Win"
	elif board[7]==board[8] and board[8]==board[9] and board[9]!=' ':
		status="Win"
	elif board[2]==board[5] and board[5]==board[8] and board[8]!=' ':
		status="Win"
	elif board[3]==board[6] and board[6]==board[9] and board[6]!=' ':
		status="Win"
	elif board[3]==board[5] and board[5]==board[7] and board[7]!=' ':
		status="Win"
	elif board[1]==board[5] and board[5]==board[9] and board[9]!=' ':
		status="Win"
	elif board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' ' :
		status="Tie"
	else:
		status="goingOn"
	return status
def Disp(status):
	if status=="Tie":
		print("\n\n::   Match Tied    ::")
	elif status=="Win":
		if play%2==0:
			print(" | | |Player 1 Wins :) its Party Time | | |")
		else:
			print(" | | |Player 2 Wins :) its Party Time | | |")
		print("\n\n Thanks Bro for Playing  Have a Nice Day")

print("\n\n[ X ] for Player1 and [ 0 ] for Player2\n\n")
while status=="goingOn":
	Draw()
	p1=int(input("\n\nPlayer1's Chance, Enter Position to place  :"))
	if Check(p1):
		board[p1]="X"
		play+=1
		Draw()
		Disp(checkWin())
	else:
		print("Kar Diya na Galti")
		
	p2=int(input("\n\nPlayer2's Chance, Enter Position to place  :"))
	if Check(p2):
		board[p2]="0"
		play+=1
		Draw()
		Disp(checkWin())
	else:
		print("Kar Diya na Galti")
else:
	print("Game Status ::",status)
