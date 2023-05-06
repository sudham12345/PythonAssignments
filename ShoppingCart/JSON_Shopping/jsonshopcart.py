import CustShoppingCart

def process_shop_cart(shopcartfile):
    
    #Creating a shopping_cart instance imported from CustShoppingCart.py

    l_CustId = shopcartfile["CustId"]
    l_CustName = shopcartfile["CustName"]
    l_CustAddress = shopcartfile["CustAddress"]
    c1=CustShoppingCart.shopping_cart(l_CustId, l_CustName, l_CustAddress)

    #Program to call the add and remove product methods from CustShoppingCart

    pl_index=0
    
    for pl in shopcartfile["ProductsList"]:
        c_cart={}
        c_cart["ProdId"] = pl["ProdId"]
        c_cart["ProdName"],c_cart["ProdPrice"] = get_prod_price(pl["ProdId"])
        c_cart["Qty"] = pl["Qty"]
        c_cart["ProdPrice"] *= c_cart["Qty"]

        if pl["CustAct"] == 'a':
            c1.add_product_to_cart(c_cart)
        elif pl["CustAct"] == 'r':
            c1.remove_product_from_cart(c_cart)
        else:
            print("Customer action field should have a value of 'a' or 'r'")

        pl_index += 1

    c1.show_cart()


#Method to fetch product details from Prodfile

def get_prod_price(l_ProdId):

    from CS_caller_json import prodfile

    for pf in prodfile:
        if l_ProdId == pf["ProdId"]:
            return pf["ProdName"],pf["ProdPrice"]
            
