import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    return (
        user_content
        .eval('converted_text = content_text.str.title()')
        .rename(columns={'content_text': 'original_text'})
    )
