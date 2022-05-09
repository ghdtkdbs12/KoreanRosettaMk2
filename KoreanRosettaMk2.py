#|-----------------------------------------------------|
#|제목: Korean Rosetta Mark2                           |
#|제작: Made by Hong Seoung jin                        |
#|날짜: 2022년 제작                                     |
#|쟁점: Tkinter를 활용한 파이썬의 GUI제작 용이성 활용    |
#|기능: 한글과 영어를 Qwerty기준 변경                    |
#|-----------------------------------------------------|


#|--------------------import(시작)--------------------------------|
from hangul_utils import split_syllables, join_jamos #설치 코드 in CMD:pip install hangul-utils
import tkinter
from tkinter import *
from tkinter import messagebox #메세지박스 기능 추가
#|--------------------import(끝)--------------------------------|



#|--------------------창 설정(시작)--------------------------------|
window = tkinter.Tk();                 #창 설정
window.title("Korean Rosetta Mark.2 | Qwerty자판 기준 한영, 영한 전환 프로그램")  #창의 타이틀 명칭
window.geometry("700x700+100+100")     #창 크기와 생성위치
window.resizable(False,False)          #(창크기고정 false, 최대화 false)
window.option_add('*Font','맑은고딕')  #창 전체에 적용되는 옵션추가(폰트)
window.configure(background='#49A')
#|--------------------창 설정(끝)--------------------------------|



#|--------------------언어 테이블 (시작)--------------------------------|
# 자음-초성/종성(영어to한글)
cons = {'r':'ㄱ', 'R':'ㄲ', 's':'ㄴ', 'e':'ㄷ', 'E':'ㄸ', 'f':'ㄹ', 'a':'ㅁ', 'q':'ㅂ', 'Q':'ㅃ', 't':'ㅅ', 'T':'ㅆ',
           'd':'ㅇ', 'w':'ㅈ', 'W':'ㅉ', 'c':'ㅊ', 'z':'ㅋ', 'x':'ㅌ', 'v':'ㅍ', 'g':'ㅎ',
         #불필요한 shift 눌린 입력대비(자음)            
            'C':'ㅊ','V':'ㅍ','A':'ㅁ','S':'ㄴ','D':'ㅇ','F':'ㄹ','G':'ㅎ','Z':'ㅋ'
           }

# 모음-중성(영어to한글)
vowels = {'k':'ㅏ', 'o':'ㅐ', 'i':'ㅑ', 'O':'ㅒ', 'j':'ㅓ', 'p':'ㅔ', 'u':'ㅕ', 'P':'ㅖ', 'h':'ㅗ', 'hk':'ㅘ', 'ho':'ㅙ', 'hl':'ㅚ',
           'y':'ㅛ', 'n':'ㅜ', 'nj':'ㅝ', 'np':'ㅞ', 'nl':'ㅟ', 'b':'ㅠ',  'm':'ㅡ', 'ml':'ㅢ', 'l':'ㅣ',
            #불필요한 shift 눌린 입력대비(모음)           
            'H':'ㅗ','J':'ㅓ','I':'ㅑ','K':'ㅏ','L':'ㅣ','Y':'ㅛ','U':'ㅕ','I':'ㅑ','B':'ㅠ','N':'ㅜ','M':'ㅡ',
            }

# 자음-종성(영어to한글)
cons_double = {'rt':'ㄳ', 'sw':'ㄵ', 'sg':'ㄶ', 'fr':'ㄺ', 'fa':'ㄻ', 'fq':'ㄼ', 'ft':'ㄽ', 'fx':'ㄾ', 'fv':'ㄿ', 'fg':'ㅀ', 'qt':'ㅄ'}

# 한글to영어
KorToEng = {'ㅂ':'q', 'ㅃ':'Q', 'ㅈ':'w', 'ㅉ':'W', 'ㄷ':'e',
            'ㄸ':'E', 'ㄱ':'r', 'ㄲ':'R',  'ㅅ':'t', 'ㅆ':'T', 
            'ㅛ':'y', 'ㅕ':'u', 'ㅑ':'i', 'ㅁ':'a', 'ㄴ':'s', 
            'ㅇ':'d', 'ㄹ':'f', 'ㅎ':'g', 'ㅗ':'h', 'ㅓ':'j', 
            'ㅏ':'k', 'ㅣ':'l', 'ㅋ':'z', 'ㅌ':'x', 'ㅊ':'c', 
            'ㅍ':'v', 'ㅠ':'b', 'ㅜ':'n', 'ㅡ':'m', 'ㄳ':'rt', 
            'ㄵ':'wq', 'ㄶ':'sg', 'ㄺ':'fr', 'ㄻ':'fa', 'ㄼ':'fq', 
            'ㄽ':'ft', 'ㄾ':'fx', 'ㄿ':'fv', 'ㅀ':'fg', 
            'ㅄ':'qt', 'ㅐ':'o', 'ㅒ':'O', 'ㅔ':'p', 'ㅖ':'P', 
            'ㅚ':'h1', 'ㅙ':'ho', 'ㅘ':'hk', 'ㅝ':'nj', 
            'ㅞ':'np', 'ㅟ':'nl', 'ㅢ':'ml', }
