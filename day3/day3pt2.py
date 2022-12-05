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

n = len(allRucksacks)

list_of_groups = list(zip(*(iter(allRucksacks),) * 3))


for group in list_of_groups:
    elf1 = group[0]
    elf2 = group[1]
    elf3 = group[2]
    character = ''.join(
    set(elf1).intersection(elf2)
    .intersection(elf3))
    score = score + scoring.index(character)+1

print(score)
