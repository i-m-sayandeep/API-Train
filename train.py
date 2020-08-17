from tkinter import*
import requests


class Irctc:

     def __init__(self):
        self.root=Tk()

        self.root.title("self.trainNo Route")
        self.root.minsize(1280,720)
        self.root.maxsize(1280,720)

        self.root.configure(background="#00a65a")

        self.label1=Label(self.root, text="TRAIN ROUTE",bg="#00a65a",fg="#ffffff")
        self.label1.configure(font=("Constantia",22,"bold"))
        self.label1.pack(pady=(30,10))

        self.trainNo=Entry(self.root)
        self.trainNo.pack(ipadx=90,ipady=10)

        self.click=Button(self.root, text="Fetch Stations",bg="#ffffff",fg="#000000",width=25,height=2,command=lambda:self.__fetch())
        self.click.configure(font=("Constantia",10))
        self.click.pack(pady=(10,20))

        self.result=Label(self.root, text="",bg="#00a65a",fg="#ffffff")
        self.result.configure(font=("Constantia",22))
        self.result.pack(pady=(5,10))

        self.root.mainloop()



     def __fetch(self):
          train=self.trainNo.get()
          url="https://api.railwayapi.com/v2/route/train/{}/apikey/wfdfojy183/".format(train)
          response=requests.get(url)
          data=response.json()
          
          stations=""
          for i in data['route']:
               #print(i['station']['name'])
               stations=stations+i['station']['name']+"\t"+i['scharr']+"\t"+i['schdep']+"\t"+str(i['distance'])+"K.M."+"\n"

          self.result.configure(text=stations)


ob=Irctc()
