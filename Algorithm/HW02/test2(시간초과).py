def solution(participant, completion):
    # if (len(participant) < 1 or len(participant) > 100000) :
    #     return -1
    # if (len(completion) != len(participant) - 1) :
    #     return -1
    #for checker in participant :
    #   if (len(checker) > 20 or checker < 1) :
    #       return -1 
    
    answer = ''
    check_list = []
    for person in participant :
        if (participant.count(person) != completion.count(person)) :
            answer = person
    return answer
