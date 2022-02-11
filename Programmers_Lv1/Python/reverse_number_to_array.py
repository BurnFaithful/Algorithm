# 자연수 뒤집어 배열로 만들기 : https://programmers.co.kr/learn/courses/30/lessons/12932

'''
    자연수 뒤집어 배열로 만들기
'''

def solution(n):
    return list(map(int, str(n)[::-1]))

inputEx = 12345;

if __name__ == "__main__":
    print(solution(inputEx))