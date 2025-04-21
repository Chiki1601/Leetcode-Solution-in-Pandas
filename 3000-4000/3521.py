import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, 
                                      product_info: pd.DataFrame) -> pd.DataFrame:

    # 1) Merge to determine pairs
    df = pd.merge(product_purchases, product_purchases, on = 'user_id')

    # 2) Use Counter to count pairs and filter for recommendations
    rows = Counter(zip(df.product_id_x, df.product_id_y)).items()
    data = [(p1,p2, cnt) for (p1, p2), cnt in rows if p1 < p2 and cnt >= 3]
    
    # 3) Create DataFrame for solution and cleanup
    return (pd.DataFrame(data, columns = ["product1_id", "product2_id",  "customer_count"])
              .merge(product_info, left_on = 'product1_id', right_on ='product_id' )
              .merge(product_info, left_on = 'product2_id', right_on ='product_id' )
              .rename(columns = {'category_x':'product1_category', 'category_y':'product2_category'})
              .sort_values(['customer_count', 'product1_id', 'product2_id'], ascending = [0,1,1])
              .iloc[:, [0, 1, 4, 7, 2]])
