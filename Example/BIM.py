height = float(input('请输入身高'))
strong = float(input('请输入体重'))
print('小明身高为%s,体重为%s' % (height, strong))
BIM = strong / height ** 2
print('小明身体状况指数为%s' % BIM)
if BIM < 18.5:
    print('过轻')
elif BIM >= 18.5 and BIM <= 25:
    print('正常')
elif BIM >= 25 and BIM <= 28:
    print('过重')
elif BIM >= 28 and BIM <= 32:
    print('肥胖')
elif BIM >= 32:
    print('严重肥胖')
else:
    print('过度严重肥胖')
