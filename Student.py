class Student:

    def __init__(self,std_id = "", name = "", m1 = "", m2 = "",room_num = ""):
        self.__std_id = std_id;
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.room_num = room_num;
 
    def insert(self,student_array,std_id, Name, marks1, marks2,room_num):
        ob = Student(std_id,Name, marks1, marks2,room_num)
        student_array.append(ob)

    def display(self, ob,room_name):
        print("Name : ", ob.name)
        print("Id : ", ob.__std_id)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("Room Name :",room_name)
        print("\n")
