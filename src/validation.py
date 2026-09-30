import pandas

def validate_customers(customers):
    report = {}
    report['total_record'] = len(customers)
    report['duplicate_record'] = customers.duplicated().sum()
    report['missing_customer_ids'] = customers['customer_id'].isna().sum()
    report['invalid_ages'] = ((~customers['age'].between(18,120)) | customers['age'].isna()).sum()
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    report['invalid_emails'] = ((~customers['email'].str.match(email_pattern,na=False))).sum()
    valid_cities = ['Pune','Mumbai','Delhi','Surat']
    report['invalid_cities'] = (~customers['city'].isin(valid_cities)).sum()
    return report

def validate_orders(orders, customers):
    report = {}
    report['total_orders'] = len(orders)
    report['duplicate_orders'] = orders['order_id'].duplicated().sum()
    report['missing_order_id'] = orders['order_id'].isna().sum()
    report['missing_customer_id'] = orders['customer_id'].isna().sum()
    report['invalid_quantities'] = (orders['quantity'] <= 0 | orders['quantity'].isna()).sum()
    report['invalid_price'] = (orders['unit_price'] <= 0 | orders['unit_price'].isna()).sum()
    report['invalid_order_date'] = (orders['order_date'].isna()).sum()
    valid_customer_id = customers['customer_id'].dropna()
    report['unmatched_customer_ids'] = (~orders['customer_id'].isin(valid_customer_id)).sum()
    return report

def validate_payments(payments,orders):
    report = {}
    report['total_payments'] = len(payments)
    report['duplicate_payments'] = payments['payment_id'].duplicated().sum()
    report['missing_payment_ids'] = payments['payment_id'].isna().sum()
    report['missing_order_ids'] = payments['order_id'].isna().sum()
    report['invalid_payment_dates'] = payments['payment_date'].isna().sum()
    valid_methods = ['Upi','Card','Cash','Net Banking']
    report['invalid_payment_methods'] = (~payments['payment_method'].isin(valid_methods)).sum()
    valid_statuses = ["Paid","Failed","Pending"]
    report['invalid_payment_status'] = payments['payment_status'].isin(valid_statuses).sum()
    valid_order_ids = orders['order_id'].dropna()
    report['unmatched_order_ids'] = (~payments['order_id'].isin(valid_order_ids)).sum()
    return report


