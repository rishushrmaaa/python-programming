subject1 =int(input("enter name:"))
subject2 =int(input("enter name:"))
subject3 =int(input("enter name:"))
subject4 =int(input("enter name:"))
subject5 =int(input("enter name:"))

total=(subject1+subject2+subject3+subject4+subject5)
average = total/5
print("Total marks:", total)      
print("Average marks:", average) 

if(average>=90):
    print("grade A")
elif(average>=80):
    print("grade B")
elif(average>=70):
    print("grade c")
elif(average>=60):
    print("grade d")
elif(average>=50):
    print("grade e")
else:
    (average>=40)
    print("grade fail")
  