for case in range(int(input())):
    n = int(input())
    people = list(map(int, input().split(' ')))
    day = 0
    total_people = 1
    while total_people<n:
        day+=1
        total_people+=sum(people[:total_people])
    else:
         print(day)