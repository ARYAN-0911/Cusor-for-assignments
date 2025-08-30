def fizzbuzz_solution(test_cases):
    for num in test_cases:
        for i in range(1, num + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

# Read input and call function
try:
    t = int(input())
    test_cases = []
    for _ in range(t):
        test_cases.append(int(input()))
    
    fizzbuzz_solution(test_cases)
except EOFError:
    pass