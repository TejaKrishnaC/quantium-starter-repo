import pandas as pd 
df0=pd.read_csv("data/daily_sales_data_0.csv")
df1=pd.read_csv("data/daily_sales_data_1.csv")
df2=pd.read_csv("data/daily_sales_data_2.csv")
combined=pd.concat([df0,df1,df2],ignore_index=True)
pink_morsel=combined[combined["product"].str.lower()=="pink morsel"].copy()
pink_morsel["price"]=pink_morsel["price"].astype(str).str.replace("$","",regex=False).astype(float)
pink_morsel["quantity"]=pink_morsel["quantity"].astype(int)
pink_morsel["sales"]=pink_morsel["price"]*pink_morsel["quantity"]
final=pink_morsel[["sales","date","region"]]
final.to_csv("formatted.csv",index=False)
print("Success")