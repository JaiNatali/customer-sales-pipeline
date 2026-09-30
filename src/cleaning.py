import pandas as pd

def clean_customer(customers):
    customers = customers.copy()
    customers['name'] = (customers['name'].str.strip().str.title())
    customers['email'] = (customers['email'].str.strip().str.lower())
    customers['city'] = (customers['city'].str.strip().str.title())
    customers['signup_date'] = pd.to_datetime(customers['signup_date'])
    return customers

def clean_orders(orders):
    orders = orders.copy()
    orders["order_date"] = pd.to_datetime(orders['order_date'])
    orders['product'] = orders['product'].str.strip().str.title()
    orders['category'] = orders['category'].str.strip().str.title()
    orders['quantity'] = pd.to_numeric(orders['quantity'],errors='coerce')
    orders['unit_price'] = pd.to_numeric(orders['unit_price'],errors='coerce')
    orders['revenue'] = orders['quantity'] * orders['unit_price']
    orders['year'] = orders['order_date'].dt.year
    orders['month'] = orders['order_date'].dt.month
    orders['day'] = orders['order_date'].dt.day
    orders['month_name'] = orders['order_date'].dt.month_name()
    return orders

def clean_payment(payments):
    payments = payments.copy()
    payments['payment_date'] = pd.to_datetime(payments['payment_date'],errors='coerce')
    payments['payment_method'] = payments['payment_method'].str.strip().str.title()
    payments['payment_status'] = payments['payment_status'].str.strip().str.title()
    return payments


