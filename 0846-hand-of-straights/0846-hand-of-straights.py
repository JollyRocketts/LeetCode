class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        if groupSize == 1:
            return True
        
        while len(hand) != 0:
            temp = min(hand)
            for i in range(groupSize - 1):
                if temp + 1 not in hand:
                    return False
                hand.remove(temp)
                temp += 1
                if i == groupSize - 2:
                    hand.remove(temp)
        return True