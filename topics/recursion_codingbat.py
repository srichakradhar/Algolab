"""
Given a string and a non-empty substring sub, compute recursively if at least n copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.

public boolean strCopies(String str, String sub, int n) {
  int k = str.length();
  int l = sub.length();
  if(k < l) return n <= 0;
  if(n == 0) return true;
  return strCopies(str.substring(1), sub, str.substring(0, l).equals(sub) ? n - 1 : n);
}

strCopies("catcowcat", "cat", 2) → true
strCopies("catcowcat", "cow", 2) → false
strCopies("catcowcat", "cow", 1) → true
strCopies("iiijjj", "i", 3) → true
strCopies("iiijjj", "i", 4) → false
strCopies("iiijjj", "ii", 2) → true
strCopies("iiijjj", "ii", 3) → false
strCopies("iiijjj", "x", 3) → false
strCopies("iiijjj", "x", 0) → true
strCopies("iiiiij", "iii", 3) → true
strCopies("iiiiij", "iii", 4) → false
strCopies("ijiiiiij", "iiii", 2) → true
strCopies("ijiiiiij", "iiii", 3) → false
strCopies("dogcatdogcat", "dog", 2) → true
"""
def strCopies(string, sub, n):
    k = len(string);
    l = len(sub);
    if k < l:
        return n <= 0
    if n == 0:
        return True
    return strCopies(string[1:], sub, n - 1 if string[: l] == sub else n)

"""
Given a string and a non-empty substring sub, compute recursively the largest substring which starts and ends with sub and return its length.

public int strDist(String str, String sub) {
  int k = str.length();
  int l = sub.length();
  if(k < l) return 0;
  if(str.substring(0, l).equals(sub) && str.substring(k-l, k).equals(sub)) return k;
  int right = strDist(str.substring(1), sub);
  int left = strDist(str.substring(0, k-1), sub);
  return left > right ? left : right;
}

strDist("catcowcat", "cat") → 9
strDist("catcowcat", "cow") → 3
strDist("cccatcowcatxx", "cat") → 9
strDist("abccatcowcatcatxyz", "cat") → 12
strDist("xyx", "x") → 3
strDist("xyx", "y") → 1
strDist("xyx", "z") → 0
strDist("z", "z") → 1
strDist("x", "z") → 0
strDist("", "z") → 0
strDist("hiHellohihihi", "hi") → 13
strDist("hiHellohihihi", "hih") → 5
strDist("hiHellohihihi", "o") → 1
strDist("hiHellohihihi", "ll") → 2
"""
def strDist(string, sub):
    k = len(string);
    l = len(sub);
    if k < l: return 0
    # print(string, k, l, string[:l], string[k-l:], sub)
    if string[:l] == sub and string[k-l:] == sub: return k
    right = strDist(string[1:], sub)
    left = strDist(string[:k-1], sub)
    return max(left, right)

def istrDist(string, sub):
    l, r = 0, len(string)
    k = len(sub)
    i = 0
    while r - l >= k:
        if string[l:l+k] == sub and string[r-k:r] == sub: return r-l
        elif i % 2 == 0:
            l += 1
        else:
            r -= 1
        i += 1
    return 0

"""
Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the string, without the sub strings overlapping.

public int strCount(String str, String sub) {
  int k = str.length();
  int l = sub.length();
  if(k < l) return 0;
  return str.substring(0, l).equals(sub) ? 1 + strCount(str.substring(l), sub) : strCount(str.substring(1), sub);
}

strCount("catcowcat", "cat") → 2
strCount("catcowcat", "cow") → 1
strCount("catcowcat", "dog") → 0
strCount("cacatcowcat", "cat") → 2
strCount("xyx", "x") → 2
strCount("iiiijj", "i") → 4
strCount("iiiijj", "ii") → 2
strCount("iiiijj", "iii") → 1
strCount("iiiijj", "j") → 2
strCount("iiiijj", "jj") → 1
strCount("aaabababab", "ab") → 4
strCount("aaabababab", "aa") → 1
strCount("aaabababab", "a") → 6	6
strCount("aaabababab", "b") → 4
"""
def strCount(string, sub):
    k = len(string);
    l = len(sub);
    if k < l: return 0
    return 1 + strCount(string[l:], sub) if string[:l] == sub else strCount(string[1:], sub);

