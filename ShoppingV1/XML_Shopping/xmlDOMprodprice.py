import xml
from xml.dom import minidom

def get_prod_price(prodfile,P_ProdId):

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
            