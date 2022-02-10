# 문자열 내 p와 y의 갯수 : https://programmers.co.kr/learn/courses/30/lessons/12916

'''
    문자열 내 p와 y의 갯수
'''

def solution(s):
    return s.lower().count('p') == s.lower().count('y')

inputExList = ("pPoooyY", "Pyy")

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))