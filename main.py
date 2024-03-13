from Room import Room
from Student import Student

student_list = []
room_list = []

student_obj = Student()
room_obj = Room()

room_id = 1;
student_id = 1;

room_obj.insert(room_list,room_id,"Test Room")
room_id += 1;

student_obj.insert(student_list,student_id,"Student Test",100,90,1)
student_id += 1;

print("\nOperations used, ")
print("\n1.List Room\n2.Add Room\n3.List Student \n4.Add Student\n5.Exit")

ch = int(input("Enter choice:"))

while (ch != 5) :
	if(ch == 1) :
		if(room_list.__len__() == 0) :
			print("Currently No Room")
		else :
			print("\n")
			print("\nList of Rooms\n")
			for i in range(room_list.__len__()):
				room_obj.display(room_list[i],student_list)

	elif(ch == 2):
		name = input("Enter Room Name : ")
		room_obj.insert(room_list,room_id,name)
		room_id+=1

	elif(ch == 3) :
		if(student_list.__len__() == 0) :
			print("Currently No Student")
		else :
			print("\n")
			print("\nList of Student\n")
			for i in range(student_list.__len__()):
				student_room = room_obj.search_room(room_list,student_list[i].room_num)
				student_obj.display(student_list[i],student_room.name)

	elif(ch == 4) :
		if(room_list.__len__() == 0) :
			print("Please Add Room First")
		else :
			name = input("Enter Student Name :")
			mark1 = input("Enter Student First Mark :")
			mark2 = input("Enter Student Second Mark :")
			print("Assign Room From Selection : \n")
			for i in range(room_list.__len__()):
				room_obj.display(room_list[i],student_list)
			room_num = input("Select Room : ")
			student_obj.insert(student_list,student_id,name,mark1,mark2,int(room_num))
			student_id+=1

	ch = int(input("Enter choice:"))
 
 