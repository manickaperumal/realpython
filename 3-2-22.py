




import re
aadharpattern=re.compile("[0-9]{4}[ ]{1}[0-9]{4}")
present=aadharpattern.search("my aadhar no is 1234 5678")

present1=aadharpattern.search(" my no is 2345 9876")
print(present1)
print(present)
c="3456 9876"
print(aadharpattern.search(c))

output:

manikam@manikam:~$ /bin/python3 /home/manikam/pyy/3-2-22.py
<re.Match object; span=(10, 19), match='2345 9876'>
<re.Match object; span=(16, 25), match='1234 5678'>
<re.Match object; span=(0, 9), match='3456 9876'>

