from dictionary import dict_02

def input_eng(eng):
    kor = input("단어 %s 뜻 : "%eng)
    dict_02[eng] = kor
    print("단어 %s 등록되었습니다."%eng)

def make_dict():
    while True:
        eng = input(" 등록할 단어를 입력하세요 ( 등록종료는 q 입력 ) : ")
        if eng == 'q':
            print("단어 등록을 종료합니다.")
            break

        elif eng not in dict_02:
            input_eng(eng)
        else:
            print("단어 %s 의 는 사전에 있습니다."
                  "뜻은 %s 입니다"%(eng,dict_02[eng]))
    print(dict_02)


