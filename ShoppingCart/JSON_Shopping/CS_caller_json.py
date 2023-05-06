
import json
import jsonvalidator
import jsonshopcart

#Validate the product file

file1='JSON_Shopping\\product.json'
file2='JSON_Shopping\\prodschema.json'

if jsonvalidator.validate(file1,file2):
    with open (file1) as f:
        prodfile = json.load(f)
else:
    exit()


#Validate the shopping cart file

file1='JSON_Shopping\\shoppingcart.json'
file2='JSON_Shopping\\shoppingschema.json'

if jsonvalidator.validate(file1,file2):
    with open (file1) as f:
        shopcartfile = json.load(f)
else:
    exit()


# Call the Process_shop_cart method with shopcartfile and prodfile as arguments

jsonshopcart.process_shop_cart(shopcartfile)