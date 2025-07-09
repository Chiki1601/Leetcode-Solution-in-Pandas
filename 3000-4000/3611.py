import pandas as pd

def find_overbooked_employees(employees: pd.DataFrame, 
                              meetings: pd.DataFrame) -> pd.DataFrame:

                    # We assign a year and an integer week to each row
    meetings['year'] = meetings.meeting_date.dt.year
    meetings['week'] = meetings.meeting_date.dt.isocalendar().week

                    # We determine hrs/week
    df = (meetings.groupby(['employee_id','year', 'week'])
                  .sum('duration_hours').reset_index()
                  .rename(columns = {'duration_hours': 'meeting_heavy_weeks'}))

                    # We filter for heavy weeks, and count the heavy weeks per employee
    df = (df[df.meeting_heavy_weeks > 20.0]
            .groupby(['employee_id']).count()
            .merge(employees, on = 'employee_id'))

                    # We filter employees for at least two heavy weeks, and we 
                    # and we sort rows and rearrange columns
    return (df[df.meeting_heavy_weeks > 1]
                 .sort_values(['meeting_heavy_weeks', 'employee_name'], ascending = [0,1])
                 .iloc[:,[0,5,6,4]])
