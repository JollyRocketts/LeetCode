class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        idx = 0
        m_prof = 0
        res = 0
        for i in worker:
            while idx < len(difficulty) and jobs[idx][0] <= i:
                if jobs[idx][1] > m_prof:
                    m_prof = jobs[idx][1]
                idx += 1
            res += m_prof
        return res