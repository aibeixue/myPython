from lxml import etree
tree=etree.parse('data.xml')
root=tree.getroot()
boxList=[child.tag for child in root]
print(boxList)
boxNum= len(boxList)
print(f'总共有{boxNum}个柜子')
list1=[ child.tag for child in root.iterchildren() ]
print(list1)
list2=[ child.tag for child in root.iterchildren(reversed=True) ]
print(list2)
list3=[ sibling.tag for sibling in list1[0].itersiblings() ]


