import copy


class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = []
        for i in s:
            if i.isalnum():
                check.append(i.lower())
        rev_check = copy.deepcopy(check)
        rev_check.reverse()

        if check == rev_check:
            return True
        else:
            return False
