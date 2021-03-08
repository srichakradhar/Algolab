"""
nums = 1 2 3 9
                                    (idx, cur_sum)
                                          0, 0
                            1, 0                          1, 1
                  2, 0                2, 2               2, 1            2, 3
          3, 0          3, 3    3, 2        3, 5    3, 1      3, 4    3, 3
      4, 0  4, 4    4, 3      4, 2        4, 5    4, 1  4,5  4, 4   4, 3


1 2 3 9

  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
1 16 14 14 .... 
1 16 12 12 12 12 ....
2 16 8  8  4  4        4  4  4  4
5 16 -2   2  2  2 
7 16 2  2 
"""

"""
X
XX
XXX
XXXX
"""
def pattern(n):
    if n == 1:
        print('X')
        return
    pattern(n-1)
    print('X' * n)

# pattern(4)

"""
X
X
XX
X
XX
XXX
X
XX
XXX
XXXX
"""
def npattern(n, i):
    if i > n: return
    pattern(i)
    npattern(n, i+1)

# npattern(4, 1)

"""
X
XX
XXX
XXXX
"""
def ipattern(n, i):
    if i > n: return
    print('X' * i)
    ipattern(n, i+1)

"""
X
XX
X
XXX
X
XX
X
XXXX
X
XX
X
XXX
X
XX
X
"""
def symmetric_pattern(n):
    if n == 1:
        print('X')
        return
    symmetric_pattern(n-1)
    print('X' * n)
    symmetric_pattern(n-1)

# symmetric_pattern(4)

"""
....X....
...XXX...
..XXXXX..
.XXXXXXX.
XXXXXXXXX
.XXXXXXX.
..XXXXX..
...XXX...
....X....
"""
def diamond(n, i):
    r = 2 * i - 1
    if i == n:
        print('X' * r)
        return
    m = n-i
    print('.' * m + 'X' * r + '.' * m)
    diamond(n, i+1)
    print('.' * m + 'X' * r + '.' * m)

# diamond(5, 1)

"""
 \   |   / 
  \  |  /  
   \ | /   
    \|/    
-----X-----
    /|\    
   / | \   
  /  |  \  
 /   |   \
"""
def kaleidoscope(n, i):
    if n == i:
        print('-' * i + 'X' + '-' * i)
        return
    m = n-i-1
    print(' '* i + '\\' + ' ' * m + '|' + ' '* m + '/' + ' ' * i)
    kaleidoscope(n, i+1)
    print(' '* i + '/' + ' ' * m + '|' + ' '* m + '\\' + ' ' * i)

# kaleidoscope(5, 1)


def hanoi(n, x, y, z):
    if n == 1:
        print(x, '->', z)
        return
    hanoi(n-1, x, z, y)
    print(x, '->', z)
    hanoi(n-1, y, z, x)

# hanoi(5)