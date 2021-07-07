# - Phát triển phần mêm quản lý tài khoản ngân hàng (BK bank)
# - 2 loại tài khoản: Saving account(tk tiết kiệm), Checking account(tk vãng lai)
# - 2 tk chứa thông tin: số tài khoản, số dư, 
# - hđ đc thực hiện: gửi tiền, rút tiền, kiểm tra số dư, số tiền rút k quá số dư
# - tk tiết kiệm thêm infor: lãi suất ngân hàng
# - tk vãng lai: k có lãi suất, nhưng được rút quá số dư nếu được liên kết với
#   tài khoản tiết kiệm của cùng 1 người. 
#       + k liên kết -> k đc rút quá số dư
#       + có liên kết -> rút hết tk vl, sau đó rút hết tk tk, nếu rút k
#         thành công -> số dư 2 tk k đổi
# - Mỗi khách hàng tối đa 10 tk (tổng cả 2 loại)
# - Khách hàng được xem: tên kh, các tk sở hữu, và tống số tk
 
# yêu cầu: 
#   - Khai báo thuộc tnh theo biểu đồ lớp đã tk.
#   - Chức năng thêm tài khoản cho khách hàng
#   - chức năng lấy tài khoản - trả về 1 tk với tham số là số tk của tk đó
#   - chức năng in thông tin tài khoản:
#       + in tổng số tk sở hữu
#       + số dư, lãi suất(nếu là tk tiết kiệm) từng tk
#       + tổng số tiền của tất cả tk



class Customer:
    def __init__(self, name):
        self.name = name
        self.account =[]
   
    def add_account(self):
        print("tạo tk: ")
        choice = int(input("tk checking(1) hoặc tk saving(2)?\nchọn: "))
        if choice == 1:
            print("tk checking")
            account = input("tk: ")
            balance = input("số dư: ")
            account = Checking_account(account, balance)
            print("liên kết với tk saving?")
            print("1. có")
            print("2. không")
            connect = int(input("chọn: "))
            if connect == 1:
                cn_account = input("liên kết tới tk: ")
                for c in self.account:
                    if isinstance(c, Saving_account) and cn_account == c.account:
                        account.connect_sv_account = c.account
                        break
                else:
                    print("tk k tồn tại")
                    
            self.account.append(account)
        elif choice == 2:
            print("tk saving")
            account = input("tk: ")
            balance = input("số dư: ")
            interest = int(input("lãi: "))
            account = Saving_account(account, balance, interest)
            self.account.append(account)

        elif int(choice) != 1 and int(choice) != 2:
            print("lựa chọn k hợp lệ")
            account = None
            self.account.append(account)
        
        return account
        
    def __str__(self):
        infor = "tên kh: {}; account:\n".format(self.name)

        if (len(self.account) == 0):
            infor += "None"

        else:
            for a in self.account:
                infor += a.__str__() + "\n"
        return infor         

    def get_account(self, account):
        for c in self.account:
            if c.account == account:
                return c
        return None


class Bank_account():
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def __str__(self):
        return "so tk: {}; số dư: {}".format(self.account, self.balance)

    def deposit(self, amount):
        amount = input("số tiền: ")
        if amount > 0:
            self.balance += amount
            print("chuyển thành công")
        else:
            print("số tiềb không hợp lệ")

    def withdraw(self, amount):
        pass

class Saving_account(Bank_account):
    def __init__(self, sv_account, sv_balance, sv_interest):
        super().__init__(sv_account, sv_balance)
        self.sv_interest = sv_interest

    def __str__(self):
        return "tk ck:" + super().__str__() + "lãi : {};".format(self.sv_interest)

    def withdraw(self, amount):
        if amount <= self.sv_balance:
            self.sv_balance -= amount
            print("rút tiền thành công")
        else:
            print("tài khoản không đủ")

class Checking_account(Bank_account):
    def __init__(self, ck_account, ck_balance):
        super().__init__(ck_account, ck_balance)
        self.connect_sv_account = None
    def __str__(self):
        return "tk ck:" + super().__str__() + '; ' "liên kết tk saving: {};".format(self.connect_sv_account)

    def withdraw(self,amount):
        if amount <= self.ck_balance:
            self.ck_balance -=amount
        elif self.connect_sv_account:
            saving_account = Customer.get_account(self.connect_sv_account)
            if self.ck_balance + saving_account.sv_balance >=0:
                self.ck_balance = 0
                saving_account.sv_balance -= (amount - self.ck_balance)
            else:
                print("tài khoản không đủ")
        else: print("tài khoản k đủ")

customer = Customer("Tran Thi B")
acc1 = customer.add_account()
acc2 = customer.add_account()
print(customer.__str__())






