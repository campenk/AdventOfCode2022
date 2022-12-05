import string

newlinechar = "\n"
count = 0

with open("day4input.txt", "r") as f:
    data = f.read()
    allPairs = data.split(newlinechar)


for pair in allPairs:
    elves = pair.split(",")
    sections = []
    for elf in elves:
        elflist = (elf.split("-"))
        sections.append(list(map(int,elflist)))
    elf1 = set(list(range(sections[0][0],sections[0][1] + 1)))
    elf2 = set(list(range(sections[1][0],sections[1][1] + 1 )))
    if elf1.issubset(elf2):
        count = count + 1
    elif elf2.issubset(elf1):
        count = count + 1
print(count)