"""
Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.

public boolean nestParen(String str) {
  int l = str.length();
  if(l == 0) return true;
  if(l < 0) return false;
  return str.charAt(0) == '(' && str.charAt(l-1) == ')' ? nestParen(str.substring(1, l-1)) : false;
}

nestParen("(())") → true
nestParen("((()))") → true
nestParen("(((x))") → false
nestParen("((())") → false
nestParen("((()()") → false
nestParen("()") → true
nestParen("") → true
nestParen("(yy)") → false
nestParen("(())") → true
nestParen("(((y))") → false
nestParen("((y)))") → false
nestParen("((()))") → true
nestParen("(())))") → false
nestParen("((yy())))") → false
nestParen("(((())))") → true
"""

def nestParen(string):
  l = len(string)
  if l == 0: return True;
  if l < 0: return False;
  return nestParen(string[1: l-1]) if string[0] == '(' and string[l-1] == ')' else False


"""
Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)".

public String parenBit(String str) {
  int l = str.length();
  if(l < 2) return "";
  if(str.charAt(0) == '(' && str.charAt(l-1) == ')') return str;
  else if(str.charAt(0) == '(') return parenBit(str.substring(0, l-1));
  else if(str.charAt(l-1) == ')') return parenBit(str.substring(1, l));
  else return parenBit(str.substring(1, l-1));
}

parenBit("xyz(abc)123") → "(abc)"
parenBit("x(hello)") → "(hello)"
parenBit("(xy)1") → "(xy)"
parenBit("not really (possible)") → "(possible)"
parenBit("(abc)") → "(abc)"
parenBit("(abc)xyz") → "(abc)"
parenBit("(abc)x") → "(abc)"
parenBit("(x)") → "(x)"
parenBit("()") → "()"
parenBit("res (ipsa) loquitor") → "(ipsa)"
parenBit("hello(not really)there") → "(not really)"
parenBit("ab(ab)ab") → "(ab)"
"""
def parenBit(string):
  l = len(string)
  if l < 2: return ""
  if string[0] == '(' and string[l-1] == ')': return string
  elif string[0] == '(': return parenBit(string[:l-1])
  elif string[l-1] == ')': return parenBit(string[1:])
  else: return parenBit(string[1: l-1])

"""
Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not count "hi" that have an 'x' immedately before them.

public int countHi2(String str) {
  int l = str.length();
  if(l < 2) return 0;
  if(str.charAt(0) == 'x'){
    return countHi2(str.substring(str.charAt(1) == 'x' ? 1 : 2));
  }
  else if(str.substring(0, 2).equals("hi")) return 1 + countHi2(str.substring(2));
  else return countHi2(str.substring(1));
}

countHi2("ahixhi") → 1
countHi2("ahibhi") → 2
countHi2("xhixhi") → 0
countHi2("hixhi") → 1
countHi2("hixhhi") → 2
countHi2("hihihi") → 3
countHi2("hihihix") → 3
countHi2("xhihihix") → 2
countHi2("xxhi") → 0
countHi2("hixxhi") → 1
countHi2("hi") → 1
countHi2("xxxx") → 0
countHi2("h") → 0
countHi2("x") → 0
countHi2("") → 0
countHi2("Hellohi") → 1
"""
def countHi2(string):
    l = len(string)
    if l < 2: return 0
    if string[0] == 'x': return countHi2(string[1 if string[1] == 'x' else  2:])
    elif string[: 2] == "hi": return 1 + countHi2(string[2:])
    else: return countHi2(string[1:])

