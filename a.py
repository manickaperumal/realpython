import csv
with open("student.csv","w",newline=" ")as file:
    reynolds=csv.writer(file)
    reynolds.writerow(["sid","sname","stdaddress"])
    count=int(input("enter no of studnets"))
    for i in range(count):
        sid=int(input("enter student id"))
        sname=input("enter student name")
        saddress=input("enter student address")
        reynolds.writerow(sid,sname,saddress)
