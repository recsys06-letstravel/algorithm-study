import sys

#N=113
#In=list('(9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2)*4*7+4*3*8*2*6+(7*8*4*5)+3+7+(2+6+5+1+7+6+7*3*(6+2)+6+6)*2+4+2*2+4*9*3)')
#In='(4+(2+3)+(4+5))+3'


answer=0
def CC(x,y):
    while y:
        if '*' in y:
            step=y.index('*')
            y.pop(step)
            x.insert(step,int(x.pop(step))*int(x.pop(step)))
        elif '+' in y:
            step=y.index('+')
            y.pop(step)
            x.insert(step,int(x.pop(step))+int(x.pop(step)))
    return x[0]
             
def Div(sen):
    a=list(sen)
    b=''
    c=''
    d=[]
    e=[]
    start=0
    finish=0
    while a:
        b=a.pop(0)
        if b=='+' or b=='*':
            e.append(b)
        elif b=='(':
            c+=b
            start+=1
            while True:
                ran=a.pop(0)
                c+=ran
                if ran=='(':
                    start+=1
                elif ran==')':
                    finish+=1
                if (start==finish) or (')' not in a) :
                    start=0
                    finish=0
                    break
            c=c[1:-1]
            d.append(c)
            c=''
        else:
            d.append(b)
    for f in range(len(d)):
        if '+' in d[f]:
            d[f]=Div(d[f])
        elif '*' in d[f]:
            d[f]=Div(d[f])
    g=CC(d,e)
    return g
 
 
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    In=input()
    answer=Div(In)
    print(f'#{test_case}',answer)
    
        
