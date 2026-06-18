import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine

# Database Connection
engine = create_engine('postgresql://postgres:umeanor01@localhost:5432/ecommerce_lifecycle_db')

print("Generating e-commerce dimension tables...")

# 1. Populate dim_products
categories = ['Electronics', 'Apparel', 'Home & Kitchen', 'Beauty', 'Sports']
products = []
for i in range(50):
    products.append({
        "product_id": f"PROD-{2000+i}",
        "product_name": f"Premium {random.choice(categories)} Item {i}",
        "category": random.choice(categories)
    })
pd.DataFrame(products).to_sql('dim_products', engine, if_exists='append', index=False)

# 2. Populate dim_customers (Acquired over a 6-month window)
channels = ['Paid Search', 'Organic Social', 'Direct Traffic', 'Affiliate']
customers = []
start_date = datetime(2025, 1, 1)

for i in range(1500):
    signup_dt = start_date + timedelta(days=random.randint(0, 180))
    customers.append({
        "customer_id": f"CUST-{5000+i}",
        "signup_date": signup_dt.date(),
        "acquisition_channel": random.choice(channels)
    })
df_cust = pd.DataFrame(customers)
df_cust.to_sql('dim_customers', engine, if_exists='append', index=False)

print("Simulating structured cohort purchase behaviors...")

# Fetch keys from DB to map correctly
cust_keys = pd.read_sql("SELECT customer_key, signup_date FROM dim_customers", engine)
prod_keys = pd.read_sql("SELECT product_key FROM dim_products", engine)['product_key'].tolist()

orders = []
# 3. Populate fact_order_items with dynamic decay curves
for _, customer in cust_keys.iterrows():
    c_key = customer['customer_key']
    signup_dt = customer['signup_date']
    
    # Simulate a lifetime number of transactions based on geometric decay
    # This creates a realistic "retention drop-off" for your cohort analysis
    num_purchases = np.random.geometric(p=0.4) 
    num_purchases = min(num_purchases, 8) # cap at 8 orders max
    
    current_order_date = signup_dt
    for order_num in range(num_purchases):
        # Space out subsequent orders realistically by 15 to 45 days
        if order_num > 0:
            current_order_date += timedelta(days=random.randint(15, 45))
        
        # Ensure we don't simulate transactions past our current analytical cutoff date
        if current_order_date > datetime(2025, 12, 31).date():
            break
            
        p_key = random.choice(prod_keys)
        net_rev = round(random.uniform(15.0, 120.0), 2)
        order_id = f"ORD-{100000 + len(orders)}"
        
        orders.append({
            "order_id": order_id,
            "customer_key": c_key,
            "product_key": p_key,
            "order_date": current_order_date,
            "net_revenue": net_rev
        })

pd.DataFrame(orders).to_sql('fact_order_items', engine, if_exists='append', index=False)
print(f"Successfully generated and injected {len(orders)} order line items with explicit retention curves!")