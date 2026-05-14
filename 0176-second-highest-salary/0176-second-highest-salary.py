import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
     # remove duplicate salaries
    employee = employee.drop_duplicates(subset=["salary"])

    # remove highest salary
    max_salary = employee["salary"].max()
    employee = employee[employee["salary"] != max_salary]

    # second highest
    second_salary = employee["salary"].max()

    return pd.DataFrame({
        "SecondHighestSalary": [second_salary]
    })