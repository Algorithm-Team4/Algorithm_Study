def solution(participant, completion):
    # if (len(participant) < 1 or len(participant) > 100000) :
    #     return -1
    # if (len(completion) != len(participant) - 1) :
    #     return -1
    #for checker in participant :
    #   if (len(checker) > 20 or checker < 1) :
    #       return -1 
    answer = ''
    participant_dictionary = {}
    for person in participant:
        if person in participant_dictionary:
            participant_dictionary[person] += 1
        else:
            participant_dictionary[person] = 1
            
    for person in completion:
        participant_dictionary[person] -= 1
    for person, counter in participant_dictionary.items():
        if counter > 0:
            answer = person
    return answer
