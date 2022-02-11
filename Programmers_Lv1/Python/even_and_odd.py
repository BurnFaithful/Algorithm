# 짝수와 홀수 : https://programmers.co.kr/learn/courses/30/lessons/12937

'''
    짝수와 홀수
'''

def solution(num):
    return "Even" if num % 2 == 0 else "Odd"

inputExList = (3, 4)

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))