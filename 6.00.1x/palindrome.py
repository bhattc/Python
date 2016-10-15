def isPalindrome(s):
    def tochar(s):
        s=s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def ispal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and ispal( s[1,-1])
    return ispal(tochar(s))
