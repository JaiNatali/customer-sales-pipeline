import pandas as pd
from cleaning import clean_customer,clean_orders,clean_payment
from validation import validate_customers,validate_orders,validate_payments
from analysis import customer_summary,order_summary,category_summary,payment_summary,payment_method_summary
from reports import save_cleaned_date,save_data_quality_report,save_customer_summary,save_sales_report


CUSTOMERS_FILE = 'data/raw/customers.xlsx'
ORDERS_FILE = "data/raw/orders.xlsx"
PAYMENTS_FILE = "data/raw/payments.xlsx"

def load_data():
    customers = pd.read_excel(CUSTOMERS_FILE)
    orders = pd.read_excel(ORDERS_FILE)
    payments = pd.read_excel(PAYMENTS_FILE)
    return customers, orders, payments

def main():
    customers,orders,payments = load_data()
    customers = clean_customer(customers)
    orders = clean_orders(orders)
    payments = clean_payment(payments)

    customer_validation = validate_customers(customers)
    order_validation = validate_orders(orders,customers)
    payment_validation = validate_payments(payments,orders)

    print("Customers:")
    print(customers.shape)
    print(customers.head())
    print(customer_validation)

    print("\nOrders:")
    print(orders.shape)
    print(orders.head())
    print(order_validation)

    print("\nPayments:")
    print(payments.shape)
    print(payments.head())
    print(payment_validation)

    customer_report = customer_summary(customers, orders)
    order_report = order_summary(orders)
    category_report = category_summary(orders)
    payment_report = payment_summary(payments)
    payment_method_report = payment_method_summary(payments)

    print("\nCustomer Summary:")
    print(customer_report.head())

    print("\nOrder Summary:")
    print(order_report)

    print("\nCategory Summary:")
    print(category_report)

    print("\nPayment Summary:")
    print(payment_report)

    print("\nPayment Method Summary:")
    print(payment_method_report)

    save_cleaned_date(
        customers,
        orders,
        payments
    )

    save_data_quality_report(
        customer_validation,
        order_validation,
        payment_validation
    )

    save_customer_summary(
        customer_report
    )

    save_sales_report(
        order_report,
        category_report,
        payment_report,
        payment_method_report
    )

if __name__ == "__main__":
    main()