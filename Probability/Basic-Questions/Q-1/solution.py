# Rolling 2 Dice with goal sum of 7

def calculate_answers():
    answers = [(i, j) for i in range(1, 7) for j in range(1,7) if i+j == 7]
    return len(answers)/(6*6), answers