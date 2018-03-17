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

        name_employee = employee[0].text
        print(name_employee)

    # creating XML Node and filling oft subtags
    new_employee_tag = doc.createElement("employee")
    new_employee_name_tag = doc.createElement("name")
    new_employee_email_tag = doc.createElement("email")

    new_employee_name_field = doc.createTextNode("John Smith")
    new_employee_email_field = doc.createTextNode("SmithJ@gmail.com")

    new_employee_name_tag.appendChild(new_employee_name_field)
    new_employee_email_tag.appendChild(new_employee_email_field)

    new_employee_tag.appendChild(new_employee_name_tag)
    new_employee_tag.appendChild(new_employee_email_tag)

    print("Information about the new employee:")
    print(new_employee_tag.toprettyxml())

    # Add new employee to company
    doc.childNodes[0].appendChild(new_employee_tag)
    print("Now in company works {} employees.".format(doc.getElementsByTagName("employee").length))


if __name__ == "__main__":
    main()
