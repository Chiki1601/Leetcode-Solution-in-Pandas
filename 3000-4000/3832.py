import pandas as pd

def find_behaviorally_stable_users(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby(['user_id','action']).agg(streak_length=('action','count'),start_date=('action_date','min'),end_date=('action_date','max')).reset_index()
    return df[df['streak_length'] >= 5].sort_values(by=['streak_length','user_id'],ascending=[False,True])
