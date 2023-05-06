
import xmlvalidator
import xmlSAXshopcart

#Validate the product file

file1='XML_Shopping\\productschema.xsd'
file2='XML_Shopping\\product.xml'
if xmlvalidator.validate(file1,file2):
    prodfile = file2
else:
    exit()

#Validate the shopping cart file

file1='XML_Shopping\\shoppingcartschema.xsd'
file2='XML_Shopping\\shoppingcart.xml'


if xmlvalidator.validate(file1,file2):
    shopcartfile = file2
else:
    exit()


# Call the SAXprocessXML function in xmlSAXshopcart with shopcartfile as an argument

xmlSAXshopcart.SAXprocessXML(shopcartfile)