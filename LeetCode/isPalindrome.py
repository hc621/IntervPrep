s = "A man, a plan, a canal: Panama"


def isPalindrome(self, s: str) -> bool:
    import re
    s1 = re.sub(r'[^\w\s]', '', s)
    s1 = s1.replace(' ', '')
    s1 = s1.lower()

    if s1 == s1[::-1]:
        return True
    else:
        return False


res = isPalindrome(s)
print(res)