import sys
N = int(sys.stdin.readline())
S = sys.stdin.readline()
result = ''
for char in S:
    new_char = chr(((ord(char) - ord('a') + N) % 26) + ord('a'))
    result += new_char

print(result)