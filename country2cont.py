# group countries into continents in a separate column
import pycountry_convert as pc
import country_converter as coco
import pandas as pd
df=pd.read_csv("../covid_stats/case_counts.csv")
cc=coco.CountryConverter()
# for each country in continent_name column, convert each country into continent it belongs to
def get_continent(country_name):
    try:
        country_code3=cc.convert(country_name) # convert country name to country code ISO 3 (3 letter code)
        country_code2=coco.convert(names=country_code3, to='ISO2') # convert 3 letter code to 2 letter code
        country_continent_code=pc.country_alpha2_to_continent_code(country_code2)
        country_continent_name=pc.convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name
    except:
        return 'not found'

df['continent_name']=df['country_region'].apply(lambda x: get_continent(x))
df.loc[df.country_region=='Western Sahara', 'continent_name']="Africa" # change the 'not found' result for sahara
df.loc[df.country_region=='Holy See', 'continent_name']="Europe"
df.loc[df.country_region=='Timor-Leste', 'continent_name']="Asia"
df.to_csv(r"C:\Users\thous\OneDrive\Desktop\covid_stats\case_counts.csv", encoding='utf-8', index=False)
