
dict_01 = {}

def input_eng(eng):
    kor = input("단어 %s 뜻 : "%eng)
    dict_01[eng] = kor
    print("단어 %s 등록되었습니다."%eng)

def make_dict():
    while True:
        eng = input(" 등록할 단어를 입력하세요 ( 등록종료는 q 입력 ) : ")
        if eng == 'q':
            print("단어 등록을 종료합니다.")
            break

        elif eng not in dict_01:
            input_eng(eng)
        else:
            print("단어 %s 의 는 사전에 있습니다."
                  "뜻은 %s 입니다"%(eng,dict_01[eng]))
    print(dict_01)

def search():
    eng = input("검색할 단어를 입력하세요 : ")
    if eng in dict_01:
        print("%s 의 뜻은 %s 입니다."%(eng,dict_01[eng]))
    elif eng not in dict_01:
        answer = input("%s 은 사전에 없습니다. 추가하시겠습니끼? Y/N :"%eng)
        if answer == 'Y':
            input_eng(eng)
        else:
            print("검색을 종료합니다.")
            pass


print("-----------------------------------------------")

while True:
    sel = input("사용하실 메뉴를 선택하세요 "
                "1. 단어 등록 "
                "2. 단어 검색 "
                "3. 종료   ")
    if sel == '3':
        print(dict_01)
        print("종료합니다")
        break
    elif sel == '1':
        make_dict()
    else:
        search()



















