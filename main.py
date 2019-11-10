from endic import Endic
import os.path
import sys 

choice = 0
title = ""
findtitle=""
num = 0
makedic = dict()
word = ""
word_meaning = ""
modification_check = 'Y'

# ===============================출력부분공통
print("-"*20)
print("{:^20}".format("<단어장 만들기 프로그램>"))
print("-"*20)
print("안녕하세요! 단어장 만드는 프로그램입니다.")
print("여기서 단어장을 생성하면 txt 파일로도 받아볼 수 있습니다.")
print("-"*20)

choice = int(input("1)단어장 생성하기 2)단어장 보기 3) 그만 나가기 :_\b"))

# ==================================단어장 생성하기
if choice == 1:

    print("-"*20)
    print("{}".format("1)단어장 생성하기"))
    print('-'*20)
    print("• 단어장 생성하기를 선택해 주셨네요!")
    title = input("• 단어장의 제목을 정해주세요:")
    num = int(input("• 단어 입력 개수를 정해주세요:"))
    print("-"*20)

    print("지금부터 {}개의 단어를 입력받겠습니다.".format(num))
    print("단어와 뜻은 스페이스로 구분해주세요.")
    for i in range(num):
        word,meaning = input(str(i+1)+".단어 // 뜻:" ).split()
        makedic[word]=meaning
    print(makedic)
    print("-"*20)

    endic = Endic(title, makedic)
    f = open("dictionaryread/"+title+".txt",'w')
    num =0

    for word, meaning in makedic.items():
        sentence = "{}. 단어: {}\t 뜻: {}".format(num+1, word, meaning)
        num +=1
        f.writelines(sentence+'\n')

    print("{}이 완성되었습니다.{}에 저장되어 있으니 txt 파일로도 받아보세요!".format(title,"dictionaryread/"+title+".txt"))
    f.close()

# ==================================단어장 보여주기
elif choice == 2:
    print("-"*20)
    print("{}".format("2)단어장 보여주기"))
    print('-'*20)
    print("• 단어장 보기를 선택해 주셨네요!")
    # print(Endic)
    path='./dictionaryread/'
    filelist = os.listdir(path)
    print(" ", filelist)
    findtitle = input("어떤 단어장을 열까요?")

    print('-'*20)
    file = 'dictionaryread/'+findtitle+'.txt'
    
    if os.path.isfile(file):
        print("{}에 있는 단어들 입니다.".format(findtitle))
        f = open(file, 'r+')
        print("단어\t뜻")
        inlist = f.readlines()
        for k in inlist:
            print(k)
        print('='*20)
        modification= input("혹시 수정하고 싶은 단어가 있나요?(Y/N)")
        
        # ==================================단어장 수정하기
        if modification == 'Y':
            while modification_check != 'N':
                print("-"*20)
                print("{}".format("3)단어장 수정하기"))
                print('-'*20)
                modification_num = int(input("몇 번째 단어를 수정하실 건가요?_\b"))
                print('-'*20)

                modification_word = input("수정할 단어)")
                modification_meaning = input("수정할 뜻)")
                print('-'*20)
                
                f.seek(0)
                f.truncate()
                f.close()

                fw = open(file,'w')
                for i in range(len(inlist)):
                    if (modification_num == int(inlist[i].split('.')[0])):
                        sent =  "{}. 단어: {}\t 뜻: {}".format(modification_num, modification_word, modification_meaning)
                        fw.writelines(sent+'\n')
                        print(sent)
                    else:
                        fw.writelines(inlist[i])
                        print(inlist[i].split('.'))

                modification_check = input("수정내용 저장할까요?")
                
                if modification_check == 'Y':
                    print("잘 저장 되었습니다.")
                    sys.exit()
                else:
                    modification_check = 'N'
                fw.close()
    else:    
        print("그런 파일은 없습니다.")

elif choice == 3:
    sys.exit()
