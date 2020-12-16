def solution(number):
    solutions = []
    for num in range(0, number):
        if num % 3 == 0:
            solutions.append(num)
        elif num % 5 == 0:
            solutions.append(num)
    return sum(solutions)