#|--------------------언어 테이블 (끝)--------------------------------|



#|--------------------기능 설정(시작)--------------------------------|

#기능: Button_delete,버튼 클릭시 텍스트박스의 텍스트 전체 삭제
def TextBoxClear():
    Textbox_Iutput.delete("1.0","end") #입력 텍스트박스 모든 텍스트 삭제
    Textbox_Output_all.delete("1.0","end") #모두전환 텍스트박스 모든 텍스트 삭제
    Textbox_Output_hanEng.delete("1.0","end") #영어to한글전환 텍스트박스 모든 텍스트 삭제
    Textbox_Output_engHan.delete("1.0","end") #한글to영어전환 텍스트박스 모든 텍스트 삭제

#기능: Copy버튼을 누를시 모두전환 텍스트박스 복사
def TextboxCopy_all():
    inputValue=Textbox_Output_all.get("1.0","end-1c") #복사할 텍스트박스에서 가져오기
    print("Copy:" + inputValue) #(개발자 확인용)복사된 내용을 터미널에 출력
    window.clipboard_clear() #클립보드 비우기
    window.clipboard_append(inputValue) #클립보드에 값 받기
    
#기능: Copy버튼을 누를시 영어to한글 텍스트박스 복사
def TextboxCopy_engHan():
    inputValue=Textbox_Output_engHan.get("1.0","end-1c")
    print("Copy:" + inputValue) #(개발자 확인용)복사된 내용을 터미널에 출력
    window.clipboard_clear()  #클립보드 비우기
    window.clipboard_append(inputValue) #클립보드에 값 받기
    
#기능: Copy버튼을 누를시 한글to영어 텍스트박스 복사
def TextboxCopt_hanEng():
    inputValue=Textbox_Output_hanEng.get("1.0","end-1c")
    print("Copy:" + inputValue) #(개발자 확인용)복사된 내용을 터미널에 출력
    window.clipboard_clear()  #클립보드 비우기
    window.clipboard_append(inputValue) #클립보드에 값 받기
    
#기능: 설명버튼을 누르면 메세지 박스 띄우기
def showInforMessagebox(): #사용설명 안내 information messagebox
	messagebox.showinfo("사용방법 안내", "입력에 Qwerty자판기준으로 바꿀 내용을 입력합니다.\n Change버튼을 눌러서 번역을 실행합니다\n Clear버튼을 눌러서 텍스트박스를 비웁니다.\n copy버튼을 눌러서 번역된 내용을 복사합니다.\n\n 그나저나 설명서를 보는 사람이 있네요. \n 안 보셨으면 울 뻔!\n\n 제작: Kosta 242기 수료자 홍승진 \n 2022년 05월 제작완료 ")

