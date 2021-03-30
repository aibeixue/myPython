from lxml import etree

root=etree.Element('root')
a=etree.SubElement(root,'a')
b=etree.SubElement(root,'b')
c=etree.SubElement(root,'c')
d=etree.SubElement(root,'d')
e=etree.SubElement(d,'e')
#获取父级节点
# print(b.getparent().tag)
#获取紧挨着的下一个节点
# print(b.getnext().tag)
#获取前面一个节点
print(b.getprevious().tag)
print('********************************')

#具体获取一个节点及其包括的节点信息
tree=etree.ElementTree(d)
# print(tree.getroot().tag)
# print(etree.tostring(tree))

ele=tree.getroot()
# print(ele.tag)
# print(ele.getparent().tag)
# print(ele.getroottree().getroot().tag)

print('*************************************')
list1=[ child.tag for child in root ]
# print(list1)
list2=[ el.tag for el in root.iter() ]
# print(list2)

list3=[ child.tag for child in root.iterchildren() ]
# print(list3)
list4=[ child.tag for child in root.iterchildren(reversed=True) ]
# print(list4)
list5=[ sibling.tag for sibling in b.itersiblings() ]
# print(list5)
list6=[ sibling.tag for sibling in c.itersiblings(preceding=True) ]
# print(list6)
list7=[ ancestor.tag for ancestor in e.iterancestors() ]
# print(list7)
list8=[ el.tag for el in root.iterdescendants() ]
# print(list8)
print('***************************************************************')

li1=[ child.tag for child in root.iterchildren('a') ]
# print(li1)
li2=[ child.tag for child in d.iterchildren('a') ]
# print(li2)
li3=[ el.tag for el in root.iterdescendants('d') ]
# print(li3)
li4=[ el.tag for el in root.iter('d') ]
# print(li4)
li5=[ el.tag for el in root.iter('d', 'a') ]
# print(li5)
print('***************************************************')
print(root[0].tag)