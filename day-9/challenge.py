def get_input():
    with open("input/day-9.txt", "r") as f:
        return [int(n) for n in f.read().split('\n')]


def find_first_invalid_number(input, window = 25):
    for i in range(window, len(input)):
        previous = input[i-window:i]
        valid = False

        for a in range(window):
            for b in range(window):
                if previous[a] + previous[b] == input[i]:
                    valid = True

        if not valid:
            return input[i]


def find_invalid_sum(input, invalid_number):
    for i in range(len(input)):
        for j in range(i+2, len(input)):
            window = input[i:j]
            if sum(window) == invalid_number:
                return min(window) + max(window)


def main():
    input = get_input()
    invalid_number = find_first_invalid_number(input)
    print('Answer one is ' + str(invalid_number))
    invalid_sum = find_invalid_sum(input, invalid_number)
    print('Answer two is ' + str(invalid_sum))


if __name__ == "__main__":
    main()