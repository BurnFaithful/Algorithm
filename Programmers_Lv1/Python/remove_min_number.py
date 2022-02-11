# 제일 작은 수 제거하기 : https://programmers.co.kr/learn/courses/30/lessons/12935

'''
    제일 작은 수 제거하기
'''

def solution(arr):
    if len(arr) != 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]

inputExList = ([4, 3, 2, 1], [10])

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))