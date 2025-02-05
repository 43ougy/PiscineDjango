def numbers():
    file = open("numbers.txt", "r").read().split(",")
    for line in file:
        print(line)

if __name__ == '__main__':
    numbers()