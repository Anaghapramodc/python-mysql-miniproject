"""
represent child class to parant class using super function

"""
class company:
    def company_name(self):
        return"google"

class employee(company):
    def info(self):
        #calling the supperclas methord using super() function
        c_name=super().company_name()
        print("chitra work at",c_name)

emp=employee()
emp.info()
#next section april 14
#https://www.lovelycoding.org/art-gallery-management-system/