#기능: 쿼티기준으로 번역함. [핵심기능]
def DoChangeLanguge():
    #(상단) 모든 종류 변환
    text = Textbox_Iutput.get("1.0","end")
    FinalResult = ''   #변환 결과
    vc = ''  #바꿔야할 글자를 처음 저장하는 변수
    print("입력받은 값text : " + text) #유지보수용
    # 1. 한글을 분해하여 나열한뒤 되돌려 놓기, 영어는 그대로 pass
    text = split_syllables(text)
    print("처리하는 값SampleText : " + text) #유지보수용
    # 2. 해당 글자가 자음인지 모음인지 확인
    for t in text:
        if t in cons : #자음-초성/종성
            vc+='c'
        elif t in vowels: #모음-중성
            vc+='v'
        elif t in KorToEng: #영어로 바꿀 한글일 경우
            vc+='k'
        else: #테이블에 포함안되는 예외
            vc+='!'
    # cvv → fVV / cv → fv / cc → dd 
    vc = vc.replace('cvv', 'fVV').replace('cv', 'fv').replace('cc', 'dd')
    #자음 + 모음(중성) + 모음(중성) -> fVV / 자음(초성/종성) + 모음 -> fv / 자음 + 자음  -> dd
	#위 vc를 replace하는 것은 글자 별로 조합을 파악하기 위해서 사용!
    # 3. 자음 / 모음 / 두글자 자음 에서 검색
    i = 0 #반복용 i
    while i < len(text): #텍스트의 길이가 0보다 크다면!
        v = vc[i] #fv!의 조합에 따른 배열 결과는 v[0]이다.
        t = text[i] 
        j = 1 #배열의 순서 +1씩 해주는 장치
        try: 
            if v == 'f' or v == 'c':   # 초성(f) & 자음(c) = 자음
                FinalResult+=cons[t] 
            elif v == 'V':   # 더블 모음
                FinalResult+=vowels[text[i:i+2]]
                j+=1
            elif v == 'v':   # 모음
                FinalResult+=vowels[t]
            elif v == 'd':   # 더블 자음
                FinalResult+=cons_double[text[i:i+2]]
                j+=1
            elif v == 'k': # to영어
                FinalResult+=KorToEng[t]
            else: # 기타
                FinalResult+=t
        except: # 혹시 번역이 안된 내용이 있다면!
            if v in cons: 
                FinalResult+=cons[t]
            elif v in vowels: 
                FinalResult+=vowels[t]
            elif v in KorToEng: 
                FinalResult+=KorToEng[t]
            else: 
                FinalResult+=t
        i += j
    print("패턴파악용 vc 값확인 : " + vc) #유지보수용
    Textbox_Output_all.delete("1.0","end") #결과 출력전 결과창 비우기.
    Textbox_Output_all.insert(INSERT, join_jamos(FinalResult)) #최종결과를 join_jamos로 한글 개별글씨를 합친 후 출력

    #(중간) 한글만 나오는 번역기능 부분
    text = Textbox_Iutput.get("1.0","end")
    FinalResult = ''   #변환 결과
    vc = ''  #바꿔야할 글자를 처음 저장하는 변수
    print("입력받은 값text : " + text) #유지보수용
    # 1. 한글을 분해하여 나열한뒤 되돌려 놓기, 영어는 그대로 pass
    text = split_syllables(text)
    print("처리하는 값SampleText : " + text) #유지보수용
    # 2. 해당 글자가 자음인지 모음인지 확인
    for t in text:
        if t in cons : #자음-초성/종성
            vc+='c'
        elif t in vowels: #모음-중성
            vc+='v'
        elif t in KorToEng: #영어로 바꿀 한글일 경우
            vc+='k'
        else: #테이블에 포함안되는 예외
            vc+='!'
    # cvv → fVV / cv → fv / cc → dd 
    vc = vc.replace('cvv', 'fVV').replace('cv', 'fv').replace('cc', 'dd')
    #자음 + 모음(중성) + 모음(중성) -> fVV / 자음(초성/종성) + 모음 -> fv / 자음 + 자음  -> dd
	#위 vc를 replace하는 것은 글자 별로 조합을 파악하기 위해서 사용!
    # 3. 자음 / 모음 / 두글자 자음 에서 검색
    i = 0 #반복용 i
    while i < len(text): #텍스트의 길이가 0보다 크다면!
        v = vc[i] #fv!의 조합에 따른 배열 결과는 v[0]이다.
        t = text[i] 
        j = 1 #배열의 순서 +1씩 해주는 장치
        try: 
            if v == 'f' or v == 'c':   # 초성(f) & 자음(c) = 자음
                FinalResult+=cons[t] 
            elif v == 'V':   # 더블 모음
                FinalResult+=vowels[text[i:i+2]]
                j+=1
            elif v == 'v':   # 모음
                FinalResult+=vowels[t]
            elif v == 'd':   # 더블 자음
                FinalResult+=cons_double[text[i:i+2]]
                j+=1
            else: # 기타
                FinalResult+=t
        except: # 혹시 번역이 안된 내용이 있다면!
            if v in cons: 
                FinalResult+=cons[t]
            elif v in vowels: 
                FinalResult+=vowels[t]
            else: 
                FinalResult+=t 
        i += j
    print("패턴파악용 vc 값확인 : " + vc) #유지보수용
    Textbox_Output_engHan.delete("1.0","end") #결과 출력전 결과창 비우기.
    Textbox_Output_engHan.insert(INSERT, join_jamos(FinalResult)) #최종결과를 join_jamos로 한글 개별글씨를 합친 후 출력
    
    #(하단) 영어만 나오는 번역기능 부분
    text = Textbox_Iutput.get("1.0","end")
    FinalResult = ''   #변환 결과
    vc = ''  #바꿔야할 글자를 처음 저장하는 변수
    print("입력받은 값text : " + text) #유지보수용
    # 1. 한글을 분해하여 나열한뒤 되돌려 놓기, 영어는 그대로 pass
    text = split_syllables(text)
    print("처리하는 값SampleText : " + text) #유지보수용
    # 2. 해당 글자가 자음인지 모음인지 확인
    for t in text:
        if t in cons : #자음-초성/종성
            vc+='c'
        elif t in vowels: #모음-중성
            vc+='v'
        elif t in KorToEng: #영어로 바꿀 한글일 경우
            vc+='k'
        else: #테이블에 포함안되는 예외
            vc+='!'
    # cvv → fVV / cv → fv / cc → dd 
    vc = vc.replace('cvv', 'fVV').replace('cv', 'fv').replace('cc', 'dd')
    #자음 + 모음(중성) + 모음(중성) -> fVV / 자음(초성/종성) + 모음 -> fv / 자음 + 자음  -> dd
	#위 vc를 replace하는 것은 글자 별로 조합을 파악하기 위해서 사용!
    # 3. 자음 / 모음 / 두글자 자음 에서 검색
    i = 0 #반복용 i
    while i < len(text): #텍스트의 길이가 0보다 크다면!
        v = vc[i] #fv!의 조합에 따른 배열 결과는 v[0]이다.
        t = text[i] 
        j = 1 #배열의 순서 +1씩 해주는 장치
        try: 
            if v == 'k': # to영어
                FinalResult+=KorToEng[t]
            else: # 기타
                FinalResult+=t
        except: # 혹시 번역이 안된 내용이 있다면!
            if v in KorToEng:
                FinalResult+=KorToEng[t]
            else: 
                FinalResult+=t 
        i += j
    print("패턴파악용 vc 값확인 : " + vc) #유지보수용
    Textbox_Output_hanEng.delete("1.0","end") #결과 출력전 결과창 비우기.
    Textbox_Output_hanEng.insert(INSERT, join_jamos(FinalResult)) #최종결과를 join_jamos로 한글 개별글씨를 합친 후 출력
    
