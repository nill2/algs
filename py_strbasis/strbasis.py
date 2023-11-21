
s = ' '
x_=257
p=10**9+7
h = []
x = []
n=0

def prepopulate(s):
    n=len(s)-1
    h=[0]*(n+1)
    x=[0]*(n+1)
    x[0] = 1
    for i in range(1,n+1):
        h[i] = (h[i-1]*x_+ord(s[i])+1)%p
        x[i] = x[i-1]*x_
    return (h, x , n)
        

def strequal(h,x,l,a,b):
    #hash1 = (h[a+l]-h[a]*x[l])%p
    #hash2 = (h[b+l]-h[b]*x[l])%p
    result1 = (h[a+l]+h[b]*x[l])%p
    result2 = (h[b+l]+h[a]*x[l])%p
    return (result1 == result2)   

def strbasis(h,x,n):
    i = 0
    for i in range(1,n):
        if strequal(h,x,n-i,0,i):
            return i
    return n
        

def main():
    f=open("input.txt")
    s = ' ' + f.readline().strip()
    h, x, n = prepopulate(s) 
    f.close()  
    answer = str(strbasis(h, x, n))
    f=open("output.txt",'w+')
    f.write(answer)
    f.close()

if __name__ == "__main__":
    main()