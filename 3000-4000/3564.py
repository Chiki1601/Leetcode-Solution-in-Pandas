import pandas as pd

def seasonal_sales_analysis(products: pd.DataFrame, 
                            sales: pd.DataFrame) -> pd.DataFrame:

                    # Determine sales season in sales dataframe   
    seasons = ['Winter', 'Spring', 'Summer', 'Fall']
    map_season = lambda x: seasons[x.month %12 //3]
    sales['season'] = sales.sale_date.apply(map_season)

                    # Determine revenue in sales dataframe
    sales['revenue'] = sales.quantity * sales.price

                    # Merge products and sales dataframes on product_id
    return (products.merge(sales)

                    # Determine sums over season and category
                    .groupby(['season', 'category'])
                    .agg({'quantity': 'sum', 'revenue': 'sum'})
                    .reset_index()

                    # Sort by the given tie-breaking criteria
                    .sort_values(['season','quantity','revenue',],
                                            ascending = [1, 0, 0])
                    # Take winner per season
                    .groupby('season').first().reset_index()

                    # Do the housekeeping
                    .rename(columns = {'quantity': 'total_quantity',
                                       'revenue': 'total_revenue'})
           )
