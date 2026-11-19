class employ:
    company_name="Nike"
    def __init__(self,name,age):

        self.name=name
        self.age=age


    def displays(self):

        print(f"hello! my name is {self.name},I am {self.age} years old ")

    def job(self,jobtittle):
        print(f"i would like to work here as a {jobtittle}")


    def __del__(self):
        print("the destructor func. has been called")


object1=employ("Ayaan",16)

object1.displays()
object1.job("manager")


object2=employ("alex",24)

object2.displays()
object2.job("hr")





            