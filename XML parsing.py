# let's study how work with XML in python

import xml.dom.minidom
import xml.etree.ElementTree as ET


def main():
    # load and parse source xml data
    doc = xml.dom.minidom.parse("data.xml")

    employees_list = doc.getElementsByTagName("employee")

    print("The company has %d employees." % employees_list.length)
    # print information about each employee
    for employee in employees_list:
        print(employee.toxml())

    # parsing XML using ElementTree
    tree = ET.parse('data.xml')
    company = tree.getroot()

    for employee in company:
        # print name of each employee in company
        print(employee[0].text)


if __name__ == "__main__":
    main()
