#4
def find_winner(player1 ="rock", player2 ="rock"):
    if player1 == player2:
        return "it's a tie!"
    if (player1 == "rock"and player2 == "scissors") or (player1 == "scissors"and player2 == "rock"):
        return "player1 win!"
    else:
        return "player 2 win!"
    
print

#8
def descending_porder(num1, num2 = 15, num3 = 3):
    a, b, c, = num1, num2, num3      #a=num1 b=num2 c=num3
    if a<b:
        a,b = b,a
    if a<c:
        a,c = c,a
    if b<c:
        b,c = c,b
    return[a,b, c]   
   


#15
def is_negative(num):
    if num < 0:
        return True
    else:
        return False
    
    #shorter way
    #def is_negative(num):
         #return num<0

def is_odd(num)
    if num % 2 == 1:
         return True
    else:
        return False
    
#shorter way
    #def is_odd(num):
         #return num % 2 ==1

def report_negative_odds(lyst):
    output =[]

    for num in lyst:
        if is_negative(num) and is_odd(num):
            output.append(num)
    return output