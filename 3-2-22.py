


import csv
with open("/home/manikam/bigproject.csv","r")as csfile:
    r=csv.reader(csfile)
    output=list(r)
    for line in output:
     print(line)

output:

manikam@manikam:~$ /bin/python3 /home/manikam/pyy/3-2-22.py
['sno', 'goods', 'price']
['1', 'sugar', '600']
['2', 'curd', '500']
['3', 'comb', '5']
manikam@manikam:~$ 

