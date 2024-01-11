# Solve the problem using "itertools.product" method

from itertools import product

def calculate_answers():
    dice = range(1, 7)
    answers = [ans for ans in product(dice, repeat=2) if sum(ans) == 7]
    return len(answers)/(6*6), answers