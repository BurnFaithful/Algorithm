# 하샤드 수 : https://programmers.co.kr/learn/courses/30/lessons/12947

'''
    하샤드 수
'''

def solution(x):
    return True if x % sum([int(digit) for digit in str(x)]) == 0 else False

inputExList = (10, 12, 11, 13)

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))