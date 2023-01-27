class child:
    def __init__(self,name,age,gender,height,weight):
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height
        self.weight=weight
    def BMI(self):
        self.BMI=self.weight/(self.height**2)*703
        print("BMI",self.BMI)
    def minimum_daily_calorie(self):
        if self.age<=2:
            print("Age b/w 0-2 years: 800 calories")
        elif 2<self.age<=4:
            print("Age b/w 2-4 years: 1400 calories")
        elif 4<self.age<=8:
            print("Age b/w 4-8 years: 1800 calories")
        else:
            print("your age is above 8")
    def input(self):
        self.milk=int(input("Milk:-",))
        self.Egg=int(input("Egg:-",))
        self.Rice=int(input("Rice:-",))
        self.Lentils=int(input("Lentils:-",))
        self.Vegetable=int(input("Vegetable:-",))
        self.meat=int(input("meat:-"))
    def daily_consumption(self):
        self.total_consumption=self.milk+self.Egg+self.Rice+self.Lentils+self.Vegetable+self.meat
        if self.age<=2:
            if self.total_consumption>=800:
                print("Not undernourished")
            else:
                print("undernourished")
        if 2<self.age<=4 :
            if self.total_consumption >= 800:
                print("Not undernourished")
            else:
                print("undernourished")
        if 4<self.age<=8:
            if self.total_consumption >= 800:
                print("Not undernourished")
            else:
                print("undernourished")
    def BMI_categories(self):
        if self.BMI<16:
            print("Severly Underweight")
        elif 16<=self.BMI<18.5:
            print("Underweight")
        elif 18.5<=self.BMI<25:
            print("Healthy")
        elif 25<=self.BMI<30:
            print("Overweight")
        else:
            print("Obese")
child1=child(name=input("Enter your Name:-",),age=int(input("Enter your age:-",)),gender=input("Enter your Gender:-",),height=int(input("Enter your height:-",)),weight=int(input("Enter your weight:-",)))
child1.BMI()
child1.minimum_daily_calorie()
child1.input()
child1.daily_consumption()
child1.BMI_categories()