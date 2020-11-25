
class CustomerManager:
    balance=0
    userpassword=""
    username=""
    userid=""
    def __init__(self,user):

        self.balance =float(user[3])
        self.userpassword = user[2]
        self.username= user[1]
        self.userid = user[0]

    
    def process(self,choice):
        
        if choice == "1":
        
            quantity = float(input("çekmek istediğiniz miktarı girin:"))
            if quantity < self.balance:

                self.balance -= quantity 
                self.balance = str(self.balance)
                print("kalan bakiyeniz ",self.balance," $ dır.")
                currentaccount = [self.userid,self.username,self.userpassword,self.balance]
                return currentaccount

            elif quantity > self.balance:

                print("yeterli bakiyeniz yok !!")
                return None

        elif choice == "2":

            quantity = float(input("yüklemek istediğiniz miktarı girin:"))
            self.balance += quantity
            self.balance = str(self.balance)
            print("hesap bakiyeniz ",self.balance, " $ dır.")
            currentaccount = [self.userid,self.username,self.userpassword,self.balance]
            return currentaccount

        elif choice == "3":

            print("tekrar bekleriz")
            return None

        else:

            print("bir işlem seçtiğinizden emin olun !!")
            return None
