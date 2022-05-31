
#Class
class customer:
    #Variables are:
    def __init__(self):
     self.FirstName=""
     self.SecondName=""
     self.Age=0
     self.Sex=""
     self.VehicleMake=""
     self.VehicleModel=""
     self.VehicleYear=""
     self.VehicleType=""
     self.IBAN=""
     self.Credit_card_number=""
     self.City=""
     self.Retired=""
     self.Salary=""
     self.Message=""
    #Methods are:
    #Setters 
    def setFirstName(self,first):
        self.FirstName=first
    def setSecondName(self,second):
        self.SecondName=second
    def setAge(self,age):
        self.Age=age
    def setSex(self,sex):
        self.Sex=sex
    def setVehicleMake(self,make):
        self.VehicleMMake=make
    def setVehicleModel(self,model):
        self.VehicleModel=model
    def setVehicleYear(self,yr):
        self.VehicleYear=yr
    def setVehicleType(self,typ):
        self.VehicleType=typ
    def setIBAN(self,ib):
        self.IBAN=ib
    def setCredit_card_number(self,cr):
        self.Credit_card_number=cr
    def setCity(self,cty):
        self.City=cty
    def setRetired(self,ret):
        self.Retired=ret
    def setSalary(self,slr):
        self.Salary=slr
    def setMessage(self,msg):
        self.Message=msg

    #Getters
    def getFirstName(self):
        return self.FirstName
    def getSecondName(self):
        return self.SecondName
    def getAge(self):
        return self.Age
    def getSex(self):
        return self.sex
    def getVehicleMake(self):
        return self.VehicleMake
    def getVehicleModel(self):
        return self.VehicleModel
    def getVehicleYear(self):
        return self.VehicleYear
    def getVehicleType(self):
        return self.VehicleType
    def getIBAN(self):
        return self.IBAN
    def getCredit_card_number(self):
        return self.Credit_card_number
    def getCity(self):
        return self.City
    def getRetired(self):
        return self.Retired
    def getSalary(self):
        return self.Salary
    def getMessage(self):
        return self.Message
#READING FILES
list=[] #To store the objects......... 
#Reading TXT FILE............
txt=open("user_data.txt")
content=txt.read()
txt.close()
Linewise=content.split("\n")
i=0
while i<len(Linewise):
    Name=Linewise[i].split(" ") #To get name
    obj=customer()
    obj.setFirstName(Name[0])
    obj.setSecondName(Name[1])
    obj.setMessage(Linewise[i])
    # print(obj.getFirstName())
    # print(obj.getSecondName())
    # print(obj.getMessage())
    list.append(obj)
    i=i+1
print("RECORDS SUCCESSFULLY FETHCHED FROM THE USER_DATA.TXT File.")
#............................

#Readin CSV FILE......
csv_f=open("user_data.csv")
content=csv_f.read()
csv_f.close()
csv=content.split() #Records are Taken in rows. Like 
#print("Total Records in CSV FILE:",len(csv))

i=8 #Because records starts from 8 index...
while i<len(csv):#39.....
   temp=csv[i].split(",") #Records are seperated.
   i=i+1
   length=len(temp)
   margin=8-length
   if(margin>=1): #If there are some missing entries.
     while(margin!=0):
          temp.append("null")
          margin=margin-1
   obj=customer()
   j=0
   obj.setFirstName(temp[j])
   obj.setSecondName(temp[j+1])
   obj.setAge(temp[j+2])
   obj.setSex(temp[j+3])
   obj.setVehicleMake(temp[j+4])
   obj.setVehicleModel(temp[j+5])
   obj.setVehicleYear(temp[j+6])
   obj.setVehicleType(temp[j+7])
   list.append(obj)
# for obj in list:
#     # calling method 
#     print(obj.getVehicleType())
print("RECORDS SUCCESSFULLY FETHCHED FROM THE USER_DATA.CSV File.")

