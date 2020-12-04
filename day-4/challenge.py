import re

def open_file(file_path):
    with open(file_path) as f:
        return f.read().split('\n\n')


class Passport():
    def __init__(self, input):
        for property in input.split():
            key, value = property.split(':')
            setattr(self, key, value)

    def contains_required_fields(self):
        REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        return all(field in vars(self) for field in REQUIRED_FIELDS)

    def is_valid_height(self):
        height = self.hgt
        if height.endswith('cm'):
            height = height.replace('cm', '')
            try:
                return 150 <= int(height) <= 193
            except:
                return False
        elif height.endswith("in"):
            height = height.replace("in", "")
            try:
                return 59 <= int(height) <= 76 
            except:
                return False
        return False

    def contains_valid_values(self):
        if self.contains_required_fields():
            checks = [
            1920 <= int(self.byr) <= 2002,
            2010 <= int(self.iyr) <= 2020,
            2020 <= int(self.eyr) <= 2030,
            self.is_valid_height(),
            re.match(r"^#[0-9a-f]{6}$", self.hcl),
            self.ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
            re.match(r"^[0-9]{9}$", self.pid)
            ]

            return all(checks)
        else:
            return False


def main():
    input = open_file('input/day-4.txt')
    passports_with_required_fields = 0
    passports_with_valid_data = 0

    for line in input:
        pp = Passport(line)
        if pp.contains_required_fields(): 
            passports_with_required_fields += 1
        if pp.contains_valid_values():
            passports_with_valid_data += 1
    
    print('Answer one is ' + str(passports_with_required_fields))
    print('Answer two is ' + str(passports_with_valid_data))


if __name__ == '__main__':
    main()
    