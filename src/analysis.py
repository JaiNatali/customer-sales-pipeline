import pandas as pd

def customer_summary(customers, orders):
    customer_orders = customers.merge(orders,on='customer_id',how='left')
    summary = (
        customer_orders
        .groupby(
            ['customer_id','name','city']
        )
        .agg(
            total_orders=('order_id','count'),
            total_revenue=('revenue','sum'),
            average_order_value=('revenue','mean'),
            largest_order=('revenue','max'),
            smallest_order=('revenue','min')
        )
    )
    return summary

def order_summary(orders):
    summary = {
        'total_orders': len(orders),
        'total_quantity': orders['quantity'].sum(),
        'total_revenue': orders['revenue'].sum(),
        'average_order_value': orders['revenue'].mean(),
        'largest_order' : orders['revenue'].max(),
        'smallest_order': orders['revenue'].min(),
    }
    return summary

def category_summary(orders):
    summary = (
        orders
        .groupby("category", as_index=False)
        .agg(
            total_orders=("order_id", "count"),
            total_quantity=("quantity", "sum"),
            total_revenue=("revenue", "sum"),
            average_order_value=("revenue", "mean")
        )
        .sort_values("total_revenue", ascending=False)
    )
    return summary

def payment_summary(payments):
    summary ={
        'total_payments': len(payments),
        'paid_payments': (payments['payment_status'] == 'Paid').sum(),
        'failed_payments': (payments['payment_status'] == 'Failed').sum(),
        'pending_payments': (payments['payment_status'] == 'Pending').sum()
    }
    return summary

def payment_method_summary(payments):
    summary = (
        payments.groupby('payment_method',as_index=False)
        .agg(
            total_payments=('payment_id','count')
        )
        .sort_values('total_payments', ascending=False)
    )
    return summary


