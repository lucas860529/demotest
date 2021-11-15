import os

print("""
這是一個非常陽春的腳本，只能快速輸入input，程式有沒有正確要自己看。
- 請先在腳本中設定檔名FILENAME record檔名RECORD_FILE_NAME (有些白ㄔ會打錯records.txt)
- 請確認你的上一位同學的records.txt或類似的東西刪掉了
- testcase.txt會輸入 但是不會顯示在terminal 可能會有點怪
- 如果噴出EOL error 那可以忽略 但其他error是程式的問題喔
- 有些同學自己設計了多餘的流程 你只能自己出去乖乖的一個一個case試了

case3-7需要有records.txt 如果你要單獨run的話可以再次執行case2
""")

FILENAME = '109062318_簡弘哲_hw2.py'
RECORD_FILE_NAME = 'records.txt'

def case1():

    print('\n=== CASE1 inital input error/在第一次執行沒有records時是否進input initial value ===\n')
    os.system(f'rm -f ./{RECORD_FILE_NAME}')
    os.system(f"python3 ./students/{FILENAME} < ./demo2_testcase/testcase1.txt")

def case2():
    print('\n=== CASE2 重複add/view/exit ========\n')
    os.system(f'rm -f ./{RECORD_FILE_NAME}')
    os.system(f"python3 ./students/{FILENAME} < ./demo2_testcase/testcase2.txt")

def case3():
    print('\n=== CASE3 回到程式 是否有保存紀錄====\n')
    os.system(f"python3 ./students/{FILENAME} < ./demo2_testcase/testcase3.txt")

def case4():
    print('\n=== CASE4 Invalid Command  === \n')
    os.system(f"python3 ./students/{FILENAME} < ./demo2_testcase/testcase4.txt")

def case5():
    print('\n=== CASE5 add error 有兩個=== \n')
    os.system(f"python3 ./students/{FILENAME} < ./demo2_testcase/testcase5.txt")

def case6():
    print('\n=== CASE6  可否刪除紀錄/balance是否正確 只剩catfood balance:900====\n')
    os.system(f"python3 ./students/{FILENAME} < ./demo2_testcase/testcase6.txt")

def case7():
    print('\n=== CASE7 wrong delete 有兩個===\n')
    os.system(f"python3 ./students/{FILENAME} < ./demo2_testcase/testcase7.txt")

def case8():
    print('\n=== CASE8 空records.txt的表現 ===\n')
    with open(RECORD_FILE_NAME, 'w+') as f:
        f.write("""""")
    os.system(f"python3 ./students/{FILENAME} < ./demo2_testcase/testcase8.txt")

def case9():
    print('\n=== CASE9 inital value不是integer ===\n')
    with open(RECORD_FILE_NAME, 'w+') as f:
        f.write("""aaa\n""")
    os.system(f"python3 ./students/{FILENAME} < ./demo2_testcase/testcase9.txt")

def case10():
    print('\n=== CASE10 inital value是integer 但是record無法辨識 ===\n')
    with open(RECORD_FILE_NAME, 'w+') as f:
        f.write("""1000\naaa\n""")
    os.system(f"python3 ./students/{FILENAME} < ./demo2_testcase/testcase10.txt")

c = input('要測第幾個case?(1-10/all)')
if c == 'all':
    for i in range(1, 11):
        locals()[f"case{i}"]()
        cont = input('\ncontinue?(any key/N)')
        if cont == 'N': exit()
else:
    locals()[f"case{c}"]()

