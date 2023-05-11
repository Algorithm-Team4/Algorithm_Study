def solution(s):
    if (len(s) % 2 == 1) :
        return False
    if (s[0] == ")") :
        return False
    #홀수면 괄호쌍이 이뤄지지 않아서 조건 충족X
    #왼쪽 소괄호로 시작하지 않으면 조건 충족 X(닫히지 않음)
    check_arr = []

    for parenthesis in s :
        if (parenthesis == "(") :
            if (len(check_arr) == 0) :
                check_arr.append(parenthesis)
            else :
                return False
        if (parenthesis == ")") :
            if (len(check_arr) == 1) :
                check_arr.pop()
            else :
                return False
                
    return True