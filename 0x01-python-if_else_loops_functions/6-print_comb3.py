for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        print(f"{digit1:01d}{digit2:1d}", end=", " if digit1 < 9 or digit2 < 9 else "\n")

