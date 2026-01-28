def fibonacci(limit):
    a, b = 0, 1
    count = 0

    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

def custom_range(start, end, step):
    current = start

    while current < end:
        yield current
        current += step

if __name__ == "__main__":
    print("Fibonacci Generator Output")
    for num in fibonacci(10):
        print(num)
    print("\nCustom Range Generator Output")
    for num in custom_range(1, 15, 3):
        print(num)
