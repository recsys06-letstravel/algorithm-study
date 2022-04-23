# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD
# 최대 상금
import copy 

T = int(input())

for test_case in range(1, T + 1):
    input_numbers, change_count = input().split(" ")    
    next_numbers = list()
    current_numbers = list()
    graph = dict()

    #input_numbers = [int(i) for i in input_numbers]
    change_count = int(change_count)

    current_numbers.append(input_numbers)

    for _ in range(change_count):
        for current_number in current_numbers :
            if current_number not in graph.keys():
                graph[current_number] = list()
                for i in range(len(current_number)-1):
                    for j in range(i+1, len(current_number)):
                        change_numebr = copy.deepcopy(current_number)
                        change_numebr = [n for n in current_number]

                        tmp = change_numebr[i]
                        change_numebr[i] = change_numebr[j]
                        change_numebr[j] = tmp

                        change_numebr = "".join(map(str, change_numebr))
                        graph[current_number].append(change_numebr)

            next_numbers.extend(graph[current_number])
        
        current_numbers = copy.deepcopy(next_numbers)
        current_numbers = list(set(current_numbers))
        next_numbers = list()

    print(f"#{test_case} {max(current_numbers)}")


    

    




