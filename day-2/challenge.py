class Password:
    def __init__(self, line):
        quantity, character, password = line.strip().split()
        self.lower, self.upper = [int(n) for n in quantity.split('-')]
        self.character = character[0]
        self.password = password

    def is_valid_1(self):
        """
        Validation Rule 1
        Password must contain character at least lower times, but no more than upper times.
        """
        return (self.password.count(self.character) >= self.lower 
                and self.password.count(self.character) <= self.upper)

    def is_valid_2(self):
        """
        Validation Rule 2
        Password must contain character at lower or upper index, but not both.
        """
        first_char = self.password[self.lower - 1] == self.character
        last_char = self.password[self.upper - 1] == self.character
        return first_char != last_char


def main(input):
    with open('input.txt') as f:
        passwords = [Password(line) for line in f.read().splitlines()]

    answer_1 = sum(password.is_valid_1() for password in passwords)
    answer_2 = sum(password.is_valid_2() for password in passwords)

    print('Answer one is ' + str(answer_1))
    print('Answer two is ' + str(answer_2))


main(input)



