N = int(input())
def sol(num, type):
    if num==0 or num==N+1: return
    if type == 'UP':
        print(num, end = " ")
        sol(num+1, type)
    else:
        print(num, end = " ")
        sol(num-1, type)

sol(N,"DOWN")
sol(1,"UP")