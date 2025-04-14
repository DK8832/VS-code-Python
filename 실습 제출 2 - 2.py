#실습 - 11
# 1. s 문자열에 "Life is too short." 대입
#s="Life is too short."
# 2. 인덱스 5번 문자 출력
#print(s[5])
# 3. 앞에서 3번째 문자 출력
#print(s[2])
# 4. 인덱스 -4번 문자 출력
#print(s[-4])
# 5. 문자 e 출력 (음수 인덱스)
#print(s[-15])
# 6. 문자 h 출력
#print(s[-5])

#실습 - 12
# 1. s 문자열에 "Life is too short, You need Python"
#s = "Life is too short, You need Python"
# 2. ed Pyt 출력
#print(s[25:31])
# 3. ort, Y 출력 (음수 인덱스 사용)
#print(s[-20:-14])
# 4. Life is too 출력
#print(s[0:11])
# 5. Python 출력 (음수 인덱스 사용)
#print(s[-6:])

#실습 - 13
# 1. m 변수에 " Welcome to Python and Python is fun" 대입
#m = " Welcome to Python and Python is fun"
# 2. m 문자열의 개수 세기
#print(len(m))
# 3. t의 개수 출력
#print(m.count('t'))
# 4. 왼쪽 공백 없애서 m 변수에 대입하고 출력하기
#m = m.lstrip()
#print(m)
# 5. 모두 대문자로 변환하여 출력하기
#print(m.upper())
# 6. 모두 소문자로 변환하여 출력하기
#print(m.lower())
# 7. fun 대신 happy로 대체하여 출력하기
#print(m.replace("fun", "happy"))
# 8. th를 왼쪽부터 찾아서 출력하기
#print(m.find("th"))
# 9. oo를 왼쪽부터 찾아서 출력하기
#print(m.find("oo"))
# 10. an를 오른쪽부터 찾아서 출력하기
#print(m.rfind("an"))

#실습 - 14
# 1. m 변수에 "Welcome to Python, Python is fun" 대입
#m = "Welcome to Python, Python is fun"
# 2. m 문자열에 fun이 있는지 확인
#print(m.find("fun"))
# 3. m 문자열에 happy가 있는지 확인
#print(m.find("happy"))
# 4. m 문자열을 "," 기준으로 나누어 v 리스트 만들고 출력하기
#v = m.split(',')
#print(v)
# 5 .v 리스트를 ":"로 이어서 문자열 만들고 출력하기
#v = ":".join(v)
#print(v)

#실습 - 15
# 1. nums에 100, 3, 49, 11, 34 요소 넣고 출력하기
#nums = [100, 3, 49, 11, 34]
#print(nums)
# 2. nums의 요소 개수 세기
#print(len(nums))
# 3. nums 리스트를 반대로 출력하기
#nums.reverse()
#print(nums)
# 4. nums 리스트 정렬하고 출력하기
#nums.sort()
#print(nums)
# 5. nums 리스트 초기화하고 출력하기
#nums.clear()
#print(nums)

#실습 - 16
# 소윤이는 친구들의 생일을 기억하고 싶어서 친구들의 이름과 생일을 튜플에
# 저장하기로 했다. 생일을 저장하고 나면 친구들이 생일을 몇 번이나 자주 물어봐도
# 쉽게 확인할 수 있을 것이다. 친구 "이민호"의 생일은 1995년 5월 15일,
# "김영희"의 생일은 1992년 3월 22일이다. 이 두 친구의 생일을 튜플로 저장하고,
#f1 = ("이민호", 1995, 5, 15)
#f2 = ("김영희", 1992, 3, 22)
# 1) “이민호”가 튜플 안에서 몇 번째 위치에 있는지 찾아라.
#print(f"이민호는 튜플에서 {f1.index('이민호')}번째 위치에 있습니다.")
# 2) “김영희”라는 이름이 몇 번 등장하는지 확인해라.
#print(f"김영희는 튜플에 {f2.count('김영희')}번 등장합니다.")

#실습 - 17
#"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
#(입력 받을 때 안내문구는 “연도.월.일을 입력하세요 : ” 로 한다.)
#ymd = list(map(int, input("연도.월.일을 입력하세요 : ").split(".")))
#print(f"{ymd[2]}일-{ymd[1]}월-{ymd[0]}년")

#실습 - 18
#꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!
#(단, A B C를 공백을 사이에 두고 입력 받는다.)
#(주석으로 코드에 대한 설명을 작성한다.)
#(입력 받을 때, 안내문구는 “A B C를 입력하세요 : ”로 한다.)
#A, B, C = map(int, input("A B C를 입력하세요 : ").split())
#print(A + B + C)

#실습 - 19
#단어 S와 정수 i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램을 작성하시오.
#(단, S와 정수 i는 키보드로 입력 받으며, 각각 한 줄 씩 입력 받는다.)
#(입력 받을 때 안내문구는 “단어 : ”와 “번호 : ”)
#S = input("단어 : ")
#i = int(input("번호 : "))
#print(S[i - 1])

#실습 - 20
#주민번호는 다음과 같이 구성된다. XXXXXX-XXXXXXX
#왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
#주민번호를 입력 받아 “20YY년 MM월 DD일에 태어났습니다.” 형태로 바꿔 출력해보자.
#(입력 받을 때, 안내 문구는 "주민번호 : "로 한다.)
#n = input("주민번호 : ")
#ny = n[0:2]
#nm = n[2:4]
#nd = n[4:6]
#print(f"20{ny}년 {nm}월 {nd}일에 태어났습니다.")