s = ' '
x_=10**8+7
p=10**9+7
h = []
x = []
n=0


#def equalstr(h,x_,l,a,b):
    #hash1 = (h[a+l]-h[a]*x_[l])%p
    #hash2 = (h[b+l]-h[b]*x_[l])%p

def main():
    f=open("input.txt")
    s = ' ' + f.readline().strip()
    n=len(s)-1
    h=[0]*(n+1)
    x=[0]*(n+1)
    x[0] = 1
    for i in range(1,n+1):
        h[i] = (h[i-1]*x_+ord(s[i])+1)%p
        x[i] = x[i-1]*x_
    q=int(f.readline())
    answer = ''
    for i in range(q):
        content = f.readline().strip()
        query_list = list(map(int, content.split()))
        l = query_list[0]
        a = query_list[1]
        b = query_list[2]
        result1 = (h[a+l]+h[b]*x[l])%p
        result2 = (h[b+l]+h[a]*x[l])%p
        if result1 == result2 : 
            answer = answer + 'yes\n'
        else:
            answer = answer + 'no\n' 
    f.close()
    f=open("output.txt",'w+')
    f.write(answer.rstrip())
    f.close()

if __name__ == "__main__":
    main()