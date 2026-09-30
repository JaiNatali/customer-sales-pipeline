import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path('data/output')

def create_output_directory():
    OUTPUT_DIR.mkdir(parents=True,exist_ok=True)

def save_cleaned_date(customers,orders,payments):
    create_output_directory()
    file_path = OUTPUT_DIR / "cleaned_data.xlsx"
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        customers.to_excel(
            writer,
            sheet_name='Customers',
            index=False
        )

        orders.to_excel(
            writer,
            sheet_name='Orders',
            index=False
        )

        payments.to_excel(
            writer,
            sheet_name='Payment',
            index=False
        )

    print(f"Created : {file_path}")


def save_data_quality_report(customer_validation,order_validation,payment_validation):
    create_output_directory()
    file_path = OUTPUT_DIR / 'data_quality_report.xlsx'
    customer_report = pd.DataFrame(
        list(customer_validation.items()),
        columns=['Check','Count']
    )

    order_report = pd.DataFrame(
        list(order_validation.items()),
        columns=['Check','Count']
    )

    payment_report = pd.DataFrame(
        list(payment_validation.items()),
        columns=['Check','Count']
    )

    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        customer_report.to_excel(
            writer,
            sheet_name='Customers',
            index=False
        )
        order_report.to_excel(
            writer,
            sheet_name='Orders',
            index=False
        )
        payment_report.to_excel(
            writer,
            sheet_name='Payments',
            index=False
        )

    print(f"Created : {file_path}")


def save_customer_summary(customer_report):
    create_output_directory()
    file_path = OUTPUT_DIR/'customer_summary.xlsx'
    customer_report.to_excel(
        file_path,
        sheet_name='Customer Summary',
        index=False
    )
    print(f'Created : {file_path}')


def save_sales_report(order_report,category_report,payment_report,payment_method_report):
    create_output_directory()
    file_path = OUTPUT_DIR / "sales_report.xlsx"
    with pd.ExcelWriter(file_path,engine='openpyxl') as writer:
        order_report.to_excel(
            writer,
            sheet_name='Orders',
            index=False
        )

        payment_report.to_excel(
            writer,
            sheet_name="Payments",
            index=False
        )

        payment_method_report.to_excel(
            writer,
            sheet_name="Payment Methods",
            index=False
        )

    print(f"Created: {file_path}")

def save_sales_report(order_report,category_report,payment_report,payment_method_report):
    create_output_directory()
    file_path = OUTPUT_DIR / "sales_report.xlsx"
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:

        # order_report.to_excel(
        #     writer,
        #     sheet_name="Orders",
        #     index=False
        # )
        pd.DataFrame([order_report]).to_excel(
            writer,
            sheet_name='Orders',
            index=False
        )

        category_report.to_excel(
            writer,
            sheet_name="Categories",
            index=False
        )

        pd.DataFrame([payment_report]).to_excel(
            writer,
            sheet_name="Payments",
            index=False
        )

        payment_method_report.to_excel(
            writer,
            sheet_name="Payment Methods",
            index=False
        )

    print(f"Created: {file_path}")
