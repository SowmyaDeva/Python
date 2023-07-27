for x in range(5):
    for y in range(5):
        print(f"({x}, {y})")


numbers = [1, 1, 1, 1, 4]
for x in numbers:
    output = ''
    for count in range(x):
        output += 'x'
    print(output)