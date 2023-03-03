def is_prime(number):
    if number == 2 or number == 3: # 特殊情況
        return True
    if number % 2 == 0 or number < 2: # 偶數或小於 2
        return False
    for i in range(3, int(number**0.5)+1, 2): # 從 3 到平方根，每次加 2
        if number % i == 0: # 如果有整除，就不是質數
            return False
    return True # 都沒有整除，就是質數

count = input().strip('\n') # 輸入測試次數

for i in range(int(count)): # 迴圈測試每個輸入值
    number = input().strip('\n') # 輸入一個數字
    print("Prime" if is_prime(int(number)) else "Composite") # 印出判斷結果
