import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(students) # whole dataframe
    df = df[df['student_id']==101] # dataframe with student_id==101
    df = df[['name','age']] # selected columns from dataframe with student_id=101
    return df
    
