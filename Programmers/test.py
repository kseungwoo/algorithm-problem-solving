def pythagorean(x, y):
    return round((x ** 2 + y ** 2) ** 0.5, 2)


if __name__ == '__main__':
    a = float(input().strip())
    b = float(input().strip())
    print(pythagorean(a, b))
