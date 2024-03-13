class Room:
    
    def __init__(self,room_id = "", name = "") :
        self.__room_id = room_id
        self.name = name

    def insert(self,room_array,id, Name) :
        ob = Room(id,Name)
        room_array.append(ob)

    def display(self, ob,student_list) :
        print("Room Id : ", ob.__room_id)
        print("Room Name : ", ob.name)
        student_total = 0;
        for i in range(student_list.__len__()):
            if(student_list[i].room_num == ob.__room_id):
                student_total+=1
        print("Amount Of Student : ", student_total)
        print("\n")

    def search_room(self,room_list,room_id) :
        for i in range(room_list.__len__()):
            if(room_list[i].__room_id == room_id):
                return room_list[i]