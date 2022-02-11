# 문자열을 정수로 바꾸기 : https://programmers.co.kr/learn/courses/30/lessons/12925

'''
    문자열을 정수로 바꾸기
'''

def solution(s):
    return int(s)

inputExList = ("1234", "-1234")

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))