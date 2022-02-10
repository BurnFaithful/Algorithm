# 문자열 다루기 기본 : https://programmers.co.kr/learn/courses/30/lessons/12918

'''
    문자열 다루기 기본
'''

def solution(s):
    return len(s) in (4, 6) and s.isdigit()

inputExList = ("a234", "1234")

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))