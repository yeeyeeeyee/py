import sys
def is_palindrome(s: str) -> bool:
    # 判斷字串是否為迴文
    return s == s[::-1]

# 測試範例
print(is_palindrome(sys.stdin.readline())) # 輸出 True
