# xml子节点读取方法
from xml.dom import minidom

dom=minidom.parse('Class_info.xml')

root=dom.documentElement

students=root.getElementsByTagName('student')

print(students[0].nodeName)
print(students[0].nodeValue)
print(students[0].nodeType)