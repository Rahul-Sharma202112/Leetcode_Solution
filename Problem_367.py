# Valid Perfect Square
"""
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.
"""

# solution:

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

# approach 1:
     """
       x,square=1,0
        
        while(square<num):
            square=x**2
            if square == num:
                return True
            x+=1
        return False
     """   
        
# approach 2:

        l,r= 0,num
        
        while(l<=r):
            mid=(l+r)//2
            squared=mid**2
            if squared ==num:
                    return True
            elif squared<num:
                    l =mid+1
            else:
                    r=mid-1
                    
        return False