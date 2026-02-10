import pandas as pd


def find_behaviorally_stable_users(activity: pd.DataFrame) -> pd.DataFrame:

    activity.action_date = pd.to_datetime(activity.action_date)
    min_date = activity.action_date.min()
    activity['streak'] = activity.index - (activity.action_date - min_date).dt.days

    df = activity.groupby(['user_id', 'action'], as_index = 0).agg(
               streak_length = ('streak'     , 'size'),
                  start_date = ('action_date', 'min' ),
                    end_date = ('action_date', 'max' ))

    df['user_max'] = df.groupby('user_id')['streak_length'].transform('max')

    return (df.loc[(df.streak_length == df.user_max) & (df.streak_length >= 5)]
              .sort_values(['streak_length', 'user_id'], ascending = [0, 1])
              .iloc[:, :5])
    
