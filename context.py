class Context():
    def __init__(self,path:str):
        self._path = path
    
    def readContext(self):
        #this function retrun lisf of datas

        text = open(self._path,"r",encoding="utf-8")
        obj=text.readlines()
        i = 0
        user=list()
        for i in obj :
            data = i.split(",")
            user.append(data)

        return user


    def uptadeContext(self,currentuser:list):
        #burada dosya güncelleme işlemi yapılacak kişinin hangi satırda olduğunun bilinmessi için id eklenecek
        #ve id okunarak o satır silinip tekrar güncellenecek
        if currentuser  == None:
            return
    
        else:

            textoku = open(self._path,"r",encoding="utf-8")
            data = textoku.readlines()
            index = int(currentuser[0])
            textoku.close()

            del data[index]

            data.insert(index,currentuser[0]+","+currentuser[1]+","+currentuser[2]+","+currentuser[3]+"\n")
            text = open(self._path,"w",encoding="utf-8")
            text.writelines(data)

            text.close()
            print("işlem başarılı")

