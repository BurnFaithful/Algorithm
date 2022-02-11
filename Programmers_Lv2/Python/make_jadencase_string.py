# JadenCase 문자열 만들기 : https://programmers.co.kr/learn/courses/30/lessons/12951

'''
    JadenCase 문자열 만들기
'''

def solution(s):
    return " ".join([word.capitalize() for word in s.split(" ")])

inputExList = ("3people unFollowed me", "for the last week")

if __name__ == "__main__":
    for inputEx in inputExList:
        print(solution(inputEx))