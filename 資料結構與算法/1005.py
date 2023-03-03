import sys

def factor(number):
    total = 0
    for i in range(1, number//2 + 1): #可以將 range(1, number) 改為 range(1, number//2 + 1)，原因是一個數的因數最大只可能是它的一半。
        if number % i == 0:
            total += i
    
    test_total = 0
    for i in range(1, total//2 + 1):
        if total % i == 0:
            test_total += i 

    if test_total == number:
        return total
    else:
        return "QQ"
  
for line in sys.stdin:
    start = int(line.strip())
    if start == 0:
        break
    
    print(factor(start))
