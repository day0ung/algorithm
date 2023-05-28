def solution(name, yearning, photo):
    memory = dict(zip(name, yearning))
    answer = []
    for arr in photo:
        score = 0
        for i in arr:
            if i in memory :
                score += memory[i]
        answer.append(score)
    return answer