#기능: any keyboard pressed되면 번역작동, 입력감지
def keyPressed(event):
    # 키보드 문자하나 출력
    DoChangeLanguge()
    print(event.char)
window.bind('<Key>', keyPressed) 
window.focus_set()# 키보드 포커를 갖게 한다

#|--------------------기능 설정(끝)--------------------------------|



#|--------------------UI 설정(시작)--------------------------------|

#라벨Lable_Title. 제목
Label_Title = tkinter.Label(window, text=" ", justify="left", background='#49A')
Label_Title.grid(row=0,column=1)

#라벨Lable_SubTitle. 보조 title 라벨
Lable_Input = tkinter.Label(window, text="Korean Rosetta by 홍승진 | ver. Mark.2 Python | Smart Pattern", anchor="w", font="궁서", background='#49A')
Lable_Input.grid(row=1,column=1)

#버튼Button_Howtouse. 입력된 내용을 바꾸는 것을 시행하는 버튼 -> 테스트필드 핵심!
Button_Howtouse = tkinter.Button(window, width=7, text="설명", command=showInforMessagebox)
Button_Howtouse.grid(row=1, column=3)

#라벨Lable_txtboxgap. 텍스트박스간 여백 라벨
Label_txtboxgap1 = tkinter.Label(window,height=1, background='#49A')
Label_txtboxgap1.grid(row=2,column=1)

#라벨Lable_txtb
Label_txtinforSupport = tkinter.Label(window, text="↓↓↓아래의 '입력' 텍스트박스에 전환될 내용을 타이핑하세요.↓↓↓", background='#49A')
Label_txtinforSupport.grid(row=3,column=1)

#버튼Button_Clear. 입력창 비우기버튼
Button_Clear = tkinter.Button(window, width=7, text="all Clear", command=TextBoxClear)
Button_Clear.grid(row=4, column=3)

#라벨Lable_Input. 입력텍스트박스 안내하는 라벨
Lable_Input = tkinter.Label(window, text="입력 : ", background='#49A')
Lable_Input.grid(row=4,column=0)

