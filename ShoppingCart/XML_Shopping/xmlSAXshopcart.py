
import xml.sax
import xmlDOMprodprice
import CustShoppingCart
            
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
            l_ProdName_val,l_ProdPrice_val = xmlDOMprodprice.get_prod_price(self.ProdId)
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

