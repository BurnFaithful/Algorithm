# 행렬의 덧셈 : https://programmers.co.kr/learn/courses/30/lessons/12950

'''
    행렬의 덧셈
'''

def solution(arr1, arr2):
    return [[sum(row) for row in zip(*col)] for col in zip(arr1, arr2)]

inputExList = (([[1, 2], [2, 3]], [[3, 4], [5, 6]]), ([[1], [2]], [[3], [4]]))

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(*inputEx))