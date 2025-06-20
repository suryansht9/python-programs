#when we have to define a class then make sure we have to define her properties and behaviour
#steps to create  a  class
'''class student():#define the class
    name="suryansh :"#give data
    age=21
    department="bca+mca"
fetch=student()#store your class in object
print(fetch.name,fetch.department)#access your data inside of class from fetch'''
#WAP TO PRINT TE TOTAL SALLARY OF EMPLOYEE WITH ADDING HER T.A AND D.A OF MONTH
#class employee():
'''Name=input("please enter the name of employee =")
    Employee_id=int(input("Enter the employee id ="))
    Designation=input("please enter the designation of employee =")
    Sallary=int(input("Enter the sallary of Employee ="))
    TA=(Sallary/100)*2
    DA=(Sallary/100)*1
    Total_Sallary=Sallary+TA+DA
A=employee()
print("NAME OF EMPLOYEE=",A.Name)
print("EMPLOYEE ID IS=",A.Employee_id)
print("DESIGNATION OF EMPLOYEE IS=",A.Designation)
print("SALLARY OF EMPLOYEE IS=",A.Sallary)
print("MONTHLY T.A OF  EMPLOYEE IS=",A.TA)
print("MONTHLY D.A OF EMPLOYEE IS=",A.DA)
print("TOTAL SALLARY OF EMPLOYEE IS=",A.Total_Sallary)'''
#WAP TO PRINT THE  ABOVE PROGRAMME IN REPEATED MODE AND PASSSING AN ARGUMENT
class credit():
    def employee(self):
        self.Name=input("please enter the name of employee =")
        self.Employee_id=int(input("Enter the employee id ="))
        self.Designation=input("please enter the designation of employee =")
        self.Sallary=int(input("Enter the sallary of Employee ="))
        self.TA=(self.Sallary/100)*4.5
        self.DA=(self.Sallary/100)*2.5
        self.Total_Sallary=self.Sallary+self.TA+self.DA
    def encrement(self):
        print("NAME OF EMPLOYEE=",self.Name)
        print("EMPLOYEE ID IS=",self.Employee_id)
        print("DESIGNATION OF EMPLOYEE IS=",self.Designation)
        print("SALLARY OF EMPLOYEE IS=",self.Total_Sallary)
        print("MONTHLY T.A OF  EMPLOYEE IS=",self.TA)
        print("MONTHLY D.A OF EMPLOYEE IS=",self.DA)
        print("TOTAL SALLARY OF EMPLOYEE IS=",self.Total_Sallary)
total_sallary=credit()
total_sallary.employee()
total_sallary.encrement()
total_sallary2=credit()
total_sallary.employee()
total_sallary.encrement()


        
        
    
