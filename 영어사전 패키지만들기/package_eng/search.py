from dictionary import dict_02
from make import *


def search():
    eng = input("검색할 단어를 입력하세요 : ")
    if eng in dict_02:
        print("%s 의 뜻은 %s 입니다."%(eng,dict_02[eng]))
    elif eng not in dict_02:
        answer = input("%s 은 사전에 없습니다. 추가하시겠습니끼? Y/N :"%eng)
        if answer == 'Y':
            input_eng(eng)
        else:
            print("검색을 종료합니다.")
            pass
