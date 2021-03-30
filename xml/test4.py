from lxml import etree



def getOrder(root):
    OrderNoList = []
    order=[]
    for child in root:
        print(child)
        attributes = child.attrib
        attr=attributes['OrderNo']
        if attr not in OrderNoList:
            OrderNoList.append(attr)
            order.append(child)
    print(order)















# rootSibilings=[ child for child in root.iterchildren() ]
# for line in rootSibilings:
#     print(line)


if __name__=='__main__':
    tree = etree.parse('data.xml')
    root = tree.getroot()
    oderlist=getOrder(root)
    print(oderlist)










