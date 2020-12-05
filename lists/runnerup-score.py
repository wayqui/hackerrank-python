if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list = list(arr)
    list.sort(reverse=True)
    runnerup = list[0]
    for element in list:
        if (runnerup > element):
            runnerup = element
            break
    
    print(runnerup)
        
