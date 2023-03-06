import sys
def calculate_expression(a: int, operator: str, b: int) -> int:
    # 根據運算符號進行計算
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a // b

# 測試範例
temp=sys.stdin.readline().split()
print(calculate_expression(int(temp[0]), temp[1], int(temp[2]))) # 輸出 12