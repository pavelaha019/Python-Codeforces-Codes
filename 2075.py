#Pavel Ahamed 
#ID: 221074002

import sys

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        if n % 2 == 1:
            if n <= k:
                print(1)
            else:
                rem = n - k
                even_moves = (rem + (k - 1) - 1) // (k - 1)
                print(1 + even_moves)
        else:
            moves = (n + (k - 1) - 1) // (k - 1)
            print(moves)
 
if __name__ == '__main__':
    main()