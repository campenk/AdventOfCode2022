
newlinechar = "\n"
score = 0
win = 6
draw = 3
lose = 0
rock = 1
paper = 2
scissors = 3

with open("day2input.txt", "r") as f:
    data = f.read()  
    rounds = data.split(newlinechar)

for round in rounds:
    plays = round.split()
    if plays[0] == "A":
        opponent = "rock"
    elif plays[0] == "B":
        opponent = "paper"
    elif plays[0] == "C":
        opponent = "scissors"

    if plays[1] == "X":
        outcome = "lose"
    elif plays[1] == "Y":
        outcome = "draw"
    elif plays[1] == "Z":
        outcome = "win"

    if opponent == "rock":
                if outcome == "lose":
                    score += lose + scissors
                elif outcome == "draw":
                    score += draw + rock
                elif outcome == "win":
                    score += win + paper
    elif opponent == "paper":
                if outcome == "lose":
                    score += lose + rock
                elif outcome == "draw":
                    score += draw + paper
                elif outcome == "win":
                    score += win + scissors
    elif opponent == "scissors":
                if outcome == "lose":
                    score += lose + paper
                elif outcome == "draw":
                    score += draw + scissors
                elif outcome == "win":
                    score += win + rock

print(score)
