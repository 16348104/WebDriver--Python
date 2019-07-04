import re

# print(re.search('www', 'www.runoob.com'))
line = "btn   disabled  cur-not-allowed";
searchObj = re.search(r'disabled', line, re.I)

if searchObj:
    print("searchObj: ", searchObj.span())
else:
    print(searchObj)
