def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


square = lambda x: x * x
uppercase = lambda text: text.upper()
