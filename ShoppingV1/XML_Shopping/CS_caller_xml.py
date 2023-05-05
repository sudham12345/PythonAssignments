import xmlvalidator
#import xmlSAXshopcart
import xml
import xml.sax
import xmlDOMprodprice
import CustShoppingCart
from xml.dom import minidom

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


def get_prod_price(P_ProdId):

  #  xmldoc = minidom.parse('C:\\Sudha\\Python\\Shopping\\product.xml')
    xmldoc = minidom.parse(prodfile)

    l_ProductList = xmldoc.getElementsByTagName("ProductList")

    for pl in l_ProductList:

        l_Product = pl.getElementsByTagName("Product")

        for p in l_Product:

            l_ProdId = p.getElementsByTagName("ProdId")[0] 
            l_ProdId_val = l_ProdId.childNodes[0].nodeValue
        
            if P_ProdId == l_ProdId_val:
                l_ProdName = p.getElementsByTagName("ProdName")[0]
                l_ProdName_val = l_ProdName.childNodes[0].nodeValue
                l_ProdPrice = p.getElementsByTagName("ProdPrice")[0]
                l_ProdPrice_val = l_ProdPrice.childNodes[0].nodeValue
                return l_ProdName_val, l_ProdPrice_val               
            
# Define a class that inherits from xml.sax.ContentHandler
class TIContentHandler(xml.sax.ContentHandler):
    
    def __init__(self):
        
        xml.sax.ContentHandler.__init__(self)
        self.CurrentData = ""
        self.ctag = ""
        
        
    # This method is called every time a new element is encountered in the XML file
    def startElement(self, name, attrs):
        
        self.CurrentData = name
    
    # This method is called every time character data is encountered inside an element
    def characters(self, content):
    
        if self.CurrentData == "CustId" and self.CurrentData != self.ctag:
            self.ctag = self.CurrentData
            self.CustId= content
            self.flag = True
        
        elif self.CurrentData == "CustName" and self.CurrentData != self.ctag:
            self.ctag = self.CurrentData
            self.CustName= content

        elif self.CurrentData == "CustAddress" and self.CurrentData != self.ctag:
            self.ctag = self.CurrentData
            self.CustAddress= content
        
        elif self.CurrentData == "ProdId" and self.CurrentData != self.ctag:
            self.ctag = self.CurrentData
            self.ProdId = content 
            l_ProdName_val,l_ProdPrice_val = get_prod_price(self.ProdId)
            self.ProdName = l_ProdName_val
            self.ProdPrice = l_ProdPrice_val

        elif self.CurrentData == "Qty" and self.CurrentData != self.ctag:
            self.ctag = self.CurrentData
            self.Qty = content

        elif self.CurrentData == "CustAct" and self.CurrentData != self.ctag:
            self.ctag = self.CurrentData
            if self.flag:
                self.c1=CustShoppingCart.shopping_cart(self.CustId,self.CustName,self.CustAddress)
                self.flag = False

            c_cart={}
            c_cart["ProdId"] = self.ProdId
            c_cart["ProdName"] = self.ProdName

            l_Qty = self.Qty
            c_cart["Qty"] = int(l_Qty)
        
            l_ProdPrice_val = self.ProdPrice
            c_cart["ProdPrice"] = float(l_ProdPrice_val)
            
            c_cart["ProdPrice"] *= c_cart["Qty"]

            if content == 'a':
                self.c1.add_product_to_cart(c_cart)
            elif content == 'r':
                self.c1.remove_product_from_cart(c_cart)
            else:
                print("Customer action field should have a value of 'a' or 'r'")


    # This method is called every time the end of an element is encountered
    def endElement(self, name):
        
        if name == 'Customer':
            self.c1.show_cart()
        else:
            pass


# This function processes an XML file using the SAX parser and the TIContentHandler class
def SAXprocessXML(sourceFileName):
  
  source = open(sourceFileName)
  # Parse the XML file using the SAX parser and the TIContentHandler class
  xml.sax.parse(source, TIContentHandler())


#def process_shop_cart(shopcartfile,Prodfile):
 #   prodfile = Prodfile
 #   SAXprocessXML(shopcartfile)
# Call the process_shop_cart function in xmlSAXshopcart.py.

SAXprocessXML(shopcartfile)
