# xml文本节点读取方法
from xml.dom import minidom
# 打开文件
dom=minidom.parse('Class_info.xml')
# 获取文档对象元素
root=dom.documentElement
# 根据标签名称获取标签对象
names=root.getElementsByTagName('name')
ages=root.getElementsByTagName('age')
citys=root.getElementsByTagName('city')
# 分别打印显示xml文档标签对里面的内容
for i in range(4):
    print(names[i].firstChild.data)
    print(ages[i].firstChild.data)
    print(citys[i].firstChild.data)
    print("")