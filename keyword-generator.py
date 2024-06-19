import pandas as pd

products = ["sofas", "convertible sofas", "love seats", "recliners", "sofa beds"]
keywords = ["buy", "prices", "budget", "affordable", "discount", "cheap", "budget friendly", "on sale", "low cost", "best price", "with discount"]

def generate_keywords(products, keywords, match_type='Exact', campaign='SEM_Sofas'):
    col_names = ['Campaign', 'Ad Group', 'Keyword', 'Criterion Type']
    campaign_keywords = []
    
    for product in products:
        for word in keywords:
            keyword_d1 = product.lower() + ' ' + word
            keyword_d2 =  word + ' ' + product.lower()
            row_d1 = [campaign, # campaign name
                   product, # ad group name
                   keyword_d1, # search keyword
                   match_type] # keyword match type
            row_d2 = [campaign, # campaign name
                   product, # ad group name
                   keyword_d2, # search keyword
                   match_type] # keyword match type
            campaign_keywords.append(row_d1)
            campaign_keywords.append(row_d2)
                
    return pd.DataFrame.from_records(campaign_keywords, columns=col_names)

keywords_df = generate_keywords(products, keywords)
keywords_df.to_csv('keywords.csv', index=False)
