
import xlwt
import xlrd

# 有关Excel 2007版之前的excel文件后缀为.xls，最大支持65535行数据，xlrd和xlwt主要应用于07版之前的Excel文件。xlrd可以用来读取.xls和.xlsx文件， xlwt写文件只支持.xls，所以对数据的大小有限制
# 2007版之后的excel文件后缀为.xlsx, 最大支持1048576行，使用openpyxl来弥补xlwt的缺陷来处理大文件。
# 有个比较简单的解决办法就是在数字和日期的单元格内容前加上一个英文的逗号即可。如果数据比较多，也可以批量加英文逗号的前缀
# 设置表格样式
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


# # 写Excel
# def write_excel():
#     f = xlwt.Workbook()
#     sheet1 = f.add_sheet('学生', cell_overwrite_ok=True)
#     row0 = ["姓名", "年龄", "出生日期", "爱好"]
#     colum0 = ["张三", "李四", "恋习Python", "小明", "小红", "无名"]
#     # 写第一行
#     for i in range(0, len(row0)):
#         sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
#     # 写第一列
#     for i in range(0, len(colum0)):
#         sheet1.write(i + 1, 0, colum0[i], set_style('Times New Roman', 220, True))
#         sheet1.write(1, 3, '2006/12/12')
#         sheet1.write_merge(6, 6, 1, 3, '未知')  # 合并行单元格
#         sheet1.write_merge(1, 2, 3, 3, '打游戏')  # 合并列单元格
#         sheet1.write_merge(4, 5, 3, 3, '打篮球')
#         f.save('test.xls')
# 写Excel
# def write_excel():
#     f = xlwt.Workbook()
#     sheet1 = f.add_sheet('各院系链接', cell_overwrite_ok=True)
#     row0 = ["院系名称", "链接"]
#     colum0 = ["张三", "李四"]
#     colum1 = ["Python", "java", "C#", "VB"]
#     # 写第一行
#     for i in range(0, len(row0)):
#         sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
#     # 写第一列
#     for i in range(0, len(colum0)):
#         sheet1.write(i + 1, 0, colum0[i], set_style('Times New Roman', 220, True))
#     # 写第二列
#     for i in range(0, len(colum1)):
#         sheet1.write(i + 1, 1, colum1[i], set_style('Times New Roman', 220, True))
#         # sheet1.write(1, 3, '2006/12/12')
#         # sheet1.write_merge(6, 6, 1, 3, '未知')  # 合并行单元格
#         # sheet1.write_merge(1, 2, 3, 3, '打游戏')  # 合并列单元格
#         # sheet1.write_merge(4, 5, 3, 3, '打篮球')
#         f.save('test.xls')

def read_excel():
    # 打开文件
    readbook = xlrd.open_workbook(r'E:\sample.xlsx')
    # writebook = xlwt.Workbook()#打开一个excel
    # sheet = writebook.add_sheet('test')#在打开的excel中添加一个sheet

    # 获取读入的文件的第一个sheet
    table = readbook.sheets()[0]
    user = table.cell(1, 0).value  # 获取1行1列的表格值
    password = table.cell(1, 1).value  # 获取1行2列的表格值
    # result = gcj02towgs84(user, password)
    print(user, password)

    # 获取sheet的行数
    # nrows = table.nrows

    # for i in range(nrows):
    #   if i == 0:#我处理的数据第一行是属性名，所以去掉
    #     continue
    #   lng = table.cell(i,3).value#获取i行3列的表格值
    #   lat = table.cell(i,4).value#获取i行4列的表格值
    #   result = gcj02towgs84(lng,lat)#引用转换函数
    #   print(i)
    #   sheet.write(i,0,result[0])#写入excel
    #   sheet.write(i,1,result[1])

    # writebook.save('answer.xls')


if __name__ == '__main__':
    read_excel()
    # write_excel()
