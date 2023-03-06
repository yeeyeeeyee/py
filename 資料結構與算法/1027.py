import sys
# 輸入信用卡號
card_number = sys.stdin.readline().replace('-', '')

# 計算奇數位加總
odd_sum = 0
for i in range(0, 15, 2):
    digit = int(card_number[i])
    digit *= 2
    if digit >= 10:
        digit -= 9
    odd_sum += digit

# 計算偶數位加總
even_sum = sum([int(card_number[i]) for i in range(1, 15, 2)])

# 計算檢查碼
total_sum = odd_sum + even_sum
check_digit = (10 - total_sum % 10) % 10
# 判斷信用卡號是否合法並輸出結果
if check_digit == int(card_number[15]):
    if card_number[0] == '4':
        print("VISA")
    elif card_number[0] == '5':
        print("MASTER_CARD")
else:
    print("INVALID")