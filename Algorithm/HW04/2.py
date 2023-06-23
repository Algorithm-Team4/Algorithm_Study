def solution(s):
    if (len(s) % 2 == 1) :
        return False
    if (s[0] == ")") :
        return False
    #홀수면 괄호쌍이 이뤄지지 않아서 조건 충족X
    #왼쪽 소괄호로 시작하지 않으면 조건 충족 X(닫히지 않음)
    #모든 괄호가 닫혔는지 확인하는 문제
    check_arr = []

    #왼쪽 괄호를 배열에 넣고 오른쪽 괄호가 나올 때마다 그걸 빼내는 형식
    for parenthesis in s :
        if(parenthesis == "(") :
            check_arr.append(parenthesis)
        if(parenthesis == ")") :
            if(len(check_arr) == 0) :
                return False
            #왼쪽 괄호가 오른쪽 괄호보다 안나올 경우 조건 충족x(꺼낼 왼쪽 괄호가 없음)
            check_arr.pop()

    #왼쪽 괄호가 남았을 경우엔 괄호쌍이 다 이뤄지지 않은 것
    if(len(check_arr) != 0) :
        return False
    return True