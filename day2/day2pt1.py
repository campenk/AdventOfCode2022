
newlinechar = "\n"
score = 0
rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
lose = 0

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
        self = "rock"
    elif plays[1] == "Y":
        self = "paper"
    elif plays[1] == "Z":
        self = "scissors"

    if opponent == "rock":
                if self == "rock":
                    score += draw + rock
                elif self == "paper":
                    score += win + paper
                elif self == "scissors":
                    score += lose + scissors
    elif opponent == "paper":
                if self == "rock":
                    score += lose + rock
                elif self == "paper":
                    score += draw + paper
                elif self == "scissors":
                    score += win + scissors
    elif opponent == "scissors":
                if self == "rock":
                    score += win + rock
                elif self == "paper":
                    score += lose + paper
                elif self == "scissors":
                    score += draw + scissors

print(score)
