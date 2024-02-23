import sqlite3

conn = sqlite3.connect('products.db')
c = conn.cursor()
# print("Executing insert...")
# c.execute("INSERT INTO product_details (name, price, delivery_time, needle_size, composition) VALUES ('test name', 32, 4, 2, 'compo test')")
# conn.commit()

print("Executing select...")
rows = c.execute("SELECT * FROM product_details")
for row in rows:
    print("ID = ", row[0])
    print("URL = ", row[1])
    print("NAME = ", row[2])
    print("PRICE = ", row[3])
    print("DELIVERY TIME = ", row[4])
    print("NEEDLE SIZE = ", row[5])
    print("COMPOSITION = ", row[6])
    print("IMAGE = ", row[7])
    print("----------------------------------------")
print("END")

c.execute("DROP TABLE product_details")
conn.commit()
conn.close()