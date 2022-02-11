# 이상한 문자 만들기 : https://programmers.co.kr/learn/courses/30/lessons/12930

'''
    이상한 문자 만들기
'''

def solution(s):
    return " ".join(map(lambda x: "".join([letter.upper() if index % 2 == 0 else letter.lower() for index, letter in enumerate(x)]), s.split(' ')))


inputEx = "try hello world"

if __name__ == "__main__":
    print(solution(inputEx))