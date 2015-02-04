# coding=utf-8
'''
Created on 2015年2月4日

@author: zhangrui6
'''
class Solution:
# @param num, a list of integers
# @return a string

    def minsub(self, s):
        s_set = set(s)
        start = 0
        end = len(s)
        min_l = len(s)
        for (i, c) in enumerate(s):
            if i == 0:
                start = 0
                end = 0
                if set(s[start:end + 1]) == s_set:
                    return s[start:end + 1]
            else:
                end = end + 1
                if set(s[start:end + 1]) == s_set:
                    j = i
                    tmp = set([])
                    while tmp != s_set:
                        tmp.add(s[j])
                        j = j - 1
                    j = j + 1
                    if (i - j + 1) < min_l:
                        min_s = j
                        min_e = i
                        start = i + 1
        return s[min_s:min_e + 1]
if __name__ == "__main__":
    a = Solution()
    print a.minsub("aabcadbbbcca")
    print a.minsub("aabcaadbbbcca")
