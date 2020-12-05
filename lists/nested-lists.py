if __name__ == '__main__':
    map = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr = [name, score]
        map.append(arr)
    
    # Obtain a list with all the scores
    notas = []
    for list in map:
        notas.append(list[1])
    
    # Obtain the runner up score
    notas.sort()
    runnerup = notas[0]
    for element in notas:
        if (runnerup < element):
            runnerup = element
            break
    
    # determine the students with the 2nd lowest score
    students = []
    for list in map:
        if list[1] == runnerup:
            students.append(list[0])
    
    students.sort()

    print(*students, sep="\n")
