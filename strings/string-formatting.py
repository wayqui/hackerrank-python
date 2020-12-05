def print_formatted(number):
    i = 1
    value = len(format(number, 'b'))
    while (i<=number):
        print(str(i).rjust(value, " ") + " " + format(i, 'o').rjust(value, " ") + " " + format(i, 'X').rjust(value, " ") + " " + format(i, 'b').rjust(value, " "))
        i+=1

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)