# product_list.py
# Import datetime to output timestamps
from datetime import datetime
# Set the currenttime function to variable to be called / used to differ filenames
current_time = datetime.now()
date_recieved = current_time.strftime("%Y-%m-%d_%H-%M-%S")
# Productlist - to process with 'takeorder01.py; contains 3x Key-Value Pair
# 1. key=productname, value=Shirt 
# 2. key=price, value=number 
# 3. key=date_recieved, value=date-variable
# 6 lists of tuples
products = [
    [('productname', 'Cap'), ('price', 50), ('date_recieved', date_recieved)],
    [('productname', 'Hoody'), ('price', 40), ('date_recieved', date_recieved)],
    [('productname', 'T-Shirt'), ('price', 20), ('date_recieved', date_recieved)],
    [('productname', 'Longsleave'), ('price', 30), ('date_recieved', date_recieved)],
    [('productname', 'Shorts'), ('price', 15), ('date_recieved', date_recieved)],
    [('productname', 'Socks'), ('price', 10), ('date_recieved', date_recieved)]
]
# index = productname, price, 'date_recieved' - value = Cap, 50, date_recieved_VAR