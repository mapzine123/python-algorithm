# 구조
# - 데이터에 제한적으로 접근할 수 있는 구조 ( 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조 )
# - 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 데이터 구조
# - LIFO (Last-In, First-Out), FILO (First-In, Last-Out)

# 활용
# - 컴퓨터 내부의 프로세스 구조의 함수 동작 방식

# 주요 기능
# - push() : 데이터를 스택에 넣기
# - pop() : 데이터를 스택에서 빼기

# 장점
# - 구조가 단순해서 구현이 쉽다
# - 데이터 저장 / 읽기 속도가 빠르다

# 단점
# - 데이터 최대 갯수를 미리 정해야한다
# - 저장 공간의 낭비가 발생할 수 있다

def recursive(data):
    if data < 0:
        print('ended')
    else:
        print(data)
        recursive(data-1)
        print('returned', data)

data_stack = list()

data_stack.append(1)
data_stack.append(2)
print(data_stack) # [1, 2]

print(data_stack.pop()) # >> 2 , 뒤에 넣은게 먼저 빠짐 LIFO

# 프로그래밍 연습
# 1. 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기
stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1] # 맨 끝 인덱스 번호
    del stack_list[-1] # 맨 끝 데이터 삭제
    return data

for index in range(10):
    push(index) # [1 ~ 9]

print(pop()) # >> 9




