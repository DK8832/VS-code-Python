"""
#실습 - 1
#문자열 Hello, Python, World를 각각 한 줄에 3회씩 출력하는 프로그램을 작성해 보자. 
print("Hello"*3)
print("Python"*3)
print("World"*3)
print('\n')
"""

"""
#실습 - 2
#문자열 "Hello", "Python", "World" 를 리스트에 넣은 후
#       "World", "Python", "Hello" 순서로 한줄로 출력하는 프로그램을 작성해 보자.
a1 = "Hello"
a2 = "Python"
a3 = "World"
a = [a1, a2, a3]
print(a[2] + a[1] + a[0])
a.reverse()
print(a)
"""

"""
#실습 - 3
#네 개의 단어를 빈칸으로 두고 한줄로 입력 받아 리스트 변수에 저장한 후,
#입력한 순서의 반대로 해서 한줄에 하나씩 출력하는 프로그램을 작성해 보자.
b = input().split()
E = '\n'
print(f"{b[3]}\n{b[2]}\n{b[1]}\n{b[0]}")
print('\n')
print(b[3] + E + b[2] + E + b[1] + E + b[0])
"""

"""
#실습 - 4
#다섯 개의 정수값을 빈칸으로 두고 한 줄로 입력 받아 리스트
#변수에 저장한 후, 순서를 바꾸어 스페이스를 사이에 두고 한 줄로 출력하는 프로그램을 작성해 보자
c = list(map(int, input().split()))
ce = 1
for i in range(len(c)):
    print(c[len(c)-ce], end=' ')
    ce = ce + 1
c.reverse()
print('\n')
print(c)


c1 = list(map(int, input().split()))
print(c1[4], c1[3], c1[2], c1[1], c1[0])
"""

"""
#실습 - 5
#쉼표(,)를 사이에 둔 형식의다섯 개의 정숫값들을 한 줄로 입력받아
#스페이스를 사이에 두고 한줄로 출력하는 프로그램을 작성해 보자.
e = list(map(int, input().split()))
ee = 0
for i in range(len(e)):
    if i == len(e) - 1:
        print( e [ ee ])
    else:
        print( e [ ee ], end = ',')
        ee = ee + 1

e1 = list(map(int, input().split()))
print(e1[0], e1[1], e1[2], e1[3], e1[4], sep=',')
"""

"""
#실습 - 6
#실수 2개(f1, f2)를 입력 받아 곱을 출력하는 프로그램을 작성해보자
#1. my 에 자신의 생년월일, 이름을 요소로 하는 튜플 만들고 출력
my = (20091015, "송지율")
#2. love에 자신이 좋아하는 색과 과일 그리고 123, 123을 요소로 하는 튜플 만들고 출력
love = ("연두색", "딸기", 123, 123)
#3. my 튜플 + love 튜플 -> 출력
mylove = my + love
print(mylove)
#4. 각각 변수를 만들어, my 튜플 언패킹하고 출력
my1 = mylove[0]
my2 = mylove[1]
print(my1)
print(my2)
#5. mylove 튜플에서 이름 출력해보기
print("내 이름 : " + my2)
#6. mylove 튜플에서 123의 개수 출력
print("123의 개수 : ",  mylove.count(123))
#7. mylove에서 3번째 요소 출력
print("3번째 요소 : ", mylove[2])
"""

"""
#실습 - 7
#1. f1 입력 받기 (안내문자 = 'f1:' )
f1 = input("f1의 값을 입력해주세요 : ")
#1-1. f1를 실수형으로 변환하여 f1에 저장하기
f1 = float(f1)
#2. f2 입력받기 (안내문자 = 'f2:' )
f2 = input("f2의 값을 입력해주세요 : ")
# 2-1. f2를 정수형으로 변환하여 f2에 저장하기
f2 = int(f2)
# 3. f1*f2를 f3에 저장하기
f3 = f1*f2
# 4. 결과값 출력하기 (예상결과 = 'f1*f2 = 3')
print("f1*f2의 값은 ", f3, "입니다.")
"""

"""
#실습 - 8
#(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
#(A×B)%C는 ((A%C)x(B%C))%C 와 같을까?
#세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
#A = 5, B = 8, C =4
A = 5
B = 8
C = 4
print( (A+B)%C == ((A%C) + (B%C))%C )
print( (A*B)%C == ((A%C) * (B%C))%C )
print( (A+B)%C )
print( ((A%B) + (B%C))%C )
print( (((A%C) * (B%C))%C ) )
"""


"""
#실습 - 9
#수완나품 국제공항에 막 도착한 팀 레드시프트 일행은 눈을 믿을 수 없었다. 공항의 대형 스크린에
#올해가 2541년이라고 적혀 있던 것이었다. 현재는 1998년이다.
#불교 국가인 태국은 불멸기원(佛滅紀元), 즉 석가모니가 열반한 해를 기준으로 연도를 세는 불기를
#사용한다. 반면, 우리나라는 서기 연도를 사용하고 있다.
#불기 연도를 입력 받고 이를 서기 연도로 바꿔 주는 프로그램을 작성하시오
#불기 연도 -> 서기 연도 하는 방법
# 불기연도 - 543 = 서기연도
print("불기 연도를 입력시 서기 연도가 출력 됍니다.")
print("입력값을 아래에 입력해주세요")
a9 = input()
a9 = int(a9)
print(a9 - 543)
"""

"""
#실습 - 10
#다음 문장을 출력하시오.
#"!@#$%^&*()'
#(단, 큰따옴표와 작은따옴표도 함께 출력한다. )
print(" \"!@#$%^&*\' ")
"""