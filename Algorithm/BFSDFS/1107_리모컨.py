import sys
sys.stdin =open('in.txt','rt')
input = sys.stdin.readline
target = int(input())
n = int(input())
break_num= list(map(int, input().split()))

# 현재 채널에서 +,-만 사용하여 이동하는 경우
min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        # 각 숫자의 버튼이 고장났는지 확인 후, 고장 났으면 break
        if int(nums[j]) in break_num:
            break

        # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))#(min_count,현재채널에서 목표채널로 가기위한 버튼 클릭 횟수)

print(min_count)