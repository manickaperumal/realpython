import csv
with open("/home/manikam/first.csv","w")as file:
    v=csv.writer(file)
   
    v.writerow(['name',"mblno","email"])
    members=int(input("given a no for your purpose:"))
    for i in range(members):
        name=input("enter your name:")
        mblno=int(input("enter your mobile no:"))
        email_id=input("enter your email id:")
        v.writerow([name,mblno,email_id])
        print(type(v))


import csv
with open ("/home/manikam/111.txt","r")as file1:
  with open("/home/manikam/supermarket.csv","w",newline="\n")as file2:

      store=file1.read()
      store=store.split()
      pen=csv.writer(file2)
      pen.writerow(["no","goods","price"])
      pen.writerow(store)










