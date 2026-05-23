import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    max= orders.groupby('customer_number')['order_number'].count().max()
    result= orders.groupby('customer_number')['order_number'].count()
    print(result)
    return result[result==max].reset_index()[['customer_number']]
    