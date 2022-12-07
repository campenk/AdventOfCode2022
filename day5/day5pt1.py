import string

count = 0

with open("day5input.txt", "r") as f:
    data = f.read()
    allStacks, instructions = data.split("\n\n")

#splits stack numbers into list of integers
stacknumbers = allStacks[allStacks.rfind(']') + 2:].split()
#extracts stack number string into single line, preserving formatting
indexes = allStacks[allStacks.rfind(']') + 2:]

#determine stack numbers, then find the index of those numbers in the original string
charIndexes = []
for i in stacknumbers:
    charIndexes.extend([index for index, char in enumerate(indexes)
        if char == i])


#extracts the stack contents
allStacks = allStacks[: allStacks.rfind(']') + 1]
allStacks = allStacks.split("\n")
allStacks.reverse()

stackdict = {}
for i in charIndexes:
    mylist = []
    for stack in allStacks:
        if (stack[int(i)].isspace() == False):
            mylist.append(stack[int(i)])
    stackNo = stacknumbers[charIndexes.index(i)]
    dict = {
        "index": i,
        "crates": mylist
    }
    stackdict.update({stackNo: dict})

#print(stackdict)

#parse instructions
instructions = instructions.split("\n")
for i in instructions:
    move = i.split()
    fromdict = stackdict[move[3]]
    todict = stackdict[move[5]]
    num = int(move[1])
    holdinglist = []
    while num > 0:
        holdinglist.append(fromdict["crates"].pop())
        num -= 1
    todict["crates"].extend(holdinglist)
    tostackno = stacknumbers[charIndexes.index(todict["index"])]
    fromstackno = stacknumbers[charIndexes.index(fromdict["index"])]
    stackdict.update({tostackno: todict})
    stackdict.update({fromstackno: fromdict})

result = ""
for stack in stackdict:
    result += (stackdict[stack]["crates"][len(stackdict[stack]["crates"])-1])

print(result)
