# 정수 내림차순으로 배치하기 : https://programmers.co.kr/learn/courses/30/lessons/12933

'''
    정수 내림차순으로 배치하기
'''

def solution(n):
    return int("".join(sorted(str(n), reverse=True)))

inputEx = 118372;

if __name__ == "__main__":
    print(solution(inputEx))