import string

newlinechar = "\n"
common_characters = ""
scoring = []
score = 0

for s in string.ascii_letters:
    scoring.append(s)

with open("day3input.txt", "r") as f:
    data = f.read()
    allRucksacks = data.split(newlinechar)


for rucksack in allRucksacks:
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]
    character = ''.join(
    set(compartment1).intersection(compartment2)
    )
    score = score + scoring.index(character)+1

print(score)