"""
Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a single char. So "yyzzza" yields "yza".

public String stringClean(String str) {
  int l = str.length();
  if(l == 1) return str;
  if(str.charAt(0) == str.charAt(1)) return stringClean(str.substring(1));
  else return str.charAt(0) + stringClean(str.substring(1));
}

stringClean("yyzzza") → "yza"
stringClean("abbbcdd") → "abcd"
stringClean("Hello") → "Helo"
stringClean("XXabcYY") → "XabcY"
stringClean("112ab445") → "12ab45"
stringClean("Hello Bookkeeper") → "Helo Bokeper"
"""
def stringClean(string):
  l = len(string)
  if l == 1: return string
  if string[0] == string[1]: return stringClean(string[1:])
  else: return string[0] + stringClean(string[1:]);

"""
Given a string, compute recursively (no loops) the number of "11" substrings in the string. The "11" substrings should not overlap.

public int count11(String str) {
  int l = str.length();
  if(l < 2) return 0;
  if(str.substring(0, 2).equals("11")) return 1 + count11(str.substring(2));
  else return count11(str.substring(1));
}

count11("11abc11") → 2
count11("abc11x11x11") → 3
count11("111") → 1
count11("1111") → 2
count11("1") → 0
count11("") → 0
count11("hi") → 0
count11("11x111x1111") → 4
count11("1x111") → 1
count11("1Hello1") → 0
count11("Hello") → 0
"""
def count11(string):
    l = len(string)
    if l < 2: return 0
    elif string[: 2] == "11": return 1 + count11(string[2:])
    else: return count11(string[1:])

"""
Count recursively the total number of "abc" and "aba" substrings that appear in the given string.

public int countAbc(String str) {
  int l = str.length();
  if(l < 3) return 0;
  if(str.substring(0, 3).equals("abc") || str.substring(0, 3).equals("aba")) return 1 + countAbc(str.substring(1));
  else return countAbc(str.substring(1));
}

countAbc("abc") → 1
countAbc("abcxxabc") → 2
countAbc("abaxxaba") → 2
countAbc("ababc") → 2
countAbc("abxbc") → 0
countAbc("aaabc") → 1
countAbc("hello") → 0
countAbc("") → 0
countAbc("ab") → 0
countAbc("aba") → 1
countAbc("aca") → 0
countAbc("aaa") → 0
"""
def countAbc(string):
    l = len(string)
    if l < 3: return 0
    elif string[: 3] in ["abc", "aba"]: return 1 + countAbc(string[1:])
    else: return countAbc(string[1:])

"""
We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the given string.

public int countPairs(String str) {
  int l = str.length();
  if(l < 3) return 0;
  if(str.charAt(0) == str.charAt(2)) return 1 + countPairs(str.substring(1));
  else return countPairs(str.substring(1));
}

countPairs("axa") → 1
countPairs("axax") → 2
countPairs("axbx") → 1
countPairs("hi") → 0
countPairs("hihih") → 3
countPairs("ihihhh") → 3
countPairs("ihjxhh") → 0
countPairs("") → 0
countPairs("a") → 0
countPairs("aa") → 0
countPairs("aaa") → 1
"""
def countPairs(string):
    l = len(string)
    if l < 3: return 0
    elif string[0] == string[2]: return 1 + countPairs(string[1:])
    else: return countPairs(string[1:])

"""
Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of the string.

public String endX(String str) {
  if(str.length() <= 1) return str;
  if(str.charAt(0) == 'x') return endX(str.substring(1)) + "x";
  else return str.charAt(0) + endX(str.substring(1));
}

endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("xhixhix") → "hihixxx"
endX("hiy") → "hiy"
endX("h") → "h"
endX("x") → "x"
endX("xx") → "xx"
endX("") → ""
endX("bxx") → "bxx"
endX("bxax") → "baxx"
endX("axaxax") → "aaaxxx"
endX("xxhxi") → "hixxx"
"""
def endX(string):
    if len(string) <= 1: return string
    elif string[0] == 'x': return endX(string[1:]) + "x"
    else: return string[0] + endX(string[1:])

