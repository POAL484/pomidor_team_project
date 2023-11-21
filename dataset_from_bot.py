import pymongo
import pandas as pd

db = pymongo.MongoClient("localhost", 27017).jaba

curs = db.messages.find({})
to_df = {}
for i in curs:
    for j in i.keys():
        try: to_df[j].append(i[j])
        except KeyError: to_df[j] = [i[j]]

df = pd.DataFrame(to_df)
df.to_csv(f"datasets/out.csv")