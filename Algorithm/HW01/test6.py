def solution(s):
    if (len(s) > 50) :
        return -1
    if(not s.isalpha()) :
        return -1
    #string.isalpha() function for check alphabet
    answer = True
    check_p = 0
    check_y = 0
    
    for alphabet in s :
        if(alphabet in 'pPyY') :
            if (alphabet == 'p' or alphabet == 'P') :
                check_p +=1
            else :
                check_y += 1
    if (check_p != check_y) :
        return False
    else :
        return True