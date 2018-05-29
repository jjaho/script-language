from tkinter import*
from tkinter import font
import tkinter.messagebox
g_Tk = Tk()
g_Tk.geometry("1000x600+750+200")
DataList = []

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
    global SearchListBox

# 메뉴 검색에 따른 텍스트 정보가 나오는 창
def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x = 375, y = 200)
    TempFont = font.Font(g_Tk, size = 10, family = 'Consolas')
    RenderText = Text(g_Tk, width = 40, height = 30, borderwidth = 12,
                      relief = 'ridge', yscrollcommand = RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x = 10, y = 180)
    RenderTextScrollbar.config(command = RenderText.yview)
    RenderTextScrollbar.pack(side = RIGHT, fill = BOTH)
    RenderText.configure(state = 'disabled')

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
    TempFont = font.Font(g_Tk, size = 15, weight = 'bold', family = 'Consolas')
    InputLabel2 = Entry(g_Tk, font = TempFont, width = 20, borderwidth = 12,
                       relief = 'ridge')
    InputLabel2.pack()
    InputLabel2.place(x = 350, y = 105)

# 휴게소 검색 버튼 칸
def InitSearchButton2():
    TempFont = font.Font(g_Tk, size = 12, weight = 'bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text = "검색", command = SearchButtonAction2)
    SearchButton.pack()
    SearchButton.place(x = 610, y = 110)

# 휴게소 검색을 눌렀을때 나오는 것
def SearchButtonAction2():
    global SearchListBox2

# 휴게소 검색에 따른 텍스트 정보가 나오는 창
def InitRenderText2():
    global RenderText2
    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x = 375, y = 200)
    TempFont = font.Font(g_Tk, size = 10, family = 'Consolas')
    RenderText2 = Text(g_Tk, width = 40, height = 30, borderwidth = 12,
                      relief = 'ridge', yscrollcommand = RenderTextScrollbar.set)
    RenderText2.pack()
    RenderText2.place(x = 350, y = 180)
    RenderTextScrollbar.config(command = RenderText2.yview)
    RenderTextScrollbar.pack(side = RIGHT, fill = BOTH)
    RenderText2.configure(state = 'disabled')

# 이메일 보내기 버튼 칸
def InitSendEmailButton():
    TempFont = font.Font(g_Tk, size = 20, weight = 'bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text = "이메일 보내기", command = SearchButtonAction3)
    SearchButton.pack()
    SearchButton.place(x = 720, y = 80)

# 이메일 보내기를 눌렀을때 나오는 것
def SearchButtonAction3():
    global SearchListBox3

InitTopText() # 제목
InitSearchMenu() # 메뉴 로고 창
InitInputLabel() # 메뉴 검색어 창
InitSearchButton() # 메뉴 검색 버튼
InitRenderText() # 메뉴 검색에 따른 텍스트 정보 보여주는 창
InitSearchRestArea() # 휴게소 로고 창
InitInputLabel2()# 휴게소 검색어 창
InitSearchButton2()# 휴게소 검색 버튼
InitRenderText2()# 휴게소 검색에 따른 텍스트 정보 보여주는 창
InitSendEmailButton()# 이메일 보내기 버튼
g_Tk.mainloop()