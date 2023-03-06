import sys
def calculate_life_number(year: int, month: int, day: int) -> int:
    # 將年、月、日轉換為字串並連接起來
    date_str = str(year) + str(month) + str(day)
    
    # 初始化生命靈數
    life_number = 0
    
    # 計算生命靈數
    while len(date_str) > 1:
        life_number = sum(int(digit) for digit in date_str)
        date_str = str(life_number)
    
    return life_number

# 測試範例
temp=sys.stdin.readline().split()
print(calculate_life_number(temp[0], temp[1], temp[2])) # 輸出 2