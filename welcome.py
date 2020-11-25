def welcome(username:str,userbalance:str):
    print("hoşgeldin ",username)
    print("\nbakiyeniz: ",userbalance," $ dır\n")
    choice = input("1:para çekmek için\n2:para yüklemek için\n3:çıkmak için\n")

    return choice
