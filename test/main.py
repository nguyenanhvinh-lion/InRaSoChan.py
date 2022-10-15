print("Chương trình in ra mảng số chẵn bằng Python")
print("Gõ exit để thoát chương trình")

def input_data():
    "Hàm nhập giữ liệu vào mảng"
    global listNum
    while True:
        try:
            print("Hãy nhập vào một số nguyên: ")
            tmp = input()
            if tmp == 'exit':
                break
            tmp = int(tmp)
            listNum.append(tmp)
        except ValueError:
            print("Lỗi, bạn phải nhập vào số nguyên: ")

def output_data(listNum):
    "Hàm in ra các số chẵn một mảng"
    for i in listNum:
        if i % 2 == 0:
            print(i, end='')

# Chương trình chính
listNum = []
input_data()
output_data(listNum)