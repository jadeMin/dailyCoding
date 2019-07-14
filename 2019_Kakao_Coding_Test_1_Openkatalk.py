def solution(record):
    answer = []
    userDict = dict()
    userLog = []
    
    for p in range(0, len(record)):
        info = record[p].split(" ")
        if info[0] == "Enter":
            userDict[info[1]] = info[2]
            userLog.append([info[1], "���� ���Խ��ϴ�."])
        elif info[0] == "Change":
            userDict[info[1]] = info[2]
        elif info[0] == "Leave":
            userLog.append([info[1], "���� �������ϴ�."])

    for result in userLog:
        answer.append(userDict[result[0]] + result[1])
        
    return answer