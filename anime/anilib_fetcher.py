import requests as req
import json
import pandas as pd

ANILIB = "https://api.anilibria.tv/v3/"

df = pd.DataFrame()

df_columns_names = ["id", "code", "name_ru", "name_en", "genres", "description", "episodes_count", "year"]
for i in range(len(df_columns_names)):
    df.insert(i, df_columns_names[i], [], True)

years = req.get(    
    ANILIB+"years"
).json()

for i in years:
    resp1 = req.get(
            ANILIB+"title/search",
            params={
                "year": i,
                "items_per_page": 30
            }
        ).json()
    for j in range(1, resp1['pagination']['pages']+1):
        resp = req.get(
            ANILIB+"title/search",
            params={
                "year": i,
                "items_per_page": 30,
                "page": j
            }
        ).json()
        json.dump(resp, open("anime/last_resp.json", 'w'))
        for k in range(len(resp['list'])):
            print(resp['list'][k])
            title = resp['list'][k]
            df_anime = pd.DataFrame.from_dict({"id": [title['id'], ], "code": [title['code'], ], "name_ru": [title['names']['ru'], ],
                        "name_en": [title['names']['en'], ], "genres": [", ".join(title['genres']), ],
                        "description": [title['description'], ], "episodes_count": [title['type']['episodes'], ], "year": [i, ]})
            df = pd.concat([df, df_anime])

df.to_csv("anime/anime.csv")