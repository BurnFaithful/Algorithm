# 수박수박수박수박수박수? : https://programmers.co.kr/learn/courses/30/lessons/12922

'''
    수박수박수박수박수박수?
'''

def solution(n):
    return ("수박" * (n // 2)) + ("수" * (n % 2))

inputExList = (3, 4)

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))