# 전화번호 목록: https://school.programmers.co.kr/learn/courses/30/lessons/42577


# O(n log n) 
def solution1(phone_book):
    
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    
    return True

# O(n)
def solution2(phone_book):
    hash_table = {}

    # 해시 테이블에 모든 전화번호 추가
    for phone_number in phone_book:
        hash_table[phone_number] = 1

    # 각 전화번호의 접두어를 해시 테이블에서 검색하여 접두어가 존재하는지 확인
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            prefix = phone_number[:i]
            if prefix in hash_table:
                return False
    
    return True

# O(n log n) 
def solution3(phone_book):

    phone_book.sort()

    for prefix1, prefix2 in zip(phone_book, phone_book[1:]):
        if prefix2.startswith(prefix1):
            return False
            
    return True