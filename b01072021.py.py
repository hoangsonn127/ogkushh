class user:
    def __init__(self, account, accnumber, balance):
        self.account = account
        self.accnumber = accnumber
        self.balance = balance

    def show_information(self):
        print("ten tai khoan: ", user1.account)
        print("so tai khoan: ", user1.accnumber)
        print("so du: ", user1.balance)
    
    def deposit(self):
        receive_accnumber = input("tai khoan nhan tien: ")
        if receive_accnumber != user1.accnumber:
            print("so tai khoan khong hop le")
        else:
            print("so tai khoan hop le")
            deposit_amount = int(input("nhap so tien nap: "))
            if deposit_amount <50000:
                print("so tien khong hop le")
            else:
                if deposit_amount >= 50000 and deposit_amount <= 100000:
                    print("ban da nap: ", deposit_amount, "vnd")
                    print("phi dich vu cua ban la 1000 vnd")
                    user1.balance += deposit_amount
                    user1.balance -= 1000
                    print("so du hien tai: ", user1.balance)
                else:
                    print("ban da nap: ", deposit_amount, "vnd")
                    print("phi dich vu cua ban la", deposit_amount/100)
                    user1.balance += deposit_amount/100*99
                    print("so d hien tai cua ban la: ", user1.balance)
    
    def withdraw_cash(self):
        wc_accnumber = input("tai khoan rut tien: ")
        if wc_accnumber != user1.accnumber:
            print("so tai khoan khong hop le")
        else:
            print("so tai khoan hop le")
            wc_amount = int(input("so tien rut: "))
            if wc_amount<50000 or wc_amount>user1.balance:
                print("so tien khong hop le")
            else:
                if wc_amount >= 50000 and wc_amount <= 100000:
                    print("ban da chuyen: ", wc_amount, "vnd")
                    print("phi dich vu cua ban la 1000 vnd")
                    user1.balance -= wc_amount
                    user1.balance -= 1000
                    print("so du hien tai: ", user1.balance)
                else:
                    print("ban chuyen: ", wc_amount, "vnd")
                    print("phi dich vu cua ban la", wc_amount/100)
                    user1.balance -= wc_amount/100*101
                    print("so d hien tai cua ban la: ", user1.balance)

    def show_information(self):
        print("ten tai khoan: ", user1.account)
        print("so tai khoan: ", user1.accnumber)
        print("so du: ", user1.balance)


        # def service_charge(self):
        #     if deposit_amount >= 50000 and deposit_amount <= 100000:
        #         print("ban da nap: ", deposit_amount, "vnd")
        #         print("phi dich vu cua ban la 1000 vnd")
        #         user1.balance -= deposit_amount
        #         user1.balance -= 1000
        #     else:
        #         print("ban da nap: ", deposit_amount, "vnd")
        #         print("phi dich vu cua ban la", deposit_amount/100)
        #         user1.balance -= deposit_amount/100*101
        #         print("so d hien tai cua ban la: ", user1.balance)


user1 = user("tk1", "01072021", 700000)
user1.deposit()
user1.withdraw_cash()
user1.show_information()

