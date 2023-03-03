import sys
prime=int(sys.stdin.readline().strip('\n'))
prime2=int(sys.stdin.readline())
is_high=max(prime,prime2)
max_vaule=is_high*2
print(max_vaule)
print(max_vaule-(prime+prime2))

