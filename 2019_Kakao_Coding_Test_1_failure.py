import operator
from collections import Counter as count

def solution(N, stages):
    answer = []
    failure = dict()
    userStage = count(stages)
    totalUser = len(stages)
    
    for i in range(1,N+1):
        stayUsers = userStage[i]
        if stayUsers == 0:
            failure[i] = 0
        else:
            failure[i] = stayUsers / totalUser
        totalUser -= stayUsers
        
    sorted_failure = sorted(failure.items(), key = operator.itemgetter(1), reverse = True)
    
    for k, v in sorted_failure:
        answer.append(k)
    
    return answer
