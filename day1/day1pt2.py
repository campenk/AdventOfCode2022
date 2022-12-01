from pprint import pprint
newlinechar = "\n"
doublenewlinechar = "\n\n"

with open("day1input.txt", "r") as f:
    data = f.read()
    allElves = data.split(doublenewlinechar)

for elfIndex, elf in enumerate(allElves):
    if newlinechar in elf:
        snacks = elf.split(newlinechar)
        result = sum(map(int, snacks))
        allElves[elfIndex] = result

mylist = list(map(int, allElves))
mylist.sort(reverse=True)
finalResultpt2 = mylist[0] + mylist[1] + mylist[2]
print(finalResultpt2)
