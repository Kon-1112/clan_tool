import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import random
import pyautogui
import time
import sys

game_data = []
member_data = []
set_list = []

def game_append():
    if entry_1.get()=="" or entry_1.get()==" " or entry_1.get()=="  " or entry_1.get()=="   ":
        messagebox.showerror("エラー","要素が空白もしくはスペースのみです")
        print("log : ERROR_空白")
        return
    else:
        game_data.append(entry_1.get())
        print(f"log : list {game_data}")
        entry_1.delete(0,tk.END)
def game_output():
    if len(game_data)==0:
        messagebox.showerror('エラー','要素が空です')
        print("log : ERROR_空要素")
    elif len(game_data)==1:
        messagebox.showerror('エラー','1つの要素では意味がありません')
        print("log : ERROR_要素不足")
    else:
        len_num = len(game_data)
        print(f"log : list_len {len_num}")
        game = random.randint(0,int(len_num-1))
        messagebox.showinfo('結果発表♪','OKを押すと結果が表示されます')
        messagebox.showinfo("結果発表♪",f"結果は {game_data[game]} となりました!")
def member_append():
    if entry_2.get()=="" or entry_2.get()==" " or entry_2.get()=="  " or entry_2.get()=="   ":
        messagebox.showerror("エラー","要素が空白もしくはスペースのみです")
        print("log : ERROR_空白")
        return
    else:
        member_data.append(entry_2.get())
        print(f"log : list {member_data}")
        entry_2.delete(0,tk.END)
def member_output():
    member_len = len(member_data)
    print("log : ERROR_空要素")
    if member_len == 0:
        messagebox.showerror('エラー','データが1つも登録されていません')            
    else:
        if member_len == 1:
            messagebox.showerror('エラー','1つの要素ではチームを分けれません')            
        else:
            try:
                random_sample = random.sample(range(member_len),member_len)
                who = 0
                for who in random_sample:
                    set_list.append(member_data[who])
                team_num_int = 2
                print(member_data)
                one_team = int(member_len/team_num_int)
                A_TEAM = ','.join(set_list[0:one_team])
                B_TEAM = ','.join(set_list[one_team:member_len])
                messagebox.showinfo('結果発表♪','OKを押すと結果が表示されます')
                messagebox.showinfo("結果発表♪",f"GOOD LUCK HAVE FUN !\n A TEAM : {A_TEAM}\n B TEAM : {B_TEAM}")
                print(f"log : list {set_list}")
                set_list.clear()
                who=0
            except:
                print("エラー")
def Reset():
    if len(game_data)==0 and len(member_data)==0:
        messagebox.showerror('エラー','データが1つも登録されていません')
    elif entry_2.get()=="例:R6S" or entry_1.get() =="例:R6S":
        entry_1.delete(0,tk.END)
        entry_2.delete(0,tk.END)
    else:
        game_data.clear()
        member_data.clear()
        set_list.clear()
        entry_1.delete(0,tk.END)
        entry_2.delete(0,tk.END)
        messagebox.showinfo("(^▽^)/","リセットしました")
        print("log : Reset success")

def R6S():
    pyautogui.press("winleft")
    time.sleep(0.3)
    pyautogui.typewrite("Rainbow six siege")
    time.sleep(0.3)
    pyautogui.press("enter")	

def APEX():
    pyautogui.press("winleft")
    time.sleep(0.3)
    pyautogui.typewrite("Apex Legends")
    time.sleep(0.3)
    pyautogui.press("enter")
    
def Valorant():
    pyautogui.press("winleft")
    time.sleep(0.3)
    pyautogui.typewrite("Valorant")
    time.sleep(0.3)
    pyautogui.press("enter")

def Discord():
    pyautogui.press("winleft")
    time.sleep(0.3)
    pyautogui.typewrite("discord")
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(1.2)
    pyautogui.hotkey("winleft","up")

def Memo():
    pyautogui.press("winleft")
    time.sleep(0.3)
    pyautogui.typewrite("memo")
    time.sleep(0.3)
    pyautogui.press("enter")
def OutPlayed():
    pyautogui.press("winleft")
    time.sleep(0.3)
    pyautogui.typewrite("Outplayed")
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(1.2)
    pyautogui.hotkey("winleft","up")

def exit_sys():
    sys.exit( )
    print('exit')

def DemoRun():
    screen_x,screen_y = pyautogui.size()
    curmus_x,curmus_y = pyautogui.position()
    pyautogui.hotkey("winleft","up")
    print (u"画面サイズ [" + str(screen_x) + "]/[" + str(screen_y) + "]")
    print (u"現在のマウス位置 [" + str(curmus_x) + "]/[" + str(curmus_y) + "]")
    messagebox.showinfo('DEMOモード 案内1',f'貴方のモニターの解像度とマウス座標を取得しました。\n解像度 {str(screen_x)}×{str(screen_y)}\n現在の座標 {str(curmus_x)}×{str(curmus_y)}\n挙動がおかしく見えますが、正常です(^▽^)/')
    messagebox.showinfo('DEMOモード 案内2',f'テロップが出たら画面に従ってくださいね\nデモではRainbow Six SiegeとApex LegendsとValorantをランダムで一つ選択します\n処理中はマウスに触れないでください\nOKを押したら始まります')
    pyautogui.hotkey("winleft","up")
    
    pyautogui.click(180,165, duration=0.5)
    pyautogui.typewrite("R6S")
    pyautogui.click(272,165, duration=0.5)
    pyautogui.click(180,165, duration=0.5)
    pyautogui.typewrite("Apex")
    pyautogui.click(180,165, duration=0.5)
    pyautogui.click(272,165, duration=0.5)
    pyautogui.typewrite("Valorant")
    pyautogui.click(272,165, duration=0.5)
    pyautogui.click(335,165, duration=0.5)
    pyautogui.pause(0.1)
    time.sleep(1)	
    pyautogui.moveTo(1035,612, duration=1)
    print('まぁこんな感じですね！要素を追加したら実行押せば処理してくれます')
    