#READING JSON FILE.........
js=open("user_data.json")
content=js.read()
js.close()
#print(content)
arr=content.split(",") #Key_Value pairs. Values are at 1,3,5,7,9,11,........
#print(arr[0])
# js=arr[20].split(",")
# print(js)
i=0
while i<len(arr)-6:
    obj=customer()
    js=arr[i].split(":")
    obj.setFirstName(js[1])
    js=arr[i+2].split(":")
    obj.setSecondName(js[1])
    js=arr[i+3].split(":")
    obj.setAge(js[1])
    js=arr[i+4].split(":")
    obj.setIBAN(js[1])
    js=arr[i+5].split(":")
    obj.setCredit_card_number(js[1])
    js=arr[i+6].split(":")
    obj.setCity(js[1])
    i=i+1
    list.append(obj)
print("RECORDS SUCCESSFULLY FETHCHED FROM THE USER_DATA.JSON File.")
#Reading XML FILE..........
xl=open("user_data.xml")
content=xl.read()
xl.close()
x=content.split(" ")
i=1
while i<len(x)-1:
 y=x[i].split(" ")
 z=y[0].split("=")
 obj=customer()
 #print(z[1])
 if(i==1):  
  obj.setFirstName(z[1])
 if(i==2):  
  obj.setSecondName(z[1])
 if(i==3):
     obj.setRetired(z[1])
 if(i==5):
     obj.setSalary(z[1])
 list.append(obj)
 i=i+1
 if i%7==1:  #........ /><user occurs at 7 index...
     i=i+1
print("RECORDS SUCCESSFULLY FETHCHED FROM THE USER_DATA.XML FILE. ")
#Too Test
# for obj in list:
#     print( obj.getMessage())
#     print( obj.getFirstName())

#DATABASE MYSQL...............
# import mysql.connector
# dbb=mysql.connector.connect(host="localhost",user="root",password="userpassword",database="customer")
# #print(dbb)
# if(db):
#     print("CONNECTION SECESSFULLY CREATED")
# else:
#     print("CONNECTION FAILED CREATED")
# mycurser=dbb.curser() #Temporary memory for manupulation.....

 # mycurser.execute("Create database customer")
# mycurser.execute("Create table info_cust(firstName varchar(20),secondName varchar(20),Age varchar(20),Sex varchar(20),vehicleMake varchar(20),vehicleModel varchar(20),vehicleYear varchar(20),vehicleType varchar(20))")

# sqlform="Insert into cust_info"(firstName,secondName,Age,Sex,vehicleMake,vehicleModel,vehicleYear,vehicleType) values(%s,%s,%s,%s,%s,%s,%s,%s)
# customers=[("Oliver","Brady","68","Male","Mitsubishi","WRX","2003","Sedan")]
# mycurser.exexute(sqlform,customers)
# dbb.commit()
#print("DATA SUCCCESSFULLY INSERTED IN MYSQL DATABASE USING MYSQL CONNECTOR.")

#PonyOrm database
#Install it by command. "pip install pony"
# Check versions by this command, "pip freeze > req.txt"
from pony.orm import *
from pony import orm
db=Database()
db.bind(provider='mysql', host='localhost', user='root', passwd='userpassword', db='customer')
class customer(db.Entity):
    firstName=orm.Required(str,20) #str automatically covert to varchar in mysql usning ponyOrm
    secondName=orm.Required(str,20)
    Age=orm.Required(str,20)
    sex=orm.Required(str,20)
    vehicleMake=orm.Required(str,20)
    vehicleModel=orm.Required(str,20)
    vehicleYear=orm.Required(str,20)
    vehicleType=orm.Required(str,20)
    IBAN=orm.Required(str,20)
    Credit_card_number=orm.Required(str,20)
    City=orm.Required(str,20)
    Retired=orm.Required(str,20)
    Salary=orm.Required(str,20)
    Message=orm.Required(str,20)
for obj in list:
  cust = customer(firstName=obj.getFirstName(),secondName=obj.getSecondName(),Age=obj.getAge(),sex=obj.getSex(),
         vehicleMake=obj.getVehicleMake(),vehicleModel=obj.getVehicleModel(), vehicleYear=obj.getVehicleYear(),
         vehicleType=obj.setVehicleType(),IBAN=obj.getIBAN(),Credit_card_number=obj.getCredit_card_number(),
         City=obj.getCity(),Retired=obj.getRetired(),Salary=obj.getSalary(),Message=obj.getMessage() )
  commit() #It sends data to database
print("DATA SUCCCESSFULLY INSERTED IN MYSQL DATABASE USING PONYORM .")