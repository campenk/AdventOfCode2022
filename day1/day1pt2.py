from pprint import pprint
newlinechar = "\n"
doublenewlinechar = "\n\n"

with open("day1input.txt", "r") as f:
    data = f.read()
    lines = data.split(doublenewlinechar)

for elfIndex, elf in enumerate(lines):
    if newlinechar in elf:
        snacks = elf.split(newlinechar)
        result = sum(map(int, snacks))
        lines[elfIndex] = result

mylist.sort(reverse=True)
finalResultpt2 = mylist[0] + mylist[1] + mylist[2]
print(finalResultpt2)
