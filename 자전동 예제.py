#문제 1: 배열의 중복 제거하기
#정수 배열이 주어졌을 때, 중복된 숫자를 제거하고 오름차순으로 정렬된 배열을 반환하라.
#입력: [3, 5, 2, 3, 7, 5]
#출력: [2, 3, 5, 7]
#a = list(map(int, input().split()))
#a1 = sorted(set(a))
#print(a1)

#문제 2: 문자열 압축하기
#문자열에서 연속적으로 반복되는 문자를 숫자와 함께 압축하라. 
#a = list(map(str, input()))
#ch = 97
#L = []
#for i in range(26):
#    L.append(a.count(chr(ch)))
#    ch = ch + 1
#ch = 97
#re = ""
#for i in L:
#    if(i>0):
#        re += chr(ch)+str(i)
#    ch = ch + 1
#print(re)

#문제 3: 소수 판별하기
#주어진 숫자가 소수인지 아닌지 판별하는 함수를 작성하라. 
#n = int(input())
#
#if n <= 1:
#    print(False)
#else:
#    for i in range(2, n):
#        if n % i == 0:
#            print(False)
#            break
#    else:
#        print(True)

#문제 4: 피보나치 수열 구하기
#정수 n이 주어졌을 때, 피보나치 수열의 n번째 숫자를 반환하라.
#(피보나치 수열: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, ...)
#n = int(input())
#nums = [0, 1]
#
#if n == 1:
#    print(nums[0])
#else:
#    for i in range(2, n):
#        nums.append(nums[i-1] + nums[i-2])
#    print(nums[n-1])

#문제 5: 두 수의 합
#배열과 특정 값이 주어졌을 때, 배열 내 두 수를 더해 특정 값을 만들 수 있는지 확인하여 True/False를 반환하라.
#입력: [2, 7, 11, 15], 9
#출력: True (2+7=9)
#list = list(map(int, input("리스트를 입력해주세요 : ").split()))
#num = int(input("정수값을 입력해주세요: "))
#res = []
#
#for i in range(len(list)):
#    for j in range(i + 1, len(list)):
#        if(list[i] + list[j] == num):
#            res.append(f"True ({list[i]} + {list[j]} == {num})")
#if(res):
#    for n in res:
#        print(n)
#else:
#    print("False")