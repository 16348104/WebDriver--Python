import re

# print(re.search('www', 'www.runoob.com'))
line = "btn   disabled  cur-not-allowed";
searchObj = re.search(r'disabled', line, re.I)

if searchObj:
    print("searchObj: ", searchObj.span())
else:
    print(searchObj)

# item = 'span_first_38380442'
item = '139639661_139639666'

# num = re.sub(r'\D', '', item)
# num = re.sub(r'\D', item)
num = item.split("_")[0]
print("id是 : ", num)
# print("id是 : ", item[-8:])
