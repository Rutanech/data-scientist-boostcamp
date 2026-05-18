import sqlite3
import random
from datetime import datetime, timedelta

random.seed(42)

import pathlib
DB_PATH = str(pathlib.Path(__file__).parent / "ecommerce.db")

# remove if exists
import os
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# ---- Schema ----
cur.executescript("""
CREATE TABLE customers (
    customer_id   INTEGER PRIMARY KEY,
    first_name    TEXT NOT NULL,
    last_name     TEXT NOT NULL,
    email         TEXT,
    city          TEXT,
    country       TEXT,
    signup_date   TEXT
);

CREATE TABLE products (
    product_id    INTEGER PRIMARY KEY,
    product_name  TEXT NOT NULL,
    category      TEXT,
    price         REAL,
    cost          REAL
);

CREATE TABLE orders (
    order_id      INTEGER PRIMARY KEY,
    customer_id   INTEGER,
    order_date    TEXT,
    status        TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id      INTEGER,
    product_id    INTEGER,
    quantity      INTEGER,
    unit_price    REAL,
    FOREIGN KEY (order_id)   REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")

# ---- Customers ----
first_names = ["Somchai","Suda","Anan","Nicha","Krit","Ploy","Tul","Mint","Boss","Fern",
               "John","Emily","Hiro","Yui","Mei","Wei","Ravi","Aisha","Lars","Marco",
               "Sara","Daan","Kai","Niran","Praew","Ton","Beam","Aom","Mook","Jane"]
last_names  = ["Wong","Suk","Chai","Ito","Smith","Garcia","Singh","Kim","Tan","Park",
               "Phan","Lee","Brown","Anand","Lim","Sato","Wang","Patel","Mueller","Costa"]
cities = [("Bangkok","Thailand"),("Chiang Mai","Thailand"),("Phuket","Thailand"),
          ("Singapore","Singapore"),("Tokyo","Japan"),("Osaka","Japan"),
          ("Seoul","South Korea"),("Hanoi","Vietnam"),("Jakarta","Indonesia"),
          ("Manila","Philippines"),("Kuala Lumpur","Malaysia"),("Taipei","Taiwan")]

customers = []
start = datetime(2024,1,1)
for i in range(1, 51):
    fn = random.choice(first_names)
    ln = random.choice(last_names)
    city, country = random.choice(cities)
    signup = start + timedelta(days=random.randint(0, 500))
    email = f"{fn.lower()}.{ln.lower()}{i}@example.com"
    customers.append((i, fn, ln, email, city, country, signup.strftime("%Y-%m-%d")))

cur.executemany("INSERT INTO customers VALUES (?,?,?,?,?,?,?)", customers)

# ---- Products ----
products_data = [
    ("Wireless Mouse",      "Electronics",  590,  250),
    ("Mechanical Keyboard", "Electronics", 2490, 1200),
    ("USB-C Cable",         "Electronics",  190,   60),
    ("Bluetooth Speaker",   "Electronics", 1290,  600),
    ("Laptop Stand",        "Accessories",  790,  300),
    ("Notebook A5",         "Stationery",   120,   40),
    ("Ballpoint Pen Pack",  "Stationery",    90,   25),
    ("Sticky Notes",        "Stationery",    60,   15),
    ("Coffee Mug",          "Home",         250,   80),
    ("Desk Lamp",           "Home",         990,  400),
    ("Yoga Mat",            "Sports",       690,  250),
    ("Water Bottle",        "Sports",       290,  100),
    ("Running Shoes",       "Sports",      2890, 1300),
    ("Backpack",            "Accessories", 1490,  600),
    ("Sunglasses",          "Accessories",  890,  350),
    ("T-Shirt Plain",       "Apparel",      390,  150),
    ("Cap",                 "Apparel",      290,  100),
    ("Hoodie",              "Apparel",      990,  420),
    ("Smart Watch",         "Electronics", 4990, 2300),
    ("Headphones",          "Electronics", 1990,  900),
]
for pid, (name, cat, price, cost) in enumerate(products_data, start=1):
    cur.execute("INSERT INTO products VALUES (?,?,?,?,?)", (pid, name, cat, price, cost))

# ---- Orders + order_items ----
statuses = ["completed","completed","completed","completed","cancelled","refunded","pending"]
order_id_counter = 1
order_rows = []
item_rows = []

for cust_id, *_, signup_str in customers:
    signup_dt = datetime.strptime(signup_str, "%Y-%m-%d")
    n_orders = random.choices([0,1,2,3,4,5,6,7], weights=[2,3,4,4,3,2,1,1])[0]
    for _ in range(n_orders):
        days_after = random.randint(1, 540)
        order_dt = signup_dt + timedelta(days=days_after)
        if order_dt > datetime(2026,5,16):
            continue
        status = random.choice(statuses)
        order_rows.append((order_id_counter, cust_id, order_dt.strftime("%Y-%m-%d"), status))
        # 1-4 items per order
        n_items = random.randint(1,4)
        chosen = random.sample(range(1, len(products_data)+1), n_items)
        for pid in chosen:
            qty = random.randint(1,3)
            unit_price = products_data[pid-1][2]
            # occasional discount
            if random.random() < 0.15:
                unit_price = round(unit_price * 0.9, 2)
            item_rows.append((order_id_counter, pid, qty, unit_price))
        order_id_counter += 1

cur.executemany("INSERT INTO orders VALUES (?,?,?,?)", order_rows)
cur.executemany("INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?,?,?,?)", item_rows)

conn.commit()

# quick sanity check
for tbl in ["customers","products","orders","order_items"]:
    cur.execute(f"SELECT COUNT(*) FROM {tbl}")
    print(tbl, cur.fetchone()[0])

conn.close()
print("DB written to", DB_PATH)
