from random import randint
pokerDeck = Deck()
noOfPlayers = 5
initialAmount = 3000
money = [initialAmount for i in range(noOfPlayers)]
playerInd = []

#pre flop
blind = randint(0,noOfPlayers-1) 
for i in range(blind,noOfPlayers):
    playerInd.append(i)
for i in range(blind):
    playerInd.append(i)
    
flop_amt = 100
curBet = flop_amt
money[blind]-=curBet
maxBet = playerInd[0]
i = 0
while True:
    if playerInd[i]!=blind:
        print("Player no:",playerInd[i],"Currently Betting: 0 Available Balance:",money[playerInd[i]],"Curent Bet:",curBet)
    else:
        print("Player no:",playerInd[i],"Currently Betting:",curBet,"Available Balance:",money[playerInd[i]],"Curent Bet:",curBet)
    ans = input("Do you want to 1) Call 2) Fold 3) Raise")
    if(ans=='1'):
        print("Player",playerInd[i],"Calls")
        if not(i==blind and curBet==flop_amt):
            money[playerInd[i]]-=curBet
    elif(ans=='2'):
        print("Player",playerInd[i],"Folds")
        playerInd.remove(playerInd[i])
        i = i-1
    else:
        while True:
            amt=int(input("How much do you want to raise by?"))
            if(amt<=money[playerInd[i]]):
                break
            else:
                print("Amount entered is more then available balance, enter again!")
        curBet=amt
        money[playerInd[i]]-=amt
        maxBet = playerInd[i]
    if (i<len(playerInd)-1 and playerInd[i+1]==maxBet):
        print("Ending")
        break
    elif (i==len(playerInd)-1 and playerInd[0]==maxBet): 
        break
    else:
        i = i+1
        if(i>=len(playerInd)):
            i=0  
            
print(playerInd)            