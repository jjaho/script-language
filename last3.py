from tkinter import*
from tkinter import font
import tkinter.messagebox

#파싱용
import urllib.request
import string
import codecs
import smtplib
# 이메일 암호화
import base64
# 이메일 보내기
from xml.dom.minidom import *
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

g_Tk = Tk()
g_Tk.geometry("1000x600+750+200")
DataList = []

# 암호화
def Base64_Encode(s):
    return base64.b64encode(s.encode('utf-8'))

def Base64_Decode(b):
    return base64.b64decode(b).decode('utf-8')

def sendMail(ReviceMail, Subject, Content):
    s = smtplib.SMTP("smtp.gmail.com",587) #SMTP 서버 설정
    s.starttls() #STARTTLS 시작
    s.login( Base64_Decode("YW5reW9uZzk5QGdtYWlsLmNvbQ=="),Base64_Decode("YW5reW9uZzk="))
    contents = Content
    msg = MIMEText(contents, _charset='euc-kr')
    msg['Subject'] = Subject
    msg['From'] = Base64_Decode("YW5reW9uZzk5QGdtYWlsLmNvbQ==")
    msg['To'] = ReviceMail
    s.sendmail( Base64_Decode("YW5reW9uZzk5QGdtYWlsLmNvbQ==") , ReviceMail, msg.as_string())

# API공유키
global key
key = "ESfoqLgZIPMdxDVdj9b%2FHG4IM%2FxzY2rgg0bcScQR2HZAI7wpwnBxf10VBUMdNIch2HrhKzD%2FCgOEzg400RDeAw%3D%3D"

#메뉴검색해 휴게소 메뉴가져오기함수
def getList():
    global AllmenuList
    global AllrestList
    global AllrestList2
    global AllmenuList2
    AllmenuList = []
    AllrestList = []
    AllrestList2 = []
    AllmenuList2 = []
    # 1~10 까지 한 이유는 xml 에서 2100개가 있고 999개 까지만 검색이 되므로
    for i in range(1, 10):
        print(i)
        # OpenAPI를 불러와서 String으로 넣어준다. i는 페이지 수
        getParsingXMLString = openAPItoXML("http://data.ex.co.kr/exopenapi/restinfo/restBestfoodList?serviceKey=",
                                           "&pageNo=" + str(i) + "&numOfRows=999&pageSize=999&type=xml")
        getParsingXMLString2 = openAPItoXML("http://data.ex.co.kr/exopenapi/restinfo/restBestfoodList?serviceKey=",
                                            "&pageNo=" + str(i) + "&numOfRows=999&pageSize=999&type=xml")
        # XML Mother, Child 를 가져와서 List에 넣어준다.
        menuList = addParsingDicList(getParsingXMLString, "list", "foodNm")
        restList = addParsingDicList(getParsingXMLString, "list", "stdRestNm")
        restList2 = addParsingDicList(getParsingXMLString2, "list", "stdRestNm")
        menuList2 = addParsingDicList(getParsingXMLString2, "list", "foodNm")

        # 각 가져온 List를 전체 List로 넣어준다.
        AllmenuList = AllmenuList + menuList
        AllrestList = AllrestList + restList
        AllrestList2 = AllrestList2 + restList2
        AllmenuList2 = AllmenuList2 + menuList2

# 파시을 편하게 하기 위하여 Open APi 주소를 넣어서 Stirng 데이터로 넣어줌.
def openAPItoXML(server, value):
    global key
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]
    # ↑ User-Agent를 입력하지 않을경우 naver.com 에서 정상적인 접근이 아닌것으로 판단하여 차단을 한다.
    data = ""
    urldata = server + key + value
    with opener.open(urldata) as f:
        data = f.read(300000).decode('utf-8') # 300000bytes 를 utf-8로 변환하여 읽어온다.  변환이 없을경우 unicode로 받아온다.
    return data

def addParsingDicList(xmlData, motherData, childData):
    # 파싱된 데이터를 리스트에 넣어서 리턴 한다.
    doc = parseString(xmlData)
    siGunGuList = doc.getElementsByTagName(motherData)
    signguCdSize = len(siGunGuList)
    list = []
    for index in range(signguCdSize):
        mphms = siGunGuList[index].getElementsByTagName(childData)
        list.append(str(mphms[0].firstChild.data))
    return list

