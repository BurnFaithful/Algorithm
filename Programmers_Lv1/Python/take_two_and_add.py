# 두 개 뽑아서 더하기 : https://programmers.co.kr/learn/courses/30/lessons/68644
'''
    두 개 뽑아서 더하기
'''

from itertools import combinations

inputEx = [2, 1, 3, 4, 1]

def solution(numbers):
    return sorted(list(set([sum(pair) for pair in combinations(numbers, 2)])))

if __name__ == "__main__":
    print(solution(inputEx))