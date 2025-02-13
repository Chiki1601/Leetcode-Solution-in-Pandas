import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    def is_invalid(ip):
        arr = ip.split(".")
        if len(arr) != 4:
            return True
        for b in arr:
            if b.startswith("0") or int(b)>255:
                return True
        return False
            
    df = logs.groupby('ip').size().reset_index(name='invalid_count')
    df = df[df['ip'].apply(is_invalid)]
    return df.sort_values(['invalid_count','ip'],ascending=[False,False])
