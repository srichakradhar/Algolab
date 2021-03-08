"""
nums = 1 2 3 4
                                    (idx, cur_sum)
                                          0, 0
                            1, 0                          1, 1
                  2, 0                2, 2               2, 1            2, 3
          3, 0          3, 3    3, 2        3, 5    3, 1      3, 4    3, 3
      4, 0  4, 4    4, 3      4, 2        4, 5    4, 1  4,5  4, 4   4, 3
"""

def can_partition(num):
  # TODO: Write your code here
  s = sum(num)
  if s %2 == 1: return False
  d = {}
  def helper(idx, cur_sum):
    if (idx,cur_sum) in d: return d[(idx,cur_sum)]
    if idx >= len(num): 
        d[(idx,cur_sum)] = False
        return False
    if cur_sum == s//2:
        d[(idx,cur_sum)] = True
        return True
    if cur_sum > s//2: 
        d[(idx,cur_sum)] = False
        return False
    if helper(idx+1, cur_sum+num[idx]) or helper(idx+1, cur_sum): 
        d[(idx,cur_sum)] = True
    else: d[(idx,cur_sum)] = False
    return d[(idx,cur_sum)]
  return helper(0,0)

# print(can_partition([3, 3, 1]))


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

def kaledeoscope(n, i):
    m = n // 2
    if n == i:
        print('-' * m + 'X' + '-' * m)
    