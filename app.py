# DATABASE GLOBAL VARIABLE

DB_COLOR = [
    {
        "name": "WHITE",
        "code": "#FFFFFF"
    },
    {
        "name": "BLACK",
        "code": "#000000"
    }
]


def startApp():
    print("------------------")
    print("1. Color List")
    print("2. Create Color")
    print("3. Delete Color")
    print("4. Exit Program")
    print("------------------")

    answer = int(input(">>"))

    if answer == 1:
        view_color()
    elif answer == 2:
        create_color()
    elif answer == 3:
        delete_color()
    elif answer == 4:
        print("프로그램 종료 할께요")
    else:
        print("[SYSTEM] 잘못 입력하셨습니다.")
        startApp()

# 실행키 python3 app.py


def view_color():
    print("🥕 COLOR LIST 🥕")
    for color in DB_COLOR:
        print(f"색상 이름 : {color['name']}")
        print(f"색상 코드 : {color['code']}")
        print("--------------------------")
    startApp()


def create_color():
    input_name = input("컬러 이름을 입력해주세요. >>")
    input_code = input("컬러 코드를 입력해주세요. >>")

    push_data = {
        "name": input_name,
        "code": input_code
    }

    DB_COLOR.append(push_data)

    startApp()


def delete_color():
    for color in enumerate(DB_COLOR):
        print(f"{color[0]} _ {color[1]['name']}")

    input_index = int(input("삭제할 색상의 번호를 입력해주세요 >>"))

    DB_COLOR.pop(input_index)
    print("입력하신 색상이 삭제되었습니다.")
    startApp()


startApp()
