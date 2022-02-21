# 위장 : https://programmers.co.kr/learn/courses/30/lessons/42578

'''
    위장
'''

from collections import Counter
from functools import reduce

def solution(clothes):
    counter = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), counter.values(), 1) - 1
    
    return answer


inputExList = (
    [['yellowhat', 'headgear'], ['bluesunglasses', 'eyewear'], ['green_turban', 'headgear']],
    [['crowmask', 'face'], ['bluesunglasses', 'face'], ['smoky_makeup', 'face']]
)

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))   