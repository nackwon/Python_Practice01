menu = input("메뉴:").strip()

menu_list = {
    '오뎅': 300,
    '순대': 400,
    '만두': 500
}
menu_key_list = list(menu_list.keys())

if menu in menu_key_list:
    print("가격:", menu_list[menu])
else:
    print("해당하는 음식이 없습니다.")