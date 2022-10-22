from xml.etree.ElementTree import Comment


Comment=input("enter any comment:")
if("make a lot of money" in Comment or "by now" in Comment or "subscibe this" in Comment or "click this" in Comment or "write a program" in Comment):
    print("spam comment")
else:
    print("not a spam comment")    