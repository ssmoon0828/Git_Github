'''
github에 sourcetree를 이용하여
python code가 올라가는지 확인
'''

# 1부터 n까지 짝수 출력
n = int(input("정수를 입력하세요 : "))

for i in range(n + 1):
    if i % 2 == 0:
        print(i)


# 구구단 출력

for i in range(2, 10):
    print(i, "단")
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)
    print("")