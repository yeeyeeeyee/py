import sys
def main(pin,ans=0):
    
    b=format(pin,"b")
    
    #print(type(b))
    for i in range(len(b)):
        if b[i]=="1":
            ans+=1
        #print(i)
    print(ans)
    return ans

pin=sys.stdin.readline()
main(int(pin))