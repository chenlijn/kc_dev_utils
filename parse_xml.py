
'''codes for parsing xml file'''

import xml.etree.ElementTree as ET

tree = ET.parse('6.xml')
root = tree.getroot()

#for child in root:
#    if child.tag == 'object':
#        for chd in child:
#            #if chd.tag == 'bndbox'
#            #for ch in chd:
#            print chd['name']
#            print(chd.tag, chd.attrib)

children = root.findall("object")
print children
for child in children:
    print child[0].text
    box=child.findall("bndbox")
    xmin = box[0].findtext("xmin")
    ymin = box[0].findtext("ymin")
    xmax = box[0].findtext("xmax")
    ymax = box[0].findtext("ymax")
    print "box: xmin {}, ymin {}, xmax {}, ymax {}".format(xmin, ymin, xmax, ymax)




