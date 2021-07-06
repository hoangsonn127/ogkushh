import uuid
global max_discount
max_discount = 5
from datetime import date, datetime

class Product:
    def __init__(self, product_id, product_name, product_brand, product_type, product_price, product_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.product_brand = product_brand
        self.product_type = product_type
        self.product_price = product_price
        self.product_quantity = product_quantity

class Customer:
    def __init__(self, cus_id, cus_name, cus_phone):
        self.cus_id = cus_id
        self.cus_name = cus_name
        self.cus_phone = cus_phone

def insert_product():
    product_id = uuid.uuid4()
    check_product_id(product_id)
    product_name = input("tên giầy: ")
    product_brand = input("thương hiệu: ")
    product_type = input("loại giầy: ")
    product_price = input("giá giầy: ")
    check_product_price(product_id)
    product_quantity = input("số lượng giầy: ")
    f1 = open('products.txt', 'a', encoding='utf-8')
    f1.write(f"{product_id},{product_name},{product_brand},{product_type},{product_price},{product_quantity}\n")
    f1.close()
    menu()

def insert_customer():
    cus_id = uuid.uuid4()
    check_customer_id(cus_id)
    cus_name = input("tên khách hàng: ")
    cus_phone = input("sđt khách hàng: ")
    f1 = open('customers.txt', 'a', encoding='utf-8')
    f1.write(f"{cus_id},{cus_name},{cus_phone}\n")
    f1.close()
    print("1. Tiếp tục mua hàng.")
    print("2. Quay lại menu chính")
    choice3 = input()
    if str(choice3) == "1":
        cus_order()
    if str(choice3) == "2":
        menu()

def menu():
    print("1. Nhập thông tin sản phẩm.")
    print("2. Nhập thông tin khách hàng.")
    print("3. Xem danh sách sản phẩm.")
    print("4. Mua hàng.")
    print("5. Báo cáo")
    print("6. sap xep")
    choice = input()
    if str(choice) == "1":
        insert_product()
    elif str(choice) == "2":
        insert_customer()
    elif str(choice) =="3":
        show_product()
    elif str(choice) == "4":
        order_choice()
    elif str(choice) == "5":
        pro_order()
    elif str(choice) =="6":
        sort()

    else:
        print("lựa chọn không hợp lệ, mời nhập lại")
        return menu()
  
def check_product_id(product_id):
    f1 = open('products.txt', 'r+', encoding='utf-8')
    lines = f1.readlines()
    for line in lines:
        line.strip()
        c = line.split(',')
        if c[0] == product_id:
            print("id trùng")
            return check_product_id()
        else:
            print("id hợp lệ")
            f1.close()
            break

def check_product_price(product_price):
    if int(product_price) <= 0:
        print("giá sản phẩm phải lớn hơn 0")
        return check_product_price()
    else:
        print("bạn đã nhập giá sản phẩm")

def check_customer_id(cus_id):
    f1 = open('products.txt', 'r+', encoding='utf-8')
    lines = f1.readlines()
    for line in lines:
        line.strip()
        c = line.split(',')
        if c[0] == cus_id:
            print("id khách hàng trùng")
            return check_customer_id(cus_id)
        else:
            print("id hợp lệ")
            f1.close()
            break

def order_choice():
    print("bạn đã là thành viên của chúng tôi?")
    print("1. Tôi đã đăng ký thành viên.")
    print("2. Tôi chưa đăng ký thành viên.")
    choice = input()
    if str(choice) == "1":
        cus_order()
    if str(choice) == "2":
        print("đăng ký thành viên")
        insert_customer()
        cus_order()

def show_product():
    f1 = open('products.txt', 'r+', encoding='utf-8')
    lines = f1.readlines()
    for line in lines:
        line.strip()
        c = line.split(',')
        print(f"mã giầy: {c[0]}, tên giầy: {c[1]}, giá: {c[4]}, số lượng: {c[5]}")
    f1.close()
    print("0. Quay lại menu")
    choice1 = input("")
    if choice1 == "0":
        menu()

def cus_order():
    global max_discount
    order_pro_id = input("Mã sản phẩm: ")
    f1 = open('products.txt', 'r+', encoding='utf-8')
    lines = f1.readlines()
    check = False
    for line in lines:
        line.strip()
        c = line.split(',')
        if str(order_pro_id) == str(c[0]):
            print("id hợp lệ")
            check = True
            break  
    if not check:
        print("id k hợp lệ")
        return cus_order()

    order_pro_quantity = input("số lượng sp: ")
    max_discount  -= int(order_pro_quantity)
    if int(order_pro_quantity) > int(c[5]) or int(order_pro_quantity) <= 0:
        print("số lượng sản phẩm hiện k đủ")

    elif int(order_pro_quantity) <= 5 and max_discount > 0: 
        total = int(c[4])*int(order_pro_quantity)
        total_discount = int(c[4])*int(order_pro_quantity)*0.5
        order_cus_name = input("tên khách hàng: ")
        print(f"chưa giảm giá: {total} USD")
        print(f"Sau giảm giá: {total_discount} USD")
        print(f"còn {max_discount} sp được giảm giá")
        dt = datetime.now()
        print(dt)
        choice_after_buying()

    elif int(order_pro_quantity) <= 5 and max_discount <= 0:
        total = int(c[4])*int(order_pro_quantity)
        print(f"Bạn đã hết số lần được giảm giá")
        print(f"Tổng: {total} USD")
        dt = datetime.now()
        print(dt)
        choice_after_buying()

    elif int(order_pro_quantity) >= 5 and max_discount <= 0:
        total = int(c[4])*int(order_pro_quantity)
        print(f"Bạn đã hết số lần được giảm giá")
        print(f"Tổng: {total} USD")
        dt = datetime.now()
        print(dt)
        choice_after_buying()

    elif int(order_pro_quantity) >= 5 and max_discount > 0:
        total = int(c[4])*(order_pro_quantity)
        total_discount = int(c[4])*max_discount*0.5 + int(c[4])*(int(order_pro_quantity)-max_discount)    
        print(f"chưa giảm giá: {total} USD")
        print(f"sau giảm giá: {total_discount} USD")
        print(f"Bạn đã hết số lần được giảm giá")
        dt = datetime.now()
        print(dt)
        choice_after_buying()

def choice_after_buying():
    print("1. Mua tiếp")
    print("2. Kết thúc")
    choice = input()
    if int(choice) == 1:
        order_choice()
    if int(choice) == 2:
        print("cảm ơn đã mua hàng")

def pro_order():
    print("Báo cáo")
    try:
        customer_id = input("mã kh: ")
    except:
        print("mã khách hàng k đúng")

    f3 = open('cus_orders.txt', 'r')
    for line in f3:
        line.strip()
        cus_id, cus_name, pro_id, time = line.split(',')
        if customer_id == cus_id:
            print(cus_id, cus_name, pro_id, time)
    f3.close()

def sortByCustomerName(order):
    name = order.split(",")[1]
    return name

def sortByOrderDate(order):

    date = order.split(",")[3]
    return date
    
def sort():
    f3 = open('cus_orders.txt', 'r')
    orders = f3.readlines()
    f3.close()

    if len(orders) == 0:
        print("đơn hàng trống")
    
    else:
        choice = input("sắp xếp theo tên(a) hoặc ngày (b) ? ")
        if choice == "a":
            orders.sort(key = sortByCustomerName)
        elif choice == "b":
            orders.sort(key = sortByOrderDate)

        for o in orders:
            cus_id, cus_name, pro_id, time = o.split(',')
            print(cus_id, cus_name, pro_id, time)


menu()


