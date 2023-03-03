def solution(participant, completion):
    # 해시로 다시 풀어보기
    # 1. 정렬 (sort 사용)
    # 2. participant와 completion 비교
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if (participant[i] != completion[i]): # 같지않으면
            return participant[i]
    return participant[-1]