#텍스트박스Textbox_input. 입력창 텍스트박스
Textbox_Iutput = Text(window, width=60, height=5)
Textbox_Iutput.grid(row=4,column=1)

#라벨Lable_txtboxgap12. 1,2번째 텍스트박스간 여백 라벨
Label_txtboxgap12 = tkinter.Label(window,height=1, background='#49A')
Label_txtboxgap12.grid(row=5,column=1)

#라벨Label_Output. 결과창 안내 라벨
Lable_Onput = tkinter.Label(window, text="결과 : ", background='#49A')
Lable_Onput.grid(row=6,column=0)

#텍스트박스Textbox_Output. 결과창 텍스트박스
Textbox_Output_all = Text(window, width=60, height=5)
Textbox_Output_all.grid(row=6,column=1)

#라벨Label_tellHowto2. 결과텍스트박스 내용물안내 라벨
Label_tellHowto2 = tkinter.Label(window, text=" ➜'결과'에는 한글은 영어로, 영어는 한글로 바뀝니다.", background='#49A')
Label_tellHowto2.grid(row=7,column=1)

#라벨Lable_txtboxgap2. 텍스트박스와 버튼 사이의 여백 라벨
Label_txtboxgap1 = tkinter.Label(window, width=1, background='#49A')
Label_txtboxgap1.grid(row=6,column=2)

#버튼Button_copy. 결과창의 값 복사하는 버튼
Button_Clear = tkinter.Button(window, width=7, text="Copy" ,command=TextboxCopy_all)
Button_Clear.grid(row=6, column=3)

#라벨Lable_txtboxgap23. 2,3번째 텍스트박스간 여백 라벨
Label_txtboxgap2 = tkinter.Label(window,height=1, background='#49A')
Label_txtboxgap2.grid(row=8,column=1)

#라벨Label_Output. 한영 결과창 안내 라벨
Lable_Onput_hanEng = tkinter.Label(window, text="영어 : ", background='#49A')
Lable_Onput_hanEng.grid(row=9,column=0)

#텍스트박스Textbox_Output. 한영 결과창 텍스트박스
Textbox_Output_hanEng = Text(window, width=60, height=5)
Textbox_Output_hanEng.grid(row=9,column=1)

#버튼Button_copy_hanEng. 한영 결과창의 값 복사하는 버튼
Button_Clear_hanEng = tkinter.Button(window, width=7, text="Copy" ,command=TextboxCopt_hanEng)
Button_Clear_hanEng.grid(row=9, column=3)

#라벨Label_tellHowto3. 결과텍스트박스 내용물안내 라벨
Label_tellHowto3 = tkinter.Label(window, text=" ➜'영어'에는 한글만 영어로 바뀝니다.", background='#49A')
Label_tellHowto3.grid(row=10,column=1)

#라벨Lable_txtboxgap23. 3,4번째 텍스트박스간 여백 라벨
Label_txtboxgap3 = tkinter.Label(window,height=1, background='#49A')
Label_txtboxgap3.grid(row=11,column=1)

#라벨Label_Output. 한영 결과창 안내 라벨
Lable_Onput_engHan = tkinter.Label(window, text="한글 : ", background='#49A')
Lable_Onput_engHan.grid(row=12,column=0)

#텍스트박스Textbox_Output. 영한 결과창 텍스트박스
Textbox_Output_engHan = Text(window, width=60, height=5)
Textbox_Output_engHan.grid(row=12,column=1)

#라벨Label_tellHowto4. 결과텍스트박스 내용물안내 라벨
Label_tellHowto4 = tkinter.Label(window, text=" ➜'한글'에는 영어만 한글로 바뀝니다.", background='#49A')
Label_tellHowto4.grid(row=13,column=1)

#버튼Button_copy_engHan. 영한 결과창의 값 복사하는 버튼
Button_Clear_engHan = tkinter.Button(window, width=7, text="Copy" ,command=TextboxCopy_engHan)
Button_Clear_engHan.grid(row=12, column=3)

#라벨Lable_txtboxgap. 텍스트박스와 최하단 레벨간 간격 라벨
Label_txtboxgap4 = tkinter.Label(window,height=1, background='#49A')
Label_txtboxgap4.grid(row=14,column=1)

#라벨Lable_. 최하단 광고라벨
Label_adver = tkinter.Label(window,text="(아무튼)기술지원 by 이창현코딩연구소", background='#49A')
Label_adver.grid(row=15,column=1)

#GUI 시작
window.mainloop()                                    
#|--------------------UI 설정(끝)--------------------------------|


