# 문자열 내림차순으로 배치하기 : https://programmers.co.kr/learn/courses/30/lessons/12917

'''
    문자열 내림차순으로 배치하기
'''

def solution(s):
    return "".join(sorted(s, reverse=True))

inputEx = "Zbcdefg"

if __name__ == "__main__":
    print(solution(inputEx))

