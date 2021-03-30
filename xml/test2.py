from collections import deque
from lxml import etree

root=etree.XML('<root><a><b/><c/></a><d><e/></d></root>')
print(etree.tostring(root,pretty_print=True))
queue=deque([root])
while queue:
    el=queue.popleft()
    queue.extend(el)
    print(el.tag)
