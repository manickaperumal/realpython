import csv
with open("/home/manikam/111.txt","r")as textfile:
    with open("/home/manikam/bigproject.csv","w",newline="")as csfile:
        writer=csv.writer(csfile)
        writer.writerow(["sno","goods","price"])

        no=int(input("how many lines of content do you want:"))
        for i in range(no):
            content=textfile.readline()
            

            content=content.split()
            writer.writerow(content)


output:
manikam@manikam:~$ /bin/python3 /home/manikam/pyy/3-2-22.py
how many lines of content do you want:3


sno	goods	price
1	sugar	600
2	curd	500
3	comb	5


