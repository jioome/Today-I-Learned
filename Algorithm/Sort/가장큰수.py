def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print((''.join(numbers)))
    return numbers

solution([6, 10, 2])