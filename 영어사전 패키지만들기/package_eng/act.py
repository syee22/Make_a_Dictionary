from dictionary import dict_02
from make import *
from search import *

print("-----------------------------------------------")

while True:
    sel = input("사용하실 메뉴를 선택하세요 "
                "1. 단어 등록 "
                "2. 단어 검색 "
                "3. 종료   ")
    if sel == '3':
        print(dict_02)
        print("종료합니다")
        break
    elif sel == '1':
        make_dict()
    else:
        search()
