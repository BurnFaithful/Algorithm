# x만큼 간격이 있는 n개의 숫자 : https://programmers.co.kr/learn/courses/30/lessons/12954

'''
    x만큼 간격이 있는 n개의 숫자
'''

def solution(x, n):
    return [x * i for i in range(1, n + 1)]

inputExList = ((2, 5), (4, 3), (-4, 2))

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(*inputEx))