# 서울에서 김서방 찾기 : https://programmers.co.kr/learn/courses/30/lessons/12919

'''
    서울에서 김서방 찾기
'''

def solution(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다"

inputEx = ["Jane", "Kim"]

if __name__ == "__main__":
    print(solution(inputEx))