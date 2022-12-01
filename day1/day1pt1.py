newlinechar = "\n"
doublenewlinechar = "\n\n"

with open("day1test.txt", "r") as f:
    data = f.read()
    allElves = data.split(doublenewlinechar)

for elfIndex, elf in enumerate(allElves):
    if newlinechar in elf:
        snacks = elf.split(newlinechar)
        result = sum(map(int, snacks))
        allElves[elfIndex] = result

mylist = list(map(int, allElves))
finalResult = max(mylist)
print(finalResult)
