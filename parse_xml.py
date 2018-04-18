
'''codes for parsing xml file'''

import xml.etree.ElementTree as ET


def get_detection_rectangle(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    children = root.findall("object")
    rectangles = [] # np.zeros((len(children), 4))
    for idx, child in enumerate(children):
        #print child[0].text
        rect = []
        box=child.find("bndbox")
        rect.append(int(box.findtext("xmin")))
        rect.append(int(box.findtext("ymin")))
        rect.append(int(box.findtext("xmax")))
        rect.append(int(box.findtext("ymax")))
        rectangles.append(rect)

    return rectangles


def get_segmentation_polygon(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    children = root.findall("object")
    polygons = []
    for idx, child in enumerate(children):
        poly = []
        poly_object = child.find('polygon')
        for point in poly_object:
            p = []
            p.append(point.text.split(',')[0])
            p.append(point.text.split(',')[-1])
            poly.appen(map(int, p)))
        polygons.append(np.array(poly))
    return polygons





if __name__ == '__main__':

    get_detection_rectangle('6.xml')
    #get_segmentation_polygon('6.xml')



