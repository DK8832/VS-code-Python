E = '\n'
#실습 - 1
w = "World"
print(w)
print(E)

#실습 - 2
h = "Hello"
p = "Python"
print(h, p, w)
print(E)

#실습 - 3
print(3, '01', '004', sep='.')
print(2025, 3, 18, sep='. ')
print(h, p, w, sep='_')
print(E)

#실습 - 4
print(h, p, w, sep=E)
print("-----")
print(h)
print(p)
print(w)
print(E)

#실습 - 5
print('A', end=',')
print('B', end=',')
print('C')

print(2025, end='. ')
print(3, end='. ')
print(18)
print(E)

#실습 - 6
print(type(h))
print(type(p))
print(type(w))
print(type(E))
print(E)

print((w+E)*3)

#실습 - 7
a = 0
for i in range(6):
    print(a)
    a = a+1
print(E)

#실습 - 8
N = "지율"
A = 17
G = 4090

print(f"내 이름은 {N}이고 나이는 {A}살이야")
# f-string   
# 변수a = "철수", 변수b = 20
# print(f"문자열 {변수a} 문자열 {변수b} 문자열)
# 출력 - 문자열 철수 문자열 20 문자열
for i in range(3):
    A = A+1
    print(f"내 이름은 {N}이고 나이는 {A}살이야")
print(E)
for i in range(7):
    print(f"현재 최신 그래픽카드는 RTX {G}이야")
    G = G+1000
print(E)

#실습 - 9
"""name = input()
print("hello " + name)"""
#터미널 아래에 빈 네모 박스(텍스트) 클릭 후 타이핑

#실습 - 9.2
"""a = input()
b = input()
print(b + E + a)"""

#실습 - 10
a = 123.0
b = 456.0
print(a*b)
print(E)

#실습 - 11
"""
print("정수를 입력해주세요")
a1 = input()
b1 = input()
a1 = int(a1)
b1 = int(b1)
print(a1//b1)
print(a1%b1)
print(E)
"""

#실습 - 12
"""
a12,b12 = input().split()
a12 = str(a12)
b12 = int(b12)
print(a12*b12)
"""

#실습 - 13
print(123==456)
print(E)

#실습 - 14
"""
a14, b14 = input().split()
print(a14!=b14)
print(E)
"""

#실습  - 15
"""
a15, b15 = input().split()
print(a15==b15)
"""

#실습 - 16
"""
a16, b16 = input().split()
print(a16<=b16)
"""

#실습 - 17
a171 = "인마고"
a17 = list()
a17 = [17, "송지율", 5]
print(a17)
a17 += ["인천 전자 마이스터고", 1, 1]
print(a17)
a17.insert(17, '파이썬')
print(a17)
a17.append(20)
a17.append(10)
print(a17)
a17[3] = "인마고"
print(a17)
del a17[7]
del a17[7]
print(a17)
a17.remove(17)
print(a17)
a17.pop()
print(a17)
print(a17[3])
print("인마고" in a17)