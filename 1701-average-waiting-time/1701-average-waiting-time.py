class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr = customers[0][0]
        
        tot_wait = 0
        #prev_arr = 0
        
        for arrival, time in customers:
            if arrival <= curr:
                tot_wait += curr-arrival
            else:
                curr = arrival
            tot_wait += time
            curr += time
        
        return tot_wait/len(customers)