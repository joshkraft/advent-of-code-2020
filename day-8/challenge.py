"""

We have a series of instructions. Here is a snippet:

nop +0
acc +1
jmp +4
acc +3

Here is what they do:
nop -> nothing, just move on to the next line. 
acc -> add n to the accumulator score, then move on
jmp -> skip forward n number of spaces in the instructions

Here is part one... right before any step is run a second time, what is the value of the accumulator score?

"""


def get_input():
    with open("input/day-8.txt", "r") as f:
        return f.read().split('\n')

def main():
    input = get_input()
    input = input[0:5] # <- temp
    accumulator_score = 0
    for instruction in input:
        action, quantity = instruction.split()

        print(action, quantity)


if __name__ == "__main__":
    main()