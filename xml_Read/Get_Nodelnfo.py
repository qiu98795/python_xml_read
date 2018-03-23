# xml元素节点读取方法
from xml.dom import minidom

# 打开xml文件
dom=minidom.parse('Class_info.xml')
# 获取文档对象元素
root=dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
