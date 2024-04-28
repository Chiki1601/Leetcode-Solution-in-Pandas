# addejans

import pandas as pd

def server_utilization_time(servers: pd.DataFrame) -> pd.DataFrame:
    # Ensure the status_time is a datetime type
    servers['status_time'] = pd.to_datetime(servers['status_time'])
    
    # Sort the DataFrame by server_id and status_time
    servers_sorted = servers.sort_values(by=['server_id', 'status_time'])

    # Assign 'stop_time' as the 'status_time' of the next row within each 'server_id'
    servers_sorted['stop_time'] = servers_sorted.groupby('server_id')['status_time'].shift(-1)

    # Filter rows where session_status is 'start' and stop_time is not null
    running_time = servers_sorted[(servers_sorted['session_status'] == 'start') & (servers_sorted['stop_time'].notna())]

    # Calculate the total seconds between start and stop times
    running_time['uptime_seconds'] = (running_time['stop_time'] - running_time['status_time']).dt.total_seconds()

    # Calculate total uptime in full days
    total_uptime_days = running_time['uptime_seconds'].sum() / 86400
    total_uptime_days = int(total_uptime_days)  # Convert to integer to simulate the FLOOR function

    # Return the result as a DataFrame
    return pd.DataFrame({'total_uptime_days': [total_uptime_days]})
