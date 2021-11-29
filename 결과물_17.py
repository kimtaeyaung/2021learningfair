print("해당 시스템을 이용하실 시, 입력하셔야 될 부분을 잘 확인해주시기를 부탁드립니다.\n특히 채소와 소스 부분을 잘 확인해주시기를 부탁드리겠습니다.")
while True:
    print()
    print("==============메뉴판==============")
    print("스테이크앤치즈\n에그마요\n이탈리안 비엠티\n비엘티")
    print("===============================")
    print()
    order=input("주문하실 메뉴를 입력해주세요.: ")
    if order == '스테이크앤치즈' or order == '에그마요' or order == '이탈리안 비엠티' or order == '비엘티' or order == '이탈리안비엠티':
        print("주문하신 메뉴는", order, "입니다.")

        break

    else :
        print("메뉴를 다시 확인해주십시오.")

while True :
    print()
    length=int(input("빵 길이 15/30 cm 중 선택해주세요.(숫자): "))
    if length == 15 or length == 30:
        print("주문하신 빵 길이는", length, "cm 입니다.")

        break

    else :
        print("빵 길이를 다시 확인해주십시오.")

while True:
    print()
    print("==============빵 종류==============")
    print("화이트\n위트\n플랫 브레드\n파마산 오레가노\n허니 오트")
    print("===================================")
    print()
    bread=input("원하시는 빵 종류를 입력해주세요: ")
    if bread == '화이트' or bread == '위트' or bread == '플랫 브레드' or bread == '파마산 오레가노' or bread == '허니 오트' or bread == '플랫브레드' or bread == '파마산오레가노' or bread == '허니오트':
        print("선택하신 빵 종류는", bread, "입니다.")

        break

    else :
       print("빵 종류를 다시 확인해주십시오.")

while True :
    print()
    toast=input("빵을 구워드릴까요?(예/아니요): ")
    if '예' in toast:
        print("빵은 구워드리도록 하겠습니다.")

        break
                
    elif '아니요' in toast:
        print("알겠습니다.")

        break

    else :
        print("입력하셔야 되는 선택지를 다시 확인해주세요.")

while True :
    print()
    print("==============치즈==============")
    print("아메리칸 치즈\n슈레드 치즈\n모짜렐라 치즈")
    print("================================")
    print()
    cheese=input("원하시는 치즈 종류를 입력해주세요.: ")
    if cheese == '아메리칸 치즈' or cheese ==  '슈레드 치즈' or cheese ==  '모짜렐라 치즈' or cheese ==  '아메리칸치즈' or cheese ==  '슈레드치즈' or cheese ==  '모짜렐라치즈':
        print("선택하신 치즈는", cheese, "입니다.")

        break

    else :
        print("치즈 종류를 다시 확인해주십시오.")
        
while True :
    print()
    print("==============채소==============")
    print("양상추\n토마토\n오이\n피망\n양파\n피클\n올리브")
    print("================================")
    print()
    veg=input("원하시는 채소를 모두 입력해주세요.: ")
    if '양상추' in veg or '토마토' in veg or '오이' in veg or '피망' in veg or '양파' in veg or '피클' in veg or '올리브' in veg:
        print("선택하신 채소는", veg, "입니다.")

        break

    else :
        print("채소 종류를 다시 확인해주십시오.")

while True :
    print()
    print("==============소스==============")
    print("고소한 맛\n달콤한 맛\n매콤한 맛\n올리브 오일\n소금\n후추")
    print("================================")
    print()
    sauce=input("원하시는 소스를 모두 입력해주세요.: ")
    if '고소한 맛' in sauce or '달콤한 맛' in sauce or '매콤한 맛' in sauce or '올리브 오일' in sauce or '소금' in sauce or '후추' in sauce or '고소한맛' in sauce or '달콤한맛' in sauce or '매콤한맛' in sauce or '올리브오일' in sauce:
        print("선택하신 소스는", sauce, "입니다.")
        print()
        print("주문해주셔서 감사합니다.\n결제는 옆 쪽에서 도와드리도록 하겠습니다.")

        break

    else :
        print("소스를 다시 확인해주십시오.")
