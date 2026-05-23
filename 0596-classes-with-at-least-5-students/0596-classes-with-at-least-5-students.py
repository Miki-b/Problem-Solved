import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses.groupby('class')['student'].count()
    return result[result>=5].reset_index()[['class']]
    