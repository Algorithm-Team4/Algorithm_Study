def solution(phone_book):
    PhoneBookDictionary = {}
    #딕셔너리 생성

    for phone_number in phone_book:
        PhoneBookDictionary[phone_number] = 1
        
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            print(temp +"\n")
            if (temp in PhoneBookDictionary) and (temp != phone_number):
                return False

    return True

# 테스트 케이스
print(solution(["119", "97674223", "1195524421"])) # false
print(solution(["123","456","789"])) # true
print(solution(["12","123","1235","567","88"])) # false
