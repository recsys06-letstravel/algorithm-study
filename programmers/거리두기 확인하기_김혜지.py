# https://programmers.co.kr/learn/courses/30/lessons/81302
# 거리두기 확인하기

def solution(places):    
    answer = []

    for place in places:
        wating_room = list()
        for seats in place:
            wating_room.append([s for s in seats])
        
        social_distance = True
        for i in range(len(wating_room)):
            for j in range(len(wating_room[i])):
                if wating_room[i][j] == 'P':
                    # 한 칸 단위로 보기
                    if (i-1>=0 and wating_room[i-1][j]=='P') \
                        or (j-1>=0 and wating_room[i][j-1]=='P') \
                        or (i+1<len(wating_room) and  wating_room[i+1][j]=='P') \
                        or (j+1<len(wating_room[i]) and  wating_room[i][j+1]=='P') :
                        social_distance = False
                        break
                    # 대각선 단위로 보기
                    if (i-1>=0 and j-1>=0 and wating_room[i-1][j-1]=='P' and (wating_room[i][j-1]=='O' or wating_room[i-1][j]=='O')) \
                        or (i-1>=0 and j+1<len(wating_room[i]) and wating_room[i-1][j+1]=='P' and (wating_room[i][j+1]=='O' or wating_room[i-1][j]=='O')) \
                        or (i+1<len(wating_room) and j+1<len(wating_room[i]) and wating_room[i+1][j+1]=='P' and (wating_room[i+1][j]=='O' or wating_room[i][j+1]=='O')) \
                        or (i+1<len(wating_room) and j-1>=0 and wating_room[i+1][j-1]=='P' and (wating_room[i+1][j]=='O' or wating_room[i][j-1]=='O')) :
                        social_distance = False
                        break
                    
                    # 두 칸 단위로 보기
                    if (i-2>=0 and wating_room[i-2][j]=='P' and wating_room[i-1][j]=='O') \
                        or (j-2>=0 and wating_room[i][j-2]=='P' and wating_room[i][j-1]=='O') \
                        or (i+2<len(wating_room) and  wating_room[i+2][j]=='P'and wating_room[i+1][j]=='O') \
                        or (j+2<len(wating_room[i]) and wating_room[i][j+2]=='P' and wating_room[i][j+1]=='O') :
                        social_distance = False
                        break
                                  
            if social_distance == False : break

        answer.append(1 if social_distance==True else 0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))