"""
Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

public String pairStar(String str) {
  if(str.length() < 2) return str;
  char ch = str.charAt(0);
  if(ch == str.charAt(1)) return ch + "*" + pairStar(str.substring(1));
  else return ch + pairStar(str.substring(1));
}

pairStar("hello") → "hel*lo"
pairStar("xxyy") → "x*xy*y"
pairStar("aaaa") → "a*a*a*a"
pairStar("aaab") → "a*a*ab"
pairStar("aa") → "a*a"
pairStar("a") → "a"
pairStar("") → ""
pairStar("noadjacent") → "noadjacent"
pairStar("abba") → "ab*ba"
pairStar("abbba") → "ab*b*ba"
"""
def pairStar(string):
    if len(string) < 2: return string
    ch = string[0]
    if ch == string[1]: return ch + '*' + pairStar(string[1:])
    else: return ch + pairStar(string[1:])

"""
Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".

public String allStar(String str) {
  if(str.length() < 2) return str;
  return str.charAt(0) + "*" + allStar(str.substring(1));
}
	
allStar("hello") → "h*e*l*l*o"
allStar("abc") → "a*b*c"
allStar("ab") → "a*b"
allStar("a") → "a"
allStar("") → ""
allStar("3.14") → "3*.*1*4"
allStar("Chocolate") → "C*h*o*c*o*l*a*t*e"
allStar("1234") → "1*2*3*4"
"""
def allStar(string):
    if len(string) < 2: return string
    return string[0] + '*' + allStar(string[1:])

"""
Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

public boolean array220(int[] nums, int index) {
  if(index >= nums.length - 1) return false;
  return nums[index] * 10 == nums[index + 1] ? true : array220(nums, index + 1);
}

array220([1, 2, 20], 0) → true
array220([3, 30], 0) → true
array220([3], 0) → false
array220([], 0) → false
array220([3, 3, 30, 4], 0) → true
array220([2, 19, 4], 0) → false
array220([20, 2, 21], 0) → false
array220([20, 2, 21, 210], 0) → true
array220([2, 200, 2000], 0) → true
array220([0, 0], 0) → true
array220([1, 2, 3, 4, 5, 6], 0) → false
array220([1, 2, 3, 4, 5, 50, 6], 0) → true
array220([1, 2, 3, 4, 5, 51, 6], 0) → false
array220([1, 2, 3, 4, 4, 50, 500, 6], 0) → true
"""
def array220(nums, index):
    if index >= len(nums) - 1: return False
    return True if nums[index] * 10 == nums[index + 1] else array220(nums, index + 1)

"""
Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

public int array11(int[] nums, int index) {
  if(index > nums.length - 1) return 0;
  return (nums[index] == 11 ? 1 : 0) + array11(nums, index + 1);
}

array11([1, 2, 11], 0) → 1
array11([11, 11], 0) → 2
array11([1, 2, 3, 4], 0) → 0
array11([1, 11, 3, 11, 11], 0) → 3
array11([11], 0) → 1
array11([1], 0) → 0
array11([], 0) → 0
array11([11, 2, 3, 4, 11, 5], 0) → 2
array11([11, 5, 11], 0) → 2
"""
def array11(nums, index):
    if index > len(nums) - 1: return 0
    return array11(nums, index + 1) + (1 if nums[index] == 11 else 0)

"""
Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

public boolean array6(int[] nums, int index) {
  if(index > nums.length - 1) return false;
  return nums[index] == 6 ? true : array6(nums, index + 1);
}

array6([1, 6, 4], 0) → true
array6([1, 4], 0) → false
array6([6], 0) → true
array6([], 0) → false
array6([6, 2, 2], 0) → true
array6([2, 5], 0) → false
array6([1, 9, 4, 6, 6], 0) → true
array6([2, 5, 6], 0) → true
"""
def array6(nums, index):
    if index > len(nums) - 1: return False
    return True if nums[index] == 6 else array6(nums, index + 1)