# 제목 칸
def InitTopText():
    TempFont = font.Font(g_Tk, size = 20, weight = 'bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text = "[휴게소 먹거리 검색 App]")
    MainText.place(x = 340)

# 메뉴 로고 칸
def InitSearchMenu():
    global SearchListBox
    TempFont = font.Font(g_Tk, size = 15, weight = 'bold', family = 'Consolas')
    SearchListBox = Listbox(g_Tk, font = TempFont, activestyle = 'none',
                           width = 25, height = 1, borderwidth = 12, relief = 'ridge')
    SearchListBox.insert(1, "메뉴 검색에 따른 휴게소")
    SearchListBox.pack()
    SearchListBox.place(x = 10, y = 50)

# 메뉴 검색 글쓰는 칸
def InitInputLabel():
    global InitInputLabel
    global InputLabel
    TempFont = font.Font(g_Tk, size = 15, weight = 'bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width = 20, borderwidth = 12,
                       relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x = 10, y = 105)

# 메뉴 검색 버튼 칸
def InitSearchButton():
    TempFont = font.Font(g_Tk, size = 12, weight = 'bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text = "검색", command = SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x = 270, y = 110)

# 메뉴 검색을 눌렀을때 나오는 것
def SearchButtonAction():
    global InputLabel
    global RenderList
    global getParsingXMLString
    number = 0
    RenderList.delete(0, END)
    for name in AllmenuList:
        number = number + 1
        if(name.find(InputLabel.get()) != -1):
            RenderList.insert(END, AllrestList[number].replace("휴게소", "") + " : " + name)


# 메뉴 검색에 따른 텍스트 정보가 나오는 창
def InitRenderList():
    global RenderList
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    RenderList = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=25, height=16, borderwidth=12, relief='ridge')
    RenderList.pack()
    RenderList.place(x=10, y=180)

# 휴게소 로고 칸
def InitSearchRestArea():
    global SearchListBox
    TempFont = font.Font(g_Tk, size = 15, weight = 'bold', family = 'Consolas')
    SearchListBox = Listbox(g_Tk, font = TempFont, activestyle = 'none',
                           width = 25, height = 1, borderwidth = 12, relief = 'ridge')
    SearchListBox.insert(1, "휴게소 검색에 따른 메뉴")
    SearchListBox.pack()
    SearchListBox.place(x = 350, y = 50)

# 휴게소 검색 글쓰는 칸
def InitInputLabel2():
    global InitInputLabel2
    global InputLabel2
    TempFont = font.Font(g_Tk, size = 15, weight = 'bold', family = 'Consolas')
    InputLabel2 = Entry(g_Tk, font = TempFont, width = 20, borderwidth = 12,
                       relief = 'ridge')
    InputLabel2.pack()
    InputLabel2.place(x = 350, y = 105)

# 휴게소 검색 버튼 칸
def InitSearchButton2():
    TempFont = font.Font(g_Tk, size = 12, weight = 'bold', family = 'Consolas')
    SearchButton2 = Button(g_Tk, font = TempFont, text = "검색", command = SearchButtonAction2)
    SearchButton2.pack()
    SearchButton2.place(x = 610, y = 110)

# 휴게소 검색을 눌렀을때 나오는 것
def SearchButtonAction2():
    global InputLabel2
    global RenderList2
    global getParsingXMLString2
    number2 = 0
    RenderList2.delete(0, END)
    for name2 in AllrestList2:
        number2 = number2 + 1
        if(name2.find(InputLabel2.get()) != -1):
            RenderList2.insert(END, AllmenuList2[number2].replace("메뉴", "") + " : " + name2)

# 휴게소 검색에 따른 텍스트 정보가 나오는 창
def InitRenderList2():
    global RenderList2
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    RenderList2 = Listbox(g_Tk, font=TempFont, activestyle='none',
                         width=25, height=16, borderwidth=12, relief='ridge')
    RenderList2.pack()
    RenderList2.place(x=350, y=180)

# 이메일 쓰는 텍스트창
def InitInputEmail():
    global inputEmailText
    TempFont = font.Font(g_Tk, size = 15, weight = 'bold', family = 'Consolas')
    inputEmailText = Entry(g_Tk, font = TempFont, width = 20, borderwidth = 12,
                       relief = 'ridge')
    inputEmailText.pack()
    inputEmailText.place(x = 700, y = 50)

# 이메일 보내기 버튼 칸
def InitSendEmailButton():
    TempFont = font.Font(g_Tk, size = 20, weight = 'bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text = "이메일 보내기", command = SearchButtonAction3)
    SearchButton.pack()
    SearchButton.place(x = 720, y = 100)

# 이메일 보내기를 눌렀을때 나오는 것
def SearchButtonAction3():
    global inputEmailText
    global SearchListBox3
    global RenderList
    global RenderList2

    ContentString = ""

    for value in range(0, RenderList.size()):
        ContentString = ContentString + RenderList.get(value) + str("\n")
    for value in range(0, RenderList2.size()):
        ContentString = ContentString + RenderList2.get(value) + str("\n")

    if ( inputEmailText.get() != ""):
        sendMail(str(inputEmailText.get()), "휴게소 먹거리 정보", ContentString)


getList() # 시작 전 먼저 XML 데이터를 가져와야지 검색이 빠르게 진행 된다.
InitTopText() # 제목
InitSearchMenu() # 메뉴 로고 창
InitInputLabel() # 메뉴 검색어 창
InitSearchButton() # 메뉴 검색 버튼
InitRenderList() # 메뉴 검색에 따른 텍스트 정보 보여주는 창
InitSearchRestArea() # 휴게소 로고 창
InitInputLabel2()# 휴게소 검색어 창
InitSearchButton2()# 휴게소 검색 버튼
InitRenderList2()# 휴게소 검색에 따른 텍스트 정보 보여주는 창
InitInputEmail()# 이메일 입력창
InitSendEmailButton()# 이메일 보내기 버튼
g_Tk.mainloop()