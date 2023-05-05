
class shopping_cart():

    def __init__(self, p_custid, p_custname, p_custaddress):
        
        self.CustId = p_custid
        self.CustName = p_custname
        self.CustAddress = p_custaddress
        self.customer_cart = []
 
    #Method to add a product to customer cart

    def add_product_to_cart(self,p_customer_cart):
        
        cart_index=0
        
        if self.customer_cart==[]:
            self.customer_cart.append(p_customer_cart)
            return
        
        for cs in self.customer_cart:
        
            if cs["ProdId"]==p_customer_cart["ProdId"]:
                self.customer_cart[cart_index]["Qty"]+=p_customer_cart["Qty"]
                self.customer_cart[cart_index]["ProdPrice"]+=p_customer_cart["ProdPrice"]
                return
            cart_index+=1
        
        self.customer_cart.append(p_customer_cart)
        
    #Method to remove a product from customer cart 
            
    def remove_product_from_cart(self,p_customer_cart):

        cart_index=0

        if self.customer_cart==[]:
            print("Cart for customer",self.CustName,"is empty")
            return
        
        for cs in self.customer_cart:
            if cs["ProdId"]==p_customer_cart["ProdId"]:
                self.customer_cart[cart_index]["Qty"]-=p_customer_cart["Qty"]
                self.customer_cart[cart_index]["ProdPrice"]-=p_customer_cart["ProdPrice"]
                if self.customer_cart[cart_index]["Qty"] <=0:
                    del(self.customer_cart[cart_index])
            cart_index+=1
        
    #Method to display the customer cart

    def show_cart(self):

        self.total=0

        print('\n')
        print("************************************")
        print("Cart for customer",self.CustName)
        print("-------------------------------------")
        print("Customer Id     :", self.CustId)
        print("Customer Address:", self.CustAddress)
        print("*************************************")
        print("Prod ID    ProdName    Qty    Price")
        print("-------------------------------------")
        for sc in self.customer_cart:
            self.total += sc["ProdPrice"]
            print(f'{sc["ProdId"]:<10}',
                  f'{sc["ProdName"]:11}',
                  f'{sc["Qty"]:<6}',
                  format(sc["ProdPrice"],".2f"))
            
        print("-------------------------------------")
        print("Total price :", f'{self.total:>21}')
        print("-------------------------------------")