def open_file(file_path):
    with open(file_path) as f:
        return f.read().split('\n')


class BoardingPass:

    def __init__(self, input):
        self.NUM_ROWS = 127
        self.NUM_COLS = 7
        self.row_code = input[:-3]
        self.column_code = input[-3:]
        self.row_number = self.calculate_row_position()
        self.column_number = self.calculate_column_position()
        self.ticket_id = self.calculate_ticket_id()

    def calculate_row_position(self):
        formatted_directions = self.row_code.replace('F', '0').replace('B', '1')
        return self.calculate_position_given_directions(formatted_directions, self.NUM_ROWS)

    def calculate_column_position(self):
        formatted_directions = self.column_code.replace('L', '0').replace('R', '1')
        return self.calculate_position_given_directions(formatted_directions, self.NUM_COLS)

    def calculate_position_given_directions(self, directions, upper_limit):
        lower, upper = 0, upper_limit
        for direction in directions:
            mid = (lower + upper) // 2
            if direction == '0':
                upper = mid
            elif direction == '1':
                lower = mid + 1
        return lower

    def calculate_ticket_id(self):
        return (self.row_number * 8) + self.column_number


def find_missing_ticket(ticket_ids):
    sorted_ids = sorted(ticket_ids)
    for i in range(len(sorted_ids) - 1):
        if sorted_ids[i] + 2 == sorted_ids[i+1]:
            return sorted_ids[i] + 1


def main():
    input = open_file('input/day-5.txt')
    boarding_passes = []
    for line in input:
        boarding_passes.append(BoardingPass(line))
    ids = [boarding_pass.ticket_id for boarding_pass in boarding_passes]

    print('Answer one is ' + str(max(ids)))  
    print('Answer two is ' + str(find_missing_ticket(ids)))

        



if __name__ == '__main__':
    main()
    