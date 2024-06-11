class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        arr = [releaseTimes[i]-releaseTimes[i-1] for i in range(len(releaseTimes))]
        arr[0] = releaseTimes[0]
        z = zip(keysPressed, arr)
        res = sorted(z, key = lambda x:-x[1])
        m = res[0][1]
        t = res[0][0]
        for i in res:
            m_val = i[1]
            temp = i[0]
            if m_val < m:
                return t
            else:
                if temp>t:
                    t = temp
        return t