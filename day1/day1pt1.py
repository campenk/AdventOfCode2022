newlinechar = "\n"
doublenewlinechar = "\n\n"

with open("day1test.txt", "r") as f:
    data = f.read()
    lines = data.split(doublenewlinechar)

for elfIndex, elf in enumerate(lines):
    if newlinechar in elf:
        snacks = elf.split(newlinechar)
        result = sum(map(int, snacks))
        lines[elfIndex] = result

mylist = list(map(int, lines))
finalResult = max(mylist)
print(finalResult)
