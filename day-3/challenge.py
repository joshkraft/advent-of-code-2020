def open_file(file_path):
    with open(file_path) as f:
        return f.read().splitlines()


class Terrain():
    def __init__(self, raw_string):
        self.points = []
        self.TREE = '#'
        self.height = len(raw_string)

        for y, row in enumerate(raw_string):
            self.width = len(row)
            for x, col in enumerate(row):
                if col == self.TREE:
                    self.points.append([x, y])

    def count_trees_in_slope_path(self, right_step, down_step):
        count_trees = 0
        x_idx = 0
        y_idx = 0
        while y_idx <= self.height:
            if [x_idx, y_idx] in self.points:
                count_trees += 1
            x_idx = (x_idx + right_step) % self.width
            y_idx += down_step
        
        return count_trees

def main():
    input_string = open_file('input/day-3.txt')
    terrain = Terrain(input_string)
    answer_one = terrain.count_trees_in_slope_path(3, 1)
    print('Answer one is ' + str(answer_one))

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    answer_two = 1
    for slope in slopes:
        answer_two *= terrain.count_trees_in_slope_path(slope[0], slope[1])
    print('Answer two is ' + str(answer_two))

if __name__ == "__main__":
    main()