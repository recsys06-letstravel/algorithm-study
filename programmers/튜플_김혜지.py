# https://programmers.co.kr/learn/courses/30/lessons/64065?language=python
# 튜플

def solution(s):
    answer = []

    s = s[2:-2]
    s_list = list(s.split("},{"))
    s_list = [list(map(int, i.split(","))) for i in s_list]
    s_list = sorted(s_list, key=lambda x :len(x))

    for s_set in s_list:
        if len(s_set) == 1 : answer.extend(s_set)
        else:
            num = set(s_set)-set(answer)
            answer.append(num.pop())

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))