"""
Given a string, compute recursively a new string where all the 'x' chars have been removed.

public String noX(String str) {
  if(str.length() < 1) return str;
  char ch = str.charAt(0);
  return (ch == 'x' ? "" : ch) + noX(str.substring(1));
}

noX("xaxb") → "ab"
noX("abc") → "abc"
noX("xx") → ""
noX("") → ""
noX("axxbxx") → "ab"
noX("Hellox") → "Hello"
"""
def noX(string):
    if len(string) < 1: return string
    ch = string[0];
    return ("" if ch == 'x' else ch) + noX(string[1:]);

"""
+++++++ skipped a few easier ones in Recursion-1 ++++++

Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target? This is a classic backtracking recursion problem. Once you understand the recursive backtracking strategy in this problem, you can use the same pattern for many problems to search a space of choices. Rather than looking at the whole array, our convention is to consider the part of the array starting at index start and continuing to the end of the array. The caller can specify the whole array simply by passing start as 0. No loops are needed -- the recursive calls progress down the array.

public boolean groupSum(int start, int[] nums, int target) {
  if(start >= nums.length) return target == 0;
  if(target < 0) return false;
  boolean with = groupSum(start + 1, nums, target - nums[start]);
  boolean without = groupSum(start + 1, nums, target);
  return with || without;
}

groupSum(0, [2, 4, 8], 10) → true
groupSum(0, [2, 4, 8], 14) → true
groupSum(0, [2, 4, 8], 9) → false	
groupSum(0, [2, 4, 8], 8) → true
groupSum(1, [2, 4, 8], 8) → true
groupSum(1, [2, 4, 8], 2) → false	
groupSum(0, [1], 1) → true
groupSum(0, [9], 1) → false	
groupSum(1, [9], 0) → true
groupSum(0, [], 0) → true
groupSum(0, [10, 2, 2, 5], 17) → true
groupSum(0, [10, 2, 2, 5], 15) → true
groupSum(0, [10, 2, 2, 5], 9) → true
"""
def groupSum(start, nums, target):
    if start >= len(nums): return target == 0
    if target < 0: return False
    with_ = groupSum(start + 1, nums, target - nums[start]);
    without = groupSum(start + 1, nums, target);
    return with_ or without


"""
Given an array of ints, is it possible to choose a group of some of the ints, beginning at the start index, such that the group sums to the given target? However, with the additional constraint that all 6's must be chosen. (No loops needed.)

public boolean groupSum6(int start, int[] nums, int target) {
  if(start >= nums.length) return target == 0;
  if(target < 0) return false;
  if(nums[start] == 6) return groupSum6(start + 1, nums, target - nums[start]);
  boolean with = groupSum6(start + 1, nums, target - nums[start]);
  boolean without = groupSum6(start + 1, nums, target);
  return with || without;
}

groupSum6(0, [5, 6, 2], 8) → true
groupSum6(0, [5, 6, 2], 9) → false
groupSum6(0, [5, 6, 2], 7) → false
groupSum6(0, [1], 1) → true
groupSum6(0, [9], 1) → false
groupSum6(0, [], 0) → true
groupSum6(0, [3, 2, 4, 6], 8) → true
groupSum6(0, [6, 2, 4, 3], 8) → true
groupSum6(0, [5, 2, 4, 6], 9) → false
groupSum6(0, [6, 2, 4, 5], 9) → false
groupSum6(0, [3, 2, 4, 6], 3) → false
groupSum6(0, [1, 6, 2, 6, 4], 12) → true
groupSum6(0, [1, 6, 2, 6, 4], 13) → true
groupSum6(0, [1, 6, 2, 6, 4], 4) → false
groupSum6(0, [1, 6, 2, 6, 4], 9) → false
groupSum6(0, [1, 6, 2, 6, 5], 14) → true
groupSum6(0, [1, 6, 2, 6, 5], 15) → true
groupSum6(0, [1, 6, 2, 6, 5], 16) → false
"""
def groupSum6(start, nums, target):
    if start >= len(nums): return target == 0
    if target < 0: return False
    if nums[start] == 6: return groupSum6(start + 1, nums, target - nums[start])
    with_ = groupSum6(start + 1, nums, target - nums[start]);
    without = groupSum6(start + 1, nums, target);
    return with_ or without

