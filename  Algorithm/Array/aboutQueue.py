# 구조
# - 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
# - FIFO (First-In, First-Out), Last-In, Last-Out
# - 줄 서는 것과 비슷하다고 이해하면 됨

# 용어
# - Enqueue : 큐에 데이터를 넣는 기능
# - Dequeue : 큐에서 데이터를 꺼내는 기능

# 큐가 많이 쓰이는 곳
# - 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨


#-------------------------------------
# Queue()로 큐 만들기 ( 가장 일반적인 큐 )
import queue
data_queue = queue.Queue()
data_queue.put("un")
data_queue.put(1) # queue에 데이터 넣기

print(data_queue.qsize()) # queue 사이즈 확인

print(data_queue.get()) # >> un / queue에서 데이터 빼기 ( 제일 먼저 넣은게 빠짐 )
print(data_queue.get()) # >> 1  / 넣은 순서대로 빠짐

#-------------------------------------
# LifoQueue로 큐 만들기 (Lifo: Last-In, First-Out)
data_lifoQueue = queue.LifoQueue();

data_lifoQueue.put("un")
data_lifoQueue.put(1)

# 마지막에 넣은 것 부터 빠짐
print(data_lifoQueue.get()) # >> 1
print(data_lifoQueue.get()) # >> un

#-------------------------------------
# PriorityQueue()로 큐 만들기
# 각각의 데이터마다 우선순위 번호를 같이 넣어서, 우선순위가 높은 순위부터 추출됨
data_priorityQueue = queue.PriorityQueue()
data_priorityQueue.put((10, "un")) # 튜플 형식으로 (우선순위, 값) 형태로 넣음
data_priorityQueue.put((11, 5))
data_priorityQueue.put((5, "ch"))
# 우선순위 숫자가 낮은 순서로 출력됨
print(data_priorityQueue.get()) # >> (5, ch)
print(data_priorityQueue.get()) # >> (10, un)
print(data_priorityQueue.get()) # >> (11, 5)\

#-------------------------------------
# 프로그래밍 연습
# 1. 리스트 변수로 큐를 다루는 dnqueue, dequeue 기능 구현해보기
queue_list = list()

def enqueue(data): # 넣을떈 그냥 넣고
    queue_list.append(data)

def dequeue():
    data = queue_list[0] # 뺄때는 젤 처음 넣은거 뺀 다음에
    del queue_list[0] # 처음에 뺀거 삭제 해줘야함 그래야 뒤에 있는 데이터가 떙겨지니까
    return data

for index in range(10):
    enqueue(index)

print(len(queue_list)) # >> 10
print(dequeue()) # >> 0
print(dequeue()) # >> 1
print(dequeue()) # >> 2













