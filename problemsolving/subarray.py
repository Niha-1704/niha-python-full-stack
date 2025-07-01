nums = [1,2,1,2,1]
k = 3
length = 0
sum_ = 0
dic ={}
c = 0
for x in range(len(nums)):
    sum_ += nums[x]
    if sum_ == k:
        length = x + 1
        c += 1
    else:
        if (sum_ - k) in dic:
            length = max(length,x - dic[sum_ - k])  
            c += 1
    if sum_ not in dic:
        dic[sum_] = x
print(c)