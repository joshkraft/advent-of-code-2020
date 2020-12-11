def get_input():
    with open("input/day-10.txt", "r") as f:
        return [int(n) for n in f.read().split('\n')]


def process_input(input):
    data = input[:]
    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    return data


def get_joltage_diffs(data):    
    diffs = {}

    for i, j in zip(data, data[1:]):
        diff = j - i
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1

    return diffs
    

def multiply_diffs(diffs):
    product = 1
    for diff in diffs.values():
        product *= diff
    return product
    

def count_all_valid_combinations(data):
    output = data[-1]
    num_ways = [0] * (output + 1)
    num_ways[0] = 1
    
    # This is no bueno... refactor some day -__-
    if 1 in data:
        num_ways[1] = 1

    if 2 in data and 1 in data:
        num_ways[2] = 2

    elif 2 in data:
        num_ways[2] = 1

    for n in range(3, output + 1):
        if n not in data:
            continue

        num_ways[n] = num_ways[n-3] + num_ways[n-2] + num_ways[n-1]

    return num_ways[output]
    

def main():
    input = get_input()
    data = process_input(input)
    diffs = get_joltage_diffs(data)
    product_of_diffs = multiply_diffs(diffs)
    print('Answer one is ' + str(product_of_diffs))
    print('Answer two is ' + str(count_all_valid_combinations(data)))
      

if __name__ == "__main__":
    main()