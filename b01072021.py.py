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
            deposit_amount = input("nhap so tien nap: ")
            user1.balance += deposit_amount
            print("nap thanh cong,so du hien tai la", user1.balance)


user1 = user("tk1", "01072021", "700000")
user1.deposit()

