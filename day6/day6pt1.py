import string
from collections import Counter

count = 0
def parseinput():
    with open("day6input.txt", "r") as f:
        return f.read()

#test data
test1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test3 = "nppdvjthqldpwncqszvftbrmjlhg"
test4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

def compute(data):
    result = 0
    i = 0
    while (i < len(data) and result == 0):
        codon = data[i:i+4]
        if len(set(codon)) == len(codon):
            result = i+4
        i += 1
    print(result)



compute(parseinput())
