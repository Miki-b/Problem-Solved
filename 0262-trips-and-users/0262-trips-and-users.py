import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:

    users = users[users.banned == 'No']                         # <-- 1)
    trips = (trips[trips.request_at
                        .between('2013-10-01','2013-10-03')]
                        .rename(columns = {'request_at': 'Day'}))

    trips['cancelled'] = trips.status.str.startswith('can')     # <-- 2)

    return (trips.loc[trips.client_id.isin(users.users_id)]     # <-- 3)
                 .loc[trips.driver_id.isin(users.users_id)]
                 .groupby('Day')['cancelled']
                 .mean().round(2)
                 .reset_index(name = 'Cancellation Rate'))