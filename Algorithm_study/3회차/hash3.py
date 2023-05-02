# 전화번호 목록: https://school.programmers.co.kr/learn/courses/30/lessons/42577


'''
전화번호 리스트를 정렬하고, 인접한 두 전화번호를 비교하여 접두어가 되는지 확인
파이썬 기본 정렬 알고리즘인 Timsort를 사용하면, 최악의 경우에도 O(N log N)의 시간 복잡도
인접한 두 전화번호를 비교하여 접두어가 되는지 확인하는 부분은 정렬된 리스트에서 순차적으로 검색하므로, 시간 복잡도는 O(N)
따라서, 전체적인 시간 복잡도는 O(N log N) + O(N) = O(N log N) 
''' 
def solution1(phone_book):
    
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    
    return True

'''
해시 테이블에 모든 전화번호 추가 후 각 전화번호의 접두어를 해시 태이블에서 검색하여 접두어가 존재하는지 확인
제한사항으로 각 전화번호의 길이는 1 이상 20 이하이기 때문에 시간 복잡도는 O(N)
'''
def solution2(phone_book):
    dic = {}

    # 해시 테이블에 모든 전화번호 추가
    for phone_number in phone_book:
        dic[phone_number] = 1

    # 각 전화번호의 접두어를 해시 테이블에서 검색하여 접두어가 존재하는지 확인
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            prefix = phone_number[:i]
            if prefix in dic:
                return False
    
    return True

'''
정렬하는 부분에서의 시간 복잡도는 O(N log N) 그리고 zip()함수를 사용하여 phone_book과 phone_book[1:]를 순회하는 부분에서의 시간 복잡도는 O(N) 
startswith() 함수의 시간 복잡도는 O(M)입니다. M은 비교하는 문자열의 길이
제한 사항으로 길이가 20이하 이므로 전체적인 알고리즘의 시간 복잡도는 O(N log N)
'''
def solution3(phone_book):

    phone_book.sort()

    for prefix, phone_number in zip(phone_book, phone_book[1:]):
        if phone_number.startswith(prefix):
            return False
            
    return True