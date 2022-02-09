# 두 정수 사이의 합 : https://programmers.co.kr/learn/courses/30/lessons/12912

'''
    두 정수 사이의 합
'''

# 등차수열의 합으로 계산(시간복잡도 향상)
def solution(a, b):
    return (abs(a - b) + 1) * (a + b) // 2

inputExList = [(3, 5), (3, 3), (5, 3)]

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(*inputEx))