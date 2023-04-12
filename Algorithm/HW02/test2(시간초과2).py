def solution(participant, completion):
    # if (len(participant) < 1 or len(participant) > 100000) :
    #     return -1
    # if (len(completion) != len(participant) - 1) :
    #     return -1
    #for checker in participant :
    #   if (len(checker) > 20 or checker < 1) :
    #       return -1 
    
    answer = ''
    for person in completion :
        participant.remove(person)
    answer = participant[0]
    print(answer)

    return answer


