import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    value = N

    # remove duplicate salaries
    employee = employee.drop_duplicates(subset=["salary"])

    # if not enough unique salaries
    if len(employee) < N or N<1:
        return pd.DataFrame({
            f"getNthHighestSalary({value})": [None]
        })

    # repeatedly remove highest salary
    while N > 1:
        max_salary = employee["salary"].max()

        employee = employee[employee["salary"] != max_salary]

        N -= 1

    nth_salary = employee["salary"].max()

    return pd.DataFrame({
        f"getNthHighestSalary({value})": [nth_salary]
    })