#class gui():
 #   word = None
  #  screen_x,screen_y = pyautogui.size()
   # pyautogui.press("winleft")
#    pyautogui.typewrite(word)
 #   pyautogui.press("enter")
  #  time.sleep(1.5)
   # pyautogui.hotkey("winleft","up")
#class_word = gui()

#UI構築
root = tk.Tk()
root.title("オリジナル便利ツール Ver-2.0")
root.geometry("800x250")
root.configure(bg='black')
frame = tk.Frame(root)
frame.configure(bg='black')
frame.grid(column=10, row=10, sticky=tk.NSEW, padx=5, pady=10)

#logo = "REVEL.PNG"
#img = Image.open(logo)
#resized = img.resize((45,45))
#frame.photoing = ImageTk.PhotoImage(resized)
#LogoImage = tk.Label(frame,image=frame.photoing,bg='black')
#LogoImage.grid(row=0,column=0)

#LogoImage_sub = tk.Label(frame,width=6,height=3,bg='black')
#LogoImage_sub.grid(row=0,column=0)

#row = y, colum = x
TOOL_TITLE = tk.Label(frame, font=('Menlo',20),text="オリジナルソフトウェア Beta",bg='black',foreground='white')
TOOL_TITLE.grid(row=0,column = 0,columnspan=8)

TOOL_EXPLAIN = tk.Label(frame, font=('Menlo',10),
                        text="このソフトウェアはベータ版であり全てのPCで正常に動作する保証は出来かねます",
                        bg='black',foreground='white')
TOOL_EXPLAIN.grid(row=1,column = 0,columnspan=9)
TOOL_EXPLAIN2 = tk.Label(frame, font=('Menlo',10),
                        text="",
                        bg='black',foreground='white',pady=2)
TOOL_EXPLAIN2.grid(row=2,column = 0,columnspan=10)

TOOL_TITLE_EL = tk.Label(frame, font=('Menlo',15),text="便利ツール",bg='black',foreground='white')
TOOL_TITLE_EL.grid(row=3,column = 0,columnspan=8,pady=1)

Element_title = tk.Label(frame, text="ランダムで一つだけ選択します",bg='black',foreground='white')
Element_title.grid(row=4,column=0,columnspan=2)
Element_Name = tk.Label(frame, text="要素",bg='black',foreground='white')
Element_Name.grid(row=4, column=2)
entry_1 = ttk.Entry(frame,width=12)
entry_1.grid(row=4, column=2)
button_add_1 = tk.Button(frame, text="要素追加", command=game_append,bg='gray',foreground='yellow',width = 7)
button_add_1.grid(row=4, column=5)
button_run_1 = tk.Button(frame, text="処理実行", command=game_output,bg='green',foreground='white',width = 7)
button_run_1.grid(row=4, column=6)

ID_Name_title = tk.Label(frame, text="ランダムでAとBでチーム分けします",bg='black',foreground='white')
ID_Name_title.grid(row=5, column=0,columnspan=2)
ID_Name = tk.Label(frame, text="要素",bg='black',foreground='white')
ID_Name.grid(row=5, column=2)
entry_2 = ttk.Entry(frame,width=12)
entry_2.grid(row=5, column=2)
button_add_2 = tk.Button(frame, text="要素追加", command=member_append,bg='gray',foreground='yellow',width = 7)
button_add_2.grid(row=5, column=5)
button_run_2 = tk.Button(frame, text="処理実行", command=member_output,bg='green',foreground='white',width = 7)
button_run_2.grid(row=5, column=6)

button_reset = tk.Button(frame, text="リセット",bg='red',foreground='white', command=Reset,width = 7)
button_reset.grid(row=6, column=6)

TOOL_TITLE_EL2 = tk.Label(frame, font=('Menlo',15),text="ソフト起動",bg='black',foreground='white')
TOOL_TITLE_EL2.grid(row=3,column = 7,columnspan=10,pady=1)

statc = tk.Label(frame, text="|",bg='black',foreground='green')
statc.grid(row=4,column=7)
R6S = tk.Button(frame, text="Rainbow Six Siege",command=R6S,width = 18,bg='orange',foreground='black' )
R6S.grid(row=4, column=8)
APEX = tk.Button(frame, text="Apex Legends",command=APEX,width = 18,bg='orange',foreground='black')
APEX.grid(row=4, column=9)
VALORANT = tk.Button(frame, text="VALORANT",command=Valorant,width = 18,bg='orange',foreground='black')
VALORANT.grid(row=4, column=10)
statc2 = tk.Label(frame, text="|",bg='black',foreground='green')
statc2.grid(row=5,column=7)
DISCORD = tk.Button(frame, text="DISCORD",command=Discord,width = 18,bg='gray',foreground='white')
DISCORD.grid(row=5, column=8)
MEMO = tk.Button(frame, text="メモ帳",command=Memo,width = 18,bg='gray',foreground='white')
MEMO.grid(row=5,column=9)
OUTPLAYED = tk.Button(frame, text="クリップ確認",command=OutPlayed,width = 18,bg='gray',foreground='white')
OUTPLAYED.grid(row=5,column=10)

Demo = tk.Button(frame, text="実演",command=DemoRun ,width = 18,bg='black',foreground='white')
Demo.grid(row=10,column=8)

EXIT = tk.Button(frame, text="終了",command=exit_sys,width = 18,bg='black',foreground='white')
EXIT.grid(row=10,column=10)

root.mainloop()