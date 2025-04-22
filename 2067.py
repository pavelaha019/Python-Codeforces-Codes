#Pavel Ahamed 
#ID 221074002

import sys
input = sys.stdin.readline
 
def solve():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        d = y - x
        if d <= 1 and (d - 1) % 9 == 0:
            print("YES")
        else:
            print("NO")
 
if __name__ == "__main__":
    solve()