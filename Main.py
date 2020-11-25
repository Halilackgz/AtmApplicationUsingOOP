from login import login
from welcome import welcome
from customerManager import CustomerManager
from context import Context

def Main():


    username = str(input("kullanıcı adını giriniz:"))
    password = str(input("şifrenizi giriniz:"))
    user = login(username,password)
    print(user)

    if user != None:
        choice = welcome(username,user[3])

        manager = CustomerManager(user)

        currentaccount = manager.process(choice)
        context = Context("C:\\Users\\Halil\\OneDrive\\Masaüstü\\Python With HAT\\kullanıcılar.txt")
        context.uptadeContext(currentaccount)

       
    else:
        print("hatalı kullanıcı adı yada parola  !!")

Main()
