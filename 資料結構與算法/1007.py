import sys
M = int(sys.stdin.readline())
max_score = -1
winners = []
for i in range(M):
    name, score = sys.stdin.readline().split()
    score = int(score)
    if score > max_score:
        max_score = score
        winners = [name]
    elif score == max_score:
        winners.append(name)
for winner in winners:
    print(winner)

    