# 가운데 글자 가져오기 : https://programmers.co.kr/learn/courses/30/lessons/12903
'''
    가운데 글자 가져오기
'''

def solution(s):
    center = len(s) // 2
    if len(s) % 2 == 0:
        return s[center - 1:center + 1]
    else:
        return s[center]
    
inputEx1 = "abcde"
inputEx2 = "qwer"

if __name__ == "__main__":
    print(solution(inputEx1))
    print(solution(inputEx2))