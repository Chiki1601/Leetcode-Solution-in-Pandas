import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users.query(
        expr = "email.str.match(r'^\w*@[a-zA-Z].*\.com$')"
    ).sort_values(
        by = "user_id"
    )
