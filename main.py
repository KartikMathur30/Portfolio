def integertobase(num,B):
    sum =""
        
    while(num != 0):
        rem = num % B
        sum = sum + str(rem)
        num = num//B
    return int(sum[::-1])
def basetointerger(k,B):
    sum = 0
    i=0
    while(k != 0):
        rem = k%10
        sum = sum + (rem*(B**i))
        k = k//10
        i += 1
    return sum
def solve(A, B):
    lit = []
    flag = 0
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            x = integertobase(A[i],B)
            y = integertobase(A[j],B)
            k = x+y
            flag += 1
            bti = basetointerger(k,B)
           # lit.append(bti)
    lit.sort()
    return lit[flag - 1]

if __name__ == '__main__':
    a = list(map(int, input().strip().split()))
    b = int(input())
    l = solve(a,b)
    print(l)