"""
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with this additional constraint: If a value in the array is chosen to be in the group, the value immediately following it in the array must not be chosen. (No loops needed.)

public boolean groupNoAdj(int start, int[] nums, int target) {
  if(start >= nums.length) return target == 0;
  if(target < 0) return false;
  boolean with = groupNoAdj(start + 2, nums, target - nums[start]);
  boolean without = groupNoAdj(start + 1, nums, target);
  return with || without;
}

groupNoAdj(0, [2, 5, 10, 4], 12) → true
groupNoAdj(0, [2, 5, 10, 4], 14) → false
groupNoAdj(0, [2, 5, 10, 4], 7) → false
groupNoAdj(0, [2, 5, 10, 4, 2], 7) → true
groupNoAdj(0, [2, 5, 10, 4], 9) → true
groupNoAdj(0, [10, 2, 2, 3, 3], 15) → true
groupNoAdj(0, [10, 2, 2, 3, 3], 7) → false
groupNoAdj(0, [], 0) → true
groupNoAdj(0, [1], 1) → true
groupNoAdj(0, [9], 1) → false
groupNoAdj(0, [9], 0) → true
groupNoAdj(0, [5, 10, 4, 1], 11) → true
"""
def groupNoAdj(start, nums, target):
    if start >= len(nums): return target == 0
    if target < 0: return False
    with_ = groupNoAdj(start + 2, nums, target - nums[start]);
    without = groupNoAdj(start + 1, nums, target);
    return with_ or without

"""
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with these additional constraints: all multiples of 5 in the array must be included in the group. If the value immediately following a multiple of 5 is 1, it must not be chosen. (No loops needed.)

public boolean groupSum5(int start, int[] nums, int target) {
  if(start >= nums.length) return target == 0;
  if(target < 0) return false;
  if(nums[start] % 5 == 0){
    if(start < nums.length - 1 && nums[start + 1] == 1)
    return groupSum5(start + 2, nums, target - nums[start]);
    else return groupSum5(start + 1, nums, target - nums[start]);
  }
  boolean with = groupSum5(start + 1, nums, target - nums[start]);
  boolean without = groupSum5(start + 1, nums, target);
  return with || without;
}

groupSum5(0, [2, 5, 10, 4], 19) → true
groupSum5(0, [2, 5, 10, 4], 17) → true
groupSum5(0, [2, 5, 10, 4], 12) → false
groupSum5(0, [2, 5, 4, 10], 12) → false
groupSum5(0, [3, 5, 1], 4) → false
groupSum5(0, [3, 5, 1], 5) → true
groupSum5(0, [1, 3, 5], 5) → true
groupSum5(0, [3, 5, 1], 9) → false
groupSum5(0, [2, 5, 10, 4], 7) → false
groupSum5(0, [2, 5, 10, 4], 15) → true
groupSum5(0, [2, 5, 10, 4], 11) → false
groupSum5(0, [1], 1) → true
groupSum5(0, [9], 1) → false
groupSum5(0, [9], 0) → true
groupSum5(0, [], 0) → true
"""
def groupSum5(start, nums, target):
    n = len(nums)
    if start >= n: return target == 0
    if target < 0: return False
    if nums[start] % 5 == 0:
        if start < n - 1 and nums[start + 1] == 1:
            return groupSum5(start + 2, nums, target - nums[start])
        else: return groupSum5(start + 1, nums, target - nums[start])
    with_ = groupSum5(start + 1, nums, target - nums[start]);
    without = groupSum5(start + 1, nums, target);
    return with_ or without

"""
Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target, with this additional constraint: if there are numbers in the array that are adjacent and the identical value, they must either all be chosen, or none of them chosen. For example, with the array {1, 2, 2, 2, 5, 2}, either all three 2's in the middle must be chosen or not, all as a group. (one loop can be used to find the extent of the identical values).


"""