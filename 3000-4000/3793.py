import pandas as pd

def find_users_with_high_tokens(prompts: pd.DataFrame) -> pd.DataFrame:

    df = prompts.groupby('user_id')['tokens'].agg(
            prompt_count = 'count',
              max_tokens = 'max',
              avg_tokens = 'mean' ).reset_index()

    return (df.loc[df.prompt_count >= 3]
              .loc[df.max_tokens > df.avg_tokens]
              .sort_values(['avg_tokens', 'user_id'], ascending  = [0,1])
              .round(2)).iloc[:,[0,1,3]]
    
