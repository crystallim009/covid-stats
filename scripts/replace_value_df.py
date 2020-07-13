import pandas as pd

df=pd.read_csv("../covid_stats/case_counts.csv")
df["continent_name"]=df["continent_name"].str.replace("not found", "Others (Cruise ship)")
df.to_csv(r"C:\Users\thous\OneDrive\Desktop\covid_stats\case_counts2.csv", encoding='utf-8', index=False)
