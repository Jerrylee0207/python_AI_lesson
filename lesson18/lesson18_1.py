import pandas as pd

df = pd.read_csv("各鄉鎮市區人口密度.csv")
df1 = df.rename(columns={"statistic_yyy":"統計年",
                   "site_id":"區域別",
                   "people_total":"年底人口數",
                   "area":"土地面積",
                   "population_density":"人口密度"
                   })
print(df1);

df.columns = ["統計年","區域別","年底人口數","土地面積","人口密度"]
df2 = df.drop(["統計年"],axis=1);
df3 = df2.dropna(axis=0);
df4 = df3.drop(index=0);

def string_to_int(value:str):
    try:
        v = int(value)
        return v
    except Exception:
        return 0
    
df4["年底人口數"] = df4["年底人口數"].map(string_to_int)
df4["人口密度"] = df4["人口密度"].apply(string_to_int)

df4['土地面積'] = df4['土地面積'].astype(float)

def split_words(v:str):
    if len(v) == 6:
        return v[:3]
    else:
        return v

df4["縣市"] = df4['區域別'].map(split_words)
def split_area(v:str):
    if len(v) == 6:
        return v[-3:]
    else:
        return v
df4['區域別'] = df4['區域別'].map(split_area)
df5 = df4.reindex(columns=["區域別","縣市","年底人口數","土地面積","人口密度"])
df6 = df5.set_index('區域別')
df6.to_excel('各鄉鎮市區人口密度.xlsx',index=True)