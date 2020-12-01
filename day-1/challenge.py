import time


with open('input.txt') as f:
    input = [int(i) for i in f.read().splitlines()]


def find_combination_of_2(input, goal=2020):
    gaps = {goal - num for num in input}
    for num in input:
        if num in gaps:
            return num * (goal-num)


def find_combination_of_3(input, goal=2020):
    for i in input:
        for j in input:
            for k in input:
                if i + j + k == 2020:
                    return i * j * k


def find_combination_of_3_fancy(input, goal=2020):
    input.sort()
    for i, a in enumerate(input):
        for j, b in enumerate(input[i+1:-1]):
            for c in input[j+1:]:
                if a + b + c == goal:
                    return a * b * c

def main():
    tic = time.perf_counter()
    assert find_combination_of_2(input) == 319531
    toc = time.perf_counter()
    print(f"find_combination_of_2 took {toc - tic:0.4f} seconds")

    tic = time.perf_counter()
    assert find_combination_of_3(input) == 244300320
    toc = time.perf_counter()
    print(f"find_combination_of_3 took {toc - tic:0.4f} seconds")

    tic = time.perf_counter()
    assert find_combination_of_3_fancy(input) == 244300320
    toc = time.perf_counter()
    print(f"find_combination_of_3_fancy took {toc - tic:0.4f} seconds")

if __name__ == "__main__":
    main()