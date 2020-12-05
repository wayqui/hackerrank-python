def count_substring(string, sub_string):
    pos = 0
    number = 0
    while (pos < len(string)):
        pos = string.find(sub_string, pos)
        if (pos != -1):
            number+=1
            pos+=1
        else:
            pos = len(string)

    return number

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)