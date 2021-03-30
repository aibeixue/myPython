from lxml import etree

root=etree.Element('root')
print(root.tag)
root.append( etree.Element("child1") )
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

print(etree.tostring(root,pretty_print=True))
child = root[0]
print(child.tag)
print(len(root))
children=list(root)
print(children)
root.insert(0,etree.Element('child0'))
print(root[:1],type(root[:1]))
print(root[:1][0].tag)
print(root[-1:])

if len(root)!=0:
    print('root有孩子')
print(root[0] is root[1].getprevious())
print(root[1] is root[0].getnext())

for child in root:
    print(child.tag)