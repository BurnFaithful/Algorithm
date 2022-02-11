# 콜라츠 추측 : https://programmers.co.kr/learn/courses/30/lessons/12943

'''
    콜라츠 추측
'''

def solution(num):
    for index in range(500):
        if num == 1:
            return index
        num = num / 2 if num % 2 == 0 else (num * 3 + 1)
    
    return -1

inputExList = (6, 16, 626331)

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))