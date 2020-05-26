# From Terminal do pip install treys
# https://github.com/worldveil/deuces
# Treys is a Python 3 compatible version

from treys import Card
from treys import Evaluator
from treys import Deck

deck = Deck()
board = deck.draw(5)
p1 = deck.draw(2)
p2 = deck.draw(2)
p3 = deck.draw(2)
p4 = deck.draw(2)
p5 = deck.draw(2)

print(Card.print_pretty_cards(board))
print(Card.print_pretty_cards(p1))
print(Card.print_pretty_cards(p2))
print(Card.print_pretty_cards(p3))
print(Card.print_pretty_cards(p4))
print(Card.print_pretty_cards(p5))

evaluator = Evaluator()
p1_score = evaluator.evaluate(board, p1)
p2_score = evaluator.evaluate(board, p2)
p3_score = evaluator.evaluate(board, p3)
p4_score = evaluator.evaluate(board, p4)
p5_score = evaluator.evaluate(board, p5)
scores  = [p1_score,p2_score,p3_score,p4_score,p5_score]

p1_class = evaluator.get_rank_class(p1_score)
p2_class = evaluator.get_rank_class(p2_score)
p3_class = evaluator.get_rank_class(p3_score)
p4_class = evaluator.get_rank_class(p4_score)
p5_class = evaluator.get_rank_class(p5_score)
classes  = [p1_class,p2_class,p3_class,p4_class,p5_class]

print(evaluator.class_to_string(p1_class))
print(evaluator.class_to_string(p2_class))
print(evaluator.class_to_string(p3_class))
print(evaluator.class_to_string(p4_class))
print(evaluator.class_to_string(p5_class))

print(p1_score)
print(p2_score)
print(p3_score)
print(p4_score)
print(p5_score)
ind = scores.index(min(scores))
print("The winner is player number", ind+1,"with the hand", evaluator.class_to_string(classes[ind]))

deck1 = Deck()
flop = deck1.draw(3)
print(Card.print_pretty_cards(flop))
turn = flop + list(deck1.draw(1))
print(Card.print_pretty_cards(turn))
river = turn + list(deck1.draw(1))
print(Card.print_pretty_cards(river))