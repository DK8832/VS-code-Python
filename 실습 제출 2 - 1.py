#실습 - 1
#정수값 123과 456을 == 비교 연산한 결괏값을 반대로 바꾸어 출력하는 프로그램을 작성
#print(not 123 == 456)

#실습 - 2
#두 개의 정수를 한 번에 한 줄씩 입력받아 두 값이 다르지 않은 경우는 True, 두 값이 다른 경우는 False를 출력하는 프로그램을 작성해 보자
#a1 = int(input())
#a2 = int(input())
#print(a1==a2)


#실습 - 3
#한 개의 정숫값을 입력받아 그 값이 3의 배수이거나 5의 배수인 경우에만 True를 출력하고, 그 외의 경우는 False를 출력하는 프로그램을 작성해 보자
#a = int(input())
#print(a%3==0 or a%5==0)

#실습 - 4
#한 개의 정숫값을 입력받아 그 값이 2의 배수이면서 3의 배수이고 또한 5의 배수인 경우, 즉 입력받은 값이 2, 3, 5의 공배수인 경우에만
#True를 출력하고 그 외의 경우는 False를 출력하는 프로그램을 작성해 보자.
#a = int(input())
#print(a%2 + a%3 + a%5 == 0) #사칙연산만 사용
#print(a%2==0 and a%3==0 and a%5==0) #AND 사용
#print((a%2==0) and (a%3==0) and (a%5==0)) #AND 사용 다른 버전

#실습 - 5
#한 개의 정숫값(n)을 입력받아, ~n+1값을 출력하는 프로그램을 작성해 보자.
#n = int(input())
#print(~n + 1)

#실습 - 6
#한 개의 정수값(n)을 입력받아 n|1값을 출력하는 프로그램을 작성해 보자
#n = int(input())
#print(n|1)

#실습 - 7
#한 개의 정숫값(n)을 입력받아 n&1값을 출력하는 프로그램을 작성해 보자
#n = int(input())
#print(n&1)

#실습 - 8
#한 개의 정숫값(n)을 입력받아 n^(-1)값을 출력하는 프로그램을 작성해 보자
#n = int(input())
#print(n^(-1))

#실습 - 9
#한 개의 정숫값(n)을 입력받아 n>>1, n<<1값을 출력하는 프로그램을 작성해 보자
#n = int(input())
#print(n>>1, n<<1)

#실습 - 10
#다음 조건에 맞게 코드를 작성하시오.
# 1. name 변수에 자신의 이름을 대입
#name = "송지율"
# 2. to 변수에 "Hello" 대입
#to = "Hello"
# 3. say 변수에 name 변수와 to 변수를 ","f로 연결하고 출력하기 (연산자 사용)
#say = name + ", " + to
#print(say)
# 4. say변수 5번 출력하기 (연산자 사용)
#print(say*5)
# 5. say 변수 3번 줄 바꿔 출력하기 (연산자, 이스케이프 코드사용)
#print((say+'\n')*3)
# 6. "Happy Programming" 출력 (큰 따옴표도 같이 출력)
#print("\"Happy Programming\"")
# 7. Hi, "Happy Programming" 출력하기 (이스케이프 코드 사용)
#print("Hi, \"Happy Programming\"")