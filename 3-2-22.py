def isphoneno(text):
    if len(text)!=10:
        return False

    for i in range(0,9):
        if (not(text[i].isdecimal())):
            return False
        if text[0]=='0':
            return False

        return True 

print('is 9976543210 a phone no?')
print(isphoneno("9876543210"))
print(isphoneno("0123456789"))

output:

    manikam@manikam:~$ /bin/python3 /home/manikam/pyy/3-2-22.py
    is 9159056955 a phone no?
    True
    False

                                                regular expression

import re
mobilenumberpattern=re.compile("\d{10}")
present=mobilenumberpattern.search("my nymber is 9876543210")
print(present)

output:

manikam@manikam:~$ /bin/python3 /home/manikam/pyy/3-2-22.py
<re.Match object; span=(13, 23), match='9876543210'>



import re
mobilenumberpattern=re.compile("[6-9][0-9]{9}")
present=mobilenumberpattern.search("my nymber is 9876543210")
present1=mobilenumberpattern.search("my number is 0123456789")
print(present)
print(present1)

output:
manikam@manikam:~$ /bin/python3 /home/manikam/pyy/3-2-22.py
<re.Match object; span=(13, 23), match='9876543210'>
None


import re
mobilenumberpattern=re.compile("(0|91)[6-9][0-9]{9}")

present1=mobilenumberpattern.search("my number is 0123456789")
present2=mobilenumberpattern.search("my number is 919875643210")
print(present1)
print(present2)

output:

manikam@manikam:~$ /bin/python3 /home/manikam/pyy/3-2-22.py
None
<re.Match object; span=(13, 25), match='919875643210'>






