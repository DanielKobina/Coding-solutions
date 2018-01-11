class Solution:
    def maxProfit(self, prices):
        """
        Find maximum profit that can be made from the array prices.
        Input:  self (class object reference to itself)
                prices (list of stock prices, with indexes corresponding to days)
        Output: maximum profit obtainable through buying and selling stocks
        """
        
        maxP = 0 #maximum profit
        if len(prices) <= 1: #if array of length 1 or less, unable to gain profit
            return maxP
        
        for i in range(len(prices)-1): #i will become the first element through the second to last element
                                       #i will not become the last element to avoid index error for c
            p = prices[i] #price on previous day
            c = prices[i+1] #price current day
            
            if c > p: #If the price on the current day is greater than the previous price, obtain profit
                maxP += c - p
        
        return maxP
