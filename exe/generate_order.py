# generate_order.py
# This script should output orders randomly
# all files should be written and not pre-exist before.
# add real random numbers, no pseudo ... maybe another day :)

# Import Random
from random import randint
# Import datetime to output timestamps
from datetime import datetime
# Import porduct_list
from product_list import products as p
# Set the currenttime function to variable to be called / used to differ filenames
current_time = datetime.now()
# Random num to get key-value pair, the highest num is the amount of orders available (len(p))
# randint() gives us a random product from the indexnumbers available (0-5)
product_picker = randint(0, len(p))
# run through the products-list in product_list.py; index from 0 to 5 for 6 products
# enumerate index and item = key and value
for index, item in enumerate(p): # in (0,len(p)) or enumerate(p)
    # execute only if a number from 0 to 5 is generated by randint()
    if index == product_picker:
        print(len(p), "is maximum number of products. Random order of index", product_picker, "was created.")
        # loop through the key-value pairs in products (p) and print them into a text file
        for key, value in item:
            # set variable for filename in combination with datetime.now() for the date in it
            filename = current_time.strftime("../orders/order_%Y-%m-%d_%H-%M-%S.txt")
            # append the key-value pairs to a text file (e.g. order_2024-10-18_17-06-24.txt)
            with open(filename, 'a') as file:
                # call the variables to write the product-data in the .txt-file
                print(f"{key}: {value}",file=file)