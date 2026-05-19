import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    manager=employee[['id','salary']].rename(columns={'id':'managerId','salary':'manag_salary'})
    result=employee.merge(manager,on='managerId',how='inner').rename(columns={'name':'Employee'})
    result1=result.loc[result['salary']>result['manag_salary']][['Employee']]
    return result1