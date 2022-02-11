# 자릿수 더하기 : https://programmers.co.kr/learn/courses/30/lessons/12931

'''
    자릿수 더하기
'''

def solution(n):
    return sum(map(int, str(n)))

inputExList = (123, 987)

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))