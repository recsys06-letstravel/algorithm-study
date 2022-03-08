import sys

def fib_dp(n):
    if n == 1 : return 1
    elif n == 2 : return 2
    elif n == 3 : return 4
    
    fibo_array = [1, 2, 4]
    for i in range(3, n):
        num = fibo_array[i-1]+fibo_array[i-2]+fibo_array[i-3]
        fibo_array.append(num)
    return fibo_array[-1]

if __name__ == "__main__":
    answers = list()
    loop_count = int(sys.stdin.readline())
    
    for _ in range(loop_count):
        last_num = int(sys.stdin.readline())
        answers.append(fib_dp(last_num))
    
    for answer in answers:
        print(answer)

    
