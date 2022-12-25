inp = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

def get_value(dupe):
    vals = {
        "a" : 1,
        "b" : 2,
        "c" : 3,
        "d" : 4,
        "e" : 5,
        "f" : 6,
        "g" : 7,
        "h" : 8,
        "i" : 9,
        "j" : 10,
        "k" : 11,
        "l" : 12,
        "m" : 13,
        "n" : 14,
        "o" : 15,
        "p" : 16,
        "q" : 17,
        "r" : 18,
        "s" : 19,
        "t" : 20,
        "u" : 21,
        "v" : 22,
        "w" : 23,
        "x" : 24,
        "y" : 25,
        "z" : 26,
        "A" : 27,
        "B" : 28,
        "C" : 29,
        "D" : 30,
        "E" : 31,
        "F" : 32,
        "G" : 33,
        "H" : 34,
        "I" : 35,
        "J" : 36,
        "K" : 37,
        "L" : 38,
        "M" : 39,
        "N" : 40,
        "O" : 41,
        "P" : 42,
        "Q" : 43,
        "R" : 44,
        "S" : 45,
        "T" : 46,
        "U" : 47,
        "V" : 48,
        "W" : 49,
        "X" : 50,
        "Y" : 51,
        "Z" : 52,
        "" : 0
    }

    return vals[dupe]

current_backpack = ""
items_in_backpack = 0

first_comp = ""
second_comp = ""
dupe = ""

total = 0

for i in inp:
    if i != "\n":
        current_backpack += i
    if i == "\n":
        items_in_backpack = len(current_backpack)

        for x in range(0, round(items_in_backpack / 2)):
            first_comp += current_backpack[x]
        for x in range(round(items_in_backpack / 2) , items_in_backpack):
            second_comp += current_backpack[x]

        #print(first_comp)
        #print(second_comp)

        for x in first_comp:
            for y in second_comp:
                if x == y:
                    dupe = x
        #print(dupe)
        
        total += get_value(dupe)
        
        first_comp = ""
        second_comp = ""
        current_backpack = ""

print(total)