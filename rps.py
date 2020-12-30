# Name: Tony Schwebach
# Section: 
# Date: 9/3/19
# rps.py

#Rock Paper Scissors Game

print "***Welcome to Rock, Paper Scissors!***\n "

#Starting score 0 vs 0
score1 = 0
score2 = 0

#Define gameplay function
def gameplay():
    global score1
    global score2

    #Player 1 selection and validation
    p1 = raw_input ("Player 1, select rock (R), paper (P), or scissors (S). ")
    def valid(ps):
        while False == (ps == 'R' or  ps == 'P' or  ps == 'S'):
            ps = raw_input ("This is not a valid selection. Enter 'R', 'S', or 'P' ")
    valid(p1)

    #Player 2 selection and validation
    p2 = raw_input ("Player 2, select rock (R), paper (P), or scissors (S). ")
    valid(p2)

    #Winner logic
    p1w = "Player 1 wins! Score: Player 1:"
    
    if p1 == p2:
        print "Tie. Score: Player 1:", score1, " Player 2:", score2
    elif p1 == 'R' and p2 == 'S':
        score1 += 1
        print p1w, score1, "Player 2:", score2
    elif p1 == 'P' and p2 == 'R':
        score1 += 1
        print p1w, score1, "Player 2:", score2
    elif p1 == 'S' and p2 == 'P':
        score1 += 1
        print p1w, score1, "Player 2:", score2
    else:
        score2 += 1
        print "Player 2 wins! Score: Player 1:", score1, " Player 2:", score2

    #play again
    again = raw_input("Play again? (Y for yes)  ")
    if again == 'Y':
        gameplay()
    elif score1 > score2:
        print "Congrats Player 1!  Score: Player 1:", score1, " Player 2:", score2
    elif score2 > score1:
        print "Congrats Player 2!  Score: Player 1:", score1, " Player 2:", score2
    else:
        print "Ties are like kissing your sister. Score: Player 1:", score1, " Player 2:", score2

gameplay()
