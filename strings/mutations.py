def mutate_string(string, position, character):
    # Primera forma
    l = list(string)
    l[position] = character
    newString = ''.join(l)
    # Segunda forma
    newString = string[:position] + character + string[position+1:]
    return newString

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)