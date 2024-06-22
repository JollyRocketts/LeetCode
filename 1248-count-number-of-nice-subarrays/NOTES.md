le = len(nums)
if k > le:
return 0
elif k == le:
for i in nums:
if i%2 == 0:
continue
else:
return 0
return 1
tot = 0
l = 0
r = 0
n_odd = 0
n_even = 1
while l <= (len(nums)-k):
if nums[r]%2==1:
n_odd += 1
elif n_odd == 0:
n_even += 1
if n_odd == k:
c = 1
while r+1 < len(nums) and nums[r+1]%2==0:
r += 1
c += 1
tot += (n_even*c)
l += n_even
r = l
n_odd = 0
n_even = 1
continue
elif r+1 < len(nums):
r += 1
else:
l += 1
r = l
n_odd = 0
n_even = 1
continue
return tot