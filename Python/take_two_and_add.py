# 두 개 뽑아서 더하기 : https://programmers.co.kr/learn/courses/30/lessons/68644
'''
    두 개 뽑아서 더하기
'''

from itertools import combinations

inputEx = [2, 1, 3, 4, 1]


def solution(numbers):
    '''
        combinations : 조합
        set : 중복 처리
        sorted : 오름차순 정렬
    '''
    return sorted(list(set([sum(pair) for pair in combinations(numbers, 2)])))

if __name__ == "__main__":
    result = solution(inputEx)
    print(result)
