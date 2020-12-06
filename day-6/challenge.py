from collections import Counter

def open_file(file_path):
    with open(file_path) as f:
        return f.read()


def count_yesses(input):
    groups = input.split('\n\n')
    count_yesses = 0
    for group in groups:
        yesses = {c for line in group.split('\n') for c in line.strip()}
        count_yesses += len(yesses)
    return count_yesses

def count_yesses_with_consensus(input):
    groups = input.split('\n\n')
    count_yesses = 0
    for group in groups:
        people = group.split('\n')
        yesses = Counter(char for person in people for char in person)
        count_yesses += sum(count == len(people) for char, count in yesses.items())
    return count_yesses


def main():
    input = open_file('input/day-6.txt')
    count_one = count_yesses(input)
    print('Answer one is ' + str(count_one))

    count_two = count_yesses_with_consensus(input)
    print('Answer two is ' + str(count_two))


if __name__ == "__main__":
    main()

