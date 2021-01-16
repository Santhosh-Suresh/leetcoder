import re


class Solution( object ):

    # def isMatch(self,s,p):
    #     return bool(re.match("\A"+p+"\Z", s))

    def isMatch(self , s , p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p:
            pat = p[-1]
            p = p[:-1]
            if pat == "*":
                reverse = 0
                if p:
                    new_pat = p[-1]
                    p = p[:-1]
                else:
                    print( "Unexpected: * does not follow any character" )
                    return False
                if self.isMatch( s , p ):
                    return True
                while len( s ) > reverse and (s[-1 - reverse] == new_pat or new_pat == "."):
                    if self.isMatch( s[:-1 - reverse] , p ):
                        return True
                    reverse += 1
                else:
                    return False
            elif s and ((s[-1] == pat) or pat == "."):
                s = s[:-1]
                return self.isMatch( s , p )
            else:
                return False
        elif s:
            return False
        else:
            return True


