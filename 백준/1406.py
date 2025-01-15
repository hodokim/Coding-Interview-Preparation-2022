import sys
sys.stdin = open('testCase.txt', 'r')
input = sys.stdin.readline

left_str = list(input().strip()) #왜 strip 해야하지?
right_str = []

m = int(input())
for _ in range(m):
    command = input().split()
    if command[0] == 'L':
        if left_str:
            right_str.append(left_str.pop())
    elif command[0] == 'D':
        if right_str:
            left_str.append(right_str.pop())
    elif command[0] == 'B':
        if left_str:
            left_str.pop()
    elif command[0] == 'P':
        left_str.append(command[1])

print(''.join(left_str + right_str[::-1])) # ''.join의 의미와 right_str[::-1] 의 의미 right_str[-1] 과 어떻게 다르지?


# strip()은 문자열의 양쪽에서 공백문자(스페이스, 탭 등)와 줄바꿈 문자를 제거한다.
# 왜 필요한가? 프로그램에서 문자열을 리스트로 변환하거나 처리할 때 
# 줄바꿈 문자가 포함되면 의도치 않은 결과를 초래할 수 있습니다.
# 예) left_str = list("abc\n")
# print(left_str)  # ['a', 'b', 'c', '\n']


#''.join 의 의미 : 리스트에 있는 문자열들을 하나의 문자열로 결합한다.

#right_str[::-1]은 right_str 리스으를를 역순으로 뒤집은 새로운 리스트를 반환
#right_str[-1]은 right_str 리스트의 마지막 요소를 반환