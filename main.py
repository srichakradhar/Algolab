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
  if s % 2 == 1: return False
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


from topics.recursion_codingbat import groupSum5
print(groupSum5(0, [3, 5, 1], 4))