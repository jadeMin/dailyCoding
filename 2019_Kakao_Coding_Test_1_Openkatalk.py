# python dict()을 이용한 풀이법
# userID를 key로 name을 value로 set -> dict 저장
# Enter과 Change event가 발생 시 dict의 이름을 추가 또는 변경하여 일괄적으로 처리
# 각각의 event에 맞게 출력문 string을 log에 저장하고 answer를 설정
def solution(record):
    answer = []
    userDict = dict()   
    userLog = []
    
    for p in range(0, len(record)):
        info = record[p].split(" ")
        if info[0] == "Enter":
            userDict[info[1]] = info[2]
            userLog.append([info[1], "님이 들어왔습니다."])
        elif info[0] == "Change":
            userDict[info[1]] = info[2]
        elif info[0] == "Leave":
            userLog.append([info[1], "님이 나갔습니다."])

    for result in userLog:
        answer.append(userDict[result[0]] + result[1])
        
    return answer
