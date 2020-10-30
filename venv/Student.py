class Student:
    def __init__(self, name,dict):
        self.name=name
        self.dict=dict

    def __str__(self):
        return str(self.name)+": "+str(self.dict)

    def lessons(self):
        return "Предмети: " + str(list(self.dict.keys()))

    def rate(self,lessonName):
        return str(lessonName) + " " + str(self.dict.get(lessonName))

    def gpa(self,lessonName):
        return str(lessonName) + " : " + str(sum(self.dict.get(lessonName))/len(self.dict.get(lessonName)))

    def zalik(self,lessonName):
        if sum(self.dict.get(lessonName))/len(self.dict.get(lessonName))>=4:
            return str(lessonName)+ ": Здав"
        else:
            return str(lessonName)+ ": Не здав"

    def newLesson(self,lessonName,values):
        self.dict.update({lessonName:values})

    def addRate(self,lessonName,num):
        self.dict[lessonName].append(num)

    def listAllGpa(self):
        return [i for i in self.dict.keys()]

firstStud=Student("Nazar ",{'OOP':[3,4,5],'Python':[5,5,3]})
print(firstStud.__str__())
print(firstStud.lessons())
print('Бали з предмету:', firstStud.rate('Python'))
print('Середнє арифметичне з', firstStud.gpa('OOP'))
print(firstStud.zalik('OOP'))
firstStud.newLesson('Fizra',[3,3,4])
print(firstStud.__str__())
firstStud.addRate('Fizra',2)
print(firstStud.__str__())
print(firstStud.listAllGpa())