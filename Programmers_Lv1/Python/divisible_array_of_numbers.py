# 나누어 떨어지는 숫자 배열 : https://programmers.co.kr/learn/courses/30/lessons/12910

'''
    나누어 떨어지는 숫자 배열
'''

def solution(arr, divisor):
    return sorted([element for element in arr if element % divisor == 0]) or [-1]

inputExList = [([5, 9, 7, 10], 5), ([2, 36, 1, 3], 1), ([3, 2, 6], 10)]

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(*inputEx))
