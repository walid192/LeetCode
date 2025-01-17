class Solution:
    def maxValue(self, s: str, x: int) -> str:
        # if n is postive i have to insert x in place of the first smaller integer i find to maximize it

        # if n is negative i hvae to insert x into the place of the place of the first bigger i find to maxmize it
        if s[0]=='-':
            for i in range(1,len(s)):
                if int(s[i])>x:
                    return s[:i]+str(x)+s[i:]
            return s+str(x)

        else:
            for i in range(len(s)):
                if int(s[i])<x:
                    return s[:i]+str(x)+str[i:]

            return s+str(x)


        