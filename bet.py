import sys, random,pickle
from treys import Card
from treys import Evaluator
from treys import Deck
from treys import Card
from treys import Evaluator
from treys import Deck

deck = Deck()
evaluator = Evaluator()
preflopupdate = 0
stages = {"preflop": 0, "flop": 1, "turn": 2, "river": 3}


def update_table(matrix, tablecards, mycards, actions, result):
    global preflopupdate, deck
    percentageranges = [0.25, 0.5, 0.75, 1]

    for i in range(len(percentageranges)):  # preflop update
        if preflopupdate < percentageranges[i] and preflopupdate >= percentageranges[i] - 0.25:
            if result:
                matrix[(0, i), 0] = matrix[(0, i), 0] - 0.5 * matrix[(0, i), 0] - 0.2
                matrix[(0, i), 1] = matrix[(0, i), 1] + 0.2 * matrix[(0, i), 1] + 0.2
                matrix[(0, i), 2] = matrix[(0, i), 2] + 0.5 * matrix[(0, i), 2] + 0.2
            else:
                matrix[(0, i), 0] = matrix[(0, i), 0] + 0.5 * matrix[(0, i), 0] + 0.2
                matrix[(0, i), 1] = matrix[(0, i), 1] - 0.2 * matrix[(0, i), 1] - 0.2
                matrix[(0, i), 2] = matrix[(0, i), 2] - 0.5 * matrix[(0, i), 2] - 0.2
    p_score1 = evaluator.evaluate(tablecards[:3], mycards)
    p_score2 = evaluator.evaluate(tablecards[:4], mycards)
    p_score3 = evaluator.evaluate(tablecards[:5], mycards)
    p1 = evaluator.get_five_card_rank_percentage(p_score1)
    p2 = evaluator.get_five_card_rank_percentage(p_score2)
    p3 = evaluator.get_five_card_rank_percentage(p_score3)
    for i in range(len(percentageranges)):  # flop update
        if p1 < percentageranges[i] and p2 >= percentageranges[i] - 0.25:
            if result:
                matrix[(1, i), 2] = matrix[(1, i), 0] - 0.5 * matrix[(1, i), 0] - 0.2  # fold
                matrix[(1, i), 1] = matrix[(1, i), 1] + 0.2 * matrix[(1, i), 1] + 0.2
                matrix[(1, i), 0] = matrix[(1, i), 2] + 0.5 * matrix[(1, i), 2] + 0.2
            else:
                matrix[(1, i), 2] = matrix[(1, i), 0] + 0.5 * matrix[(1, i), 0] + 0.2
                matrix[(1, i), 1] = matrix[(1, i), 1] - 0.2 * matrix[(1, i), 1] - 0.2
                matrix[(1, i), 0] = matrix[(1, i), 2] - 0.5 * matrix[(1, i), 2] - 0.2
    for i in range(len(percentageranges)):  # turn update
        if p2 < percentageranges[i] and p2 >= percentageranges[i] - 0.25:
            if result:
                matrix[(2, i), 2] = matrix[(2, i), 0] - 0.5 * matrix[(1, i), 0] - 0.2
                matrix[(2, i), 1] = matrix[(2, i), 1] + 0.2 * matrix[(2, i), 1] + 0.2
                matrix[(2, i), 0] = matrix[(2, i), 2] + 0.5 * matrix[(2, i), 2] + 0.2
            else:
                matrix[(2, i), 2] = matrix[(2, i), 0] + 0.5 * matrix[(2, i), 0] + 0.2
                matrix[(2, i), 1] = matrix[(2, i), 1] - 0.2 * matrix[(2, i), 1] - 0.2
                matrix[(2, i), 0] = matrix[(2, i), 2] - 0.5 * matrix[(2, i), 2] - 0.2
    for i in range(len(percentageranges)):  # river update
        if p3 < percentageranges[i] and p3 >= percentageranges[i] - 0.25:
            if result:
                matrix[(3, i), 2] = matrix[(3, i), 0] - 0.5 * matrix[(1, i), 0] - 0.2
                matrix[(3, i), 1] = matrix[(3, i), 1] + 0.2 * matrix[(3, i), 1] + 0.2
                matrix[(3, i), 0] = matrix[(3, i), 2] + 0.5 * matrix[(3, i), 2] + 0.2
            else:
                matrix[(3, i), 2] = matrix[(3, i), 0] + 0.5 * matrix[(3, i), 0] + 0.2
                matrix[(3, i), 1] = matrix[(3, i), 1] - 0.2 * matrix[(3, i), 1] - 0.2
                matrix[(3, i), 0] = matrix[(3, i), 2] - 0.5 * matrix[(3, i), 2] - 0.2
    return matrix


