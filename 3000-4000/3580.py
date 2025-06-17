import pandas as pd

def find_consistently_improving_employees(
            employees: pd.DataFrame,
            performance_reviews: pd.DataFrame) -> pd.DataFrame:

                    # We rank rating by date for each employee
    performance_reviews['rank'] = (performance_reviews.
            groupby('employee_id')['review_date'].rank(ascending=False))

                    # We filter for most recent three
    df = performance_reviews[performance_reviews['rank'] <= 3]

                    # We create a pivot table with columns for each rating 
    df = df.pivot(index="employee_id", columns = "rank", 
            values = "rating").reset_index()

                    # We filter for increasing ratings, and we compute score
    df = df.dropna()[(df[1] > df[2]) & (df[2] > df[3])]
    df['improvement_score'] = df[1] - df[3]
    
                    # We merge employee names, sort rows, and rearrange columns
    return (df.merge(employees)
            .sort_values(['improvement_score', 'name'], ascending = [0,1])
            .iloc[:,[0, 5, 4]])
