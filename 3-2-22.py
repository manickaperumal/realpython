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

output:

manikam@manikam:~$ /bin/python3 /home/manikam/pyy/3-2-22.py
given a no for your purpose:2
enter your name:manic
enter your mobile no:91590
enter your email id:manic@.com
<class '_csv.writer'>
enter your name:perumal
enter your mobile no:56955
enter your email id:perumal@.com
<class '_csv.writer'>
