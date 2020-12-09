class Instruction():
    def __init__(self, line):
        operation, argument = line.split()
        self.operation = operation
        self.argument = int(argument)


class Program():
    def __init__(self, instructions):
        self.instructions = instructions
        self.accumulator_score = 0
        self.idx = 0

    def execute_next_instruction(self):
        operation = self.instructions[self.idx].operation
        argument = self.instructions[self.idx].argument

        if operation == 'acc':
            self.accumulator_score += argument
            self.idx += 1
        elif operation == 'jmp':
            self.idx += argument
        elif operation == 'nop':
            self.idx += 1
        else:
            raise ValueError('Unknown operation: ' + str(operation))

    def calculate_score_at_first_repeat(self):
        executed_lines = set()
        while self.idx not in executed_lines:
            executed_lines.add(self.idx)
            self.execute_next_instruction()        

    def determine_if_infinite_loop(self):
        executed_lines = set()

        while self.idx not in executed_lines:
            if self.idx == len(self.instructions):
                return True

            executed_lines.add(self.idx)
            self.execute_next_instruction()
        
        return False


def find_terminating_instruction(instructions):
    for i, instruction in enumerate(instructions):
        instructions_clone = instructions[:]
        operation = instruction.operation
        argument = instruction.argument

        if operation == 'nop':
            instructions_clone[i] = Instruction('jmp ' + str(argument))
        elif operation == 'jmp':
            instructions_clone[i] = Instruction('nop ' + str(argument))
        else:
            continue

        program = Program(instructions_clone)

        if program.determine_if_infinite_loop():
            return program.accumulator_score
    
    raise RuntimeError("Never terminated")


def get_input():
    with open("input/day-8.txt", "r") as f:
        return f.read().split('\n')


def main():
    input = get_input()
    instructions = [Instruction(line) for line in input]
    program = Program(instructions)
    program.calculate_score_at_first_repeat()
    print('Answer one is ' + str(program.accumulator_score))
    print('Answer two is ' + str(find_terminating_instruction(instructions)))


if __name__ == "__main__":
    main()