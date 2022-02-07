# K번째 수 : https://programmers.co.kr/learn/courses/30/lessons/42748

'''
    2022.01.23
'''

def solution(array, commands):
    '''
        solution
    '''
    return [(sorted(array[i[0] - 1:i[1]]))[i[2] - 1] for i in commands]


if __name__ == "__main__":
    result = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    print(result)
