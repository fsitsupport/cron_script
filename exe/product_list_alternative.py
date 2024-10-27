# product_list_alternativ.py
import random
# Creating arrays mit headlines and sample data
array = [
    ["Produkt_name", "Price", "Inventory"],  # headlines
    ["ProduktA", 10, 5],
    ["ProduktB", 20, 0],
    ["ProduktC", 30, 3],
    ["ProduktD", 20, 0],
    ["ProduktE", 10, 2],
    ["ProduktF", 40, 1],
]
# Set maximum number of rows (without the headlines)
max_rows = len(array) - 1
# chose random index i  (1 to max_rows)
i = random.randint(1, max_rows)
# call product name from row i
produkt_name = array[i][0]
# output
print(f"In row/index {i} is {array[0][0]} = {array[i][0]}.")