class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = sum([abs(seats[x]-students[x]) for x in range(len(seats))])
        return res