# 직사각형 별찍기 : https://programmers.co.kr/learn/courses/30/lessons/12969
'''
    직사각형 별찍기
'''

n, m = map(int, input().split(' '))
for row in range(m):
    print('*' * n)