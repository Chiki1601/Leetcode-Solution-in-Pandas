import pandas as pd

def find_category_recommendation_pairs(product_purchases: pd.DataFrame,
                            product_info: pd.DataFrame) -> pd.DataFrame:

                # Merge the dataframes and group each category's users in a set
    df = (pd.merge(product_purchases, product_info, on = 'product_id')
            .groupby('category')['user_id'].agg(lambda x: set(x)).reset_index())

                # Merge df with itself, then filter for category1 < category2
    df = df.merge(df, how = 'cross', suffixes = ['1', '2'])
    df = df[df.category1 < df.category2]

                # Find the counts of the common users for each pair
    df['customer_count'] = df.apply(lambda x: len(x.user_id1 & x.user_id2), axis=1)

                # Filter for at least 3 common users, then sort and format as required
    return (df[df.customer_count >= 3]
                 .sort_values(['customer_count', 'category1', 'category2'],
                  ascending = [0,1,1])).iloc[:,[0,2,4]]
