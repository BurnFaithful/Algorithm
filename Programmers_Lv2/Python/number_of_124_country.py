# 124 나라의 숫자 : https://programmers.co.kr/learn/courses/30/lessons/12899

'''
    124 나라의 숫자
'''

from itertools import product

def decimal_to_ternary(n):
    result = ''
    
    while n > 0:
        n, remainder = divmod(n - 1, 3)
        result += str(remainder + 1)
    
    return result[::-1]

def solution(n):
    return decimal_to_ternary(n).replace('3', '4')

if __name__ == "__main__":
    print(solution(9))