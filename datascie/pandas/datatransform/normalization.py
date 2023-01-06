import pandas as pd
import numpy as np
from sklearn import preprocessing
import scipy.stats as s
data={
    "co1":[1,2,3,4],
    "co2":[2,3,4,3],
    "co3":[1,3,4,33],
    "co4":[11,2,32,4],
    "co5":[7,-2,3,4],
    "co6":[6,32,8,4]
}
df=pd.DataFrame(data)
print(df.describe())
print("\n\n")

data_normalized=preprocessing.normalize(df)
print(data_normalized.round(2))