# 기능 개발 : https://programmers.co.kr/learn/courses/30/lessons/42586

'''
    기능 개발
'''

import math

def solution(progresses, speeds):

    required_day_list = [math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
    
    answer = list()
    last_deployment_index = 0
    for index, required_day in enumerate(required_day_list):
        if required_day_list[last_deployment_index] < required_day:
            answer.append(index - last_deployment_index) 
            last_deployment_index = index
    answer.append(len(required_day_list) - last_deployment_index)
    
    # answer = [len(functions) for functions in functions_list]
    return answer


inputExLists = [((93, 30, 55), (1, 30, 5)), ((95, 90, 99, 99, 80, 99), (1, 1, 1, 1, 1, 1))]

if __name__ == "__main__":
    for inputEx in inputExLists:
        print(solution(*inputEx))