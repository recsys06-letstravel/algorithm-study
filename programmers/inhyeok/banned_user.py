import itertools


def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] == '*':
                continue
            elif banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_permutation = list(itertools.combinations(user_id, len(banned_id)))
    banned_Set = []
    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            print(users)
            users = set(users)
            print("set:", users)
            if users not in banned_Set:
                banned_Set.append(users)

    print(len(banned_Set))
    return len(banned_Set)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])