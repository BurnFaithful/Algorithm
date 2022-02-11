# 평균 구하기 : https://programmers.co.kr/learn/courses/30/lessons/12944

'''
    평균 구하기
'''

def solution(arr):
    return sum(arr) / len(arr)

inputExList = ([1, 2, 3, 4], [5, 5])

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))