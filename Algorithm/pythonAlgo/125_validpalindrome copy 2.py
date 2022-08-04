# dequ 사용
from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = deque()
        for i in s:
            if i.isalnum():
                check.append(i.lower())
        while len(check) > 1:
            if check.popleft() != check.pop():
                return False
        return True
