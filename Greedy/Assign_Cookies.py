class Solution:
    def findContentChildren(self, g, s):
        """
        Find the number of children able to satisfy given
        Input: g (array of greedy children containing greed levels)
               s (array of cookie size)
        Output: maximum number of children that can be satisfied
        """
        cc = 0 #number of satisfied children
        g = sorted(g) #sort greedy children smalles to largest
        s = sorted(s) #sort cookie sizes
        
        i,j = 0,0 #initialize indexes
        
        while i < len(g) and j < len(s): #keep going until run out of cookies or children to satisfy
            if s[j] >= g[i]: #check if cookie size satisfies child
                cc += 1 
                i += 1 #move onto greedier child
                
            j += 1 #either way a cookie is removed
                
        return cc