def botAction(matrix, myCards, communityCards, state, currentBetAmt):
    global preflopupdate, stages

    actionspossible = ["fold", "raise", "check"]
    if state == "preflop":
        rankscummulative = 0

        card1 = myCards[0]
        x = (Card.print_pretty_cards([card1]))
        card2 = myCards[1]
        y = (Card.print_pretty_cards([card2]))
        if x[2] == y[2]:
            rankscummulative = 1

        percentageranges = [0.25, 0.5, 0.75, 1]
        for i in range(len(percentageranges)):
            if rankscummulative < percentageranges[i] and rankscummulative >= percentageranges[i] - 0.25:
                maxx = float('-inf')
                action = -0.1
                summ=0
                for j in range(3):
                    check = matrix[(stages[state], i), j]
                    summ+=check
                    if check > maxx:
                        maxx = check
                        action = j
                if summ == 0:
                    action = random.randint(0, 2)
                return actionspossible[action]
    if state == "flop":
        deck = Deck()
        evaluator = Evaluator()
        rankscummulative = 0
        p_score = evaluator.evaluate(communityCards, myCards)
        rank_p = evaluator.get_five_card_rank_percentage(p_score)
        rankscummulative = rank_p
        percentageranges = [0.25, 0.5, 0.75, 1]
        for i in range(len(percentageranges)):
            if rankscummulative < percentageranges[i] and rankscummulative >= percentageranges[i] - 0.25:
                maxx = float('-inf')
                action = -0.1
                summ=0
                for j in range(3):
                    check = matrix[(stages[state], i), j]
                    summ+=check
                    if check > maxx:
                        maxx = check
                        action = j
                if summ == 0:
                    action = random.randint(0, 2)
                return actionspossible[action]
    if state == "turn":
        deck = Deck()
        evaluator = Evaluator()
        rankscummulative = 0
        p_score = evaluator.evaluate(communityCards, myCards)
        rank_p = evaluator.get_five_card_rank_percentage(p_score)
        rankscummulative = rank_p
        percentageranges = [0.25, 0.5, 0.75, 1]
        for i in range(len(percentageranges)):
            if rankscummulative < percentageranges[i] and rankscummulative >= percentageranges[i] - 0.25:
                maxx = float('-inf')
                action = -0.1
                summ=0
                for j in range(3):
                    check = matrix[(stages[state], i), j]
                    summ+=check
                    if check > maxx:
                        maxx = check
                        action = j
                if summ == 0:
                    action = random.randint(0, 2)
                return actionspossible[action]
    if state == "river":
        deck = Deck()
        evaluator = Evaluator()
        rankscummulative = 0
        p_score = evaluator.evaluate(communityCards, myCards)
        rank_p = evaluator.get_five_card_rank_percentage(p_score)
        rankscummulative = rank_p
        percentageranges = [0.25, 0.5, 0.75, 1]
        for i in range(len(percentageranges)):
            if rankscummulative < percentageranges[i] and rankscummulative >= percentageranges[i] - 0.25:
                maxx = float('-inf')
                action = -0.1
                summ=0
                for j in range(3):
                    check = matrix[(stages[state], i), j]
                    summ+=check
                    if check > maxx:
                        maxx = check
                        action = j
                if summ == 0:
                    action = random.randint(0, 2)
                return actionspossible[action]


def Round(Q_table, noRound, BlindAmt, InitAmt, betAmt):
    botAmt = fishAmt = InitAmt
    for i in range(noRound):
        print("round", i)
        actions = []
        if (botAmt < BlindAmt or fishAmt < BlindAmt):
            break
        deck = Deck()
        board = deck.draw(5)
        bot = deck.draw(2)
        fish = deck.draw(2)
        pot = 0
        # preflop
        # the bot moves first and is also the Blind
        curBetPreFlop = BlindAmt
        botAmt = botAmt - curBetPreFlop  # since the bot is the blind
        fishAmt = fishAmt - curBetPreFlop  # since opponent always calls a bet
        pot = 2 * curBetPreFlop
        action = botAction(Q_table, bot, [], 'preflop', betAmt)  # turn for bot to make a move
        if (action == "fold"):
            fishAmt = fishAmt + pot
            actions.append("fold")
            continue
        elif (action == 'check'):
            actions.append("check")
        elif (action == "raise"):
            actions.append("raise")
            curBetPreFlop = curBetPreFlop + betAmt
            botAmt = botAmt - betAmt
            pot = pot + betAmt
            if (fishAmt >= betAmt):
                fishAmt = fishAmt - betAmt
                pot = pot + betAmt
            else:  # fish goes all in
                pot = pot + fishAmt
                fishAmt = 0
                if (evaluator.evaluate(board, fish) < evaluator.evaluate(board, bot)):
                    # nofurther betting as all cards are revealed
                    fishAmt = pot
                    continue

        # flop
        curBetFlop = 0
        # Fish checks and the turn is for the bot to make a move
        action = botAction(Q_table, bot, board[:3], 'flop', betAmt)  # turn for bot to make a move
        if (action == "fold"):
            actions.append("fold")
            fishAmt = fishAmt + pot
            continue
        elif (action == 'check'):
            actions.append("check")

        elif (action == "raise"):
            actions.append("raise")
            curBetFlop = betAmt
            botAmt = botAmt - betAmt
            pot = pot + betAmt
            if (fishAmt >= betAmt):
                fishAmt = fishAmt - betAmt
                pot = pot + betAmt
            else:  # fish goes all in
                pot = pot + fishAmt
                fishAmt = 0
                if (evaluator.evaluate(board, fish) < evaluator.evaluate(board, bot)):
                    # nofurther betting as all cards are revealed
                    fishAmt = pot
                    continue
        # turn
        curBetTurn = 0
        # Fish checks and the turn is for the bot to make a move
        action = botAction(Q_table, bot, board[:4], 'turn', betAmt)  # turn for bot to make a move
        if (action == "fold"):
            actions.append("fold")
            fishAmt = fishAmt + pot
            continue
        elif (action == 'check'):
            actions.append("check")
        elif (action == "raise"):
            actions.append("raise")
            curBetTurn = betAmt
            botAmt = botAmt - betAmt
            pot = pot + betAmt
            if (fishAmt >= betAmt):
                fishAmt = fishAmt - betAmt
                pot = pot + betAmt
            else:  # fish goes all in
                pot = pot + fishAmt
                fishAmt = 0
                if (evaluator.evaluate(board, fish) < evaluator.evaluate(board, bot)):
                    # nofurther betting as all cards are revealed
                    fishAmt = pot
                    continue

        # river
        curBetRiver = 0
        # Fish checks and the turn is for the bot to make a move
        action = botAction(Q_table, bot, board, 'river', betAmt)  # turn for bot to make a move
        if (action == "fold"):
            actions.append("fold")
            fishAmt = fishAmt + pot
            continue
        elif (action == 'check'):
            actions.append("check")
        elif (action == "raise"):
            actions.append("raise")
            curBetRiver = betAmt
            botAmt = botAmt - betAmt
            pot = pot + betAmt
            if (fishAmt >= betAmt):
                fishAmt = fishAmt - betAmt
                pot = pot + betAmt
            else:  # fish goes all in
                pot = pot + fishAmt
                fishAmt = 0
                if (evaluator.evaluate(board, fish) < evaluator.evaluate(board, bot)):
                    # nofurther betting as all cards are revealed
                    fishAmt = pot
                    continue

        # evaluation
        result = -1
        if (evaluator.evaluate(board, fish) < evaluator.evaluate(board, bot)):
            fishAmt = fishAmt + pot
            result = 0
        else:
            botAmt = botAmt + pot
            result = 1
            print("bot won")
        Q_table = update_table(Q_table, board, bot, actions, result)
    for i in range(4):#Rounds
        print("Round",i)
        for j in range(4):#handstrength
            print("HandStrength", j)
            for k in range(0, 3):  # fold,check,raise
                print("Action",k)
                print(Q_table[(i, j), k])
        print()
    picklewords=open("Q.pkl","wb")
    pickle.dump(Q_table,picklewords)
    picklewords.close()


matrix = {}
# State---handstrengthrange---action percentage
for i in range(4):
    for j in range(4):
        for k in range(0, 3):  # fold,check,raise
            matrix[(i, j), k] = 0.0

a = Round(matrix, 1000, 5, 10000, 5)#Training done on a = Round(matrix, 10000, 5, 100000, 5)