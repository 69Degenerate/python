import pandas as pd
import numpy as np
from sklearn import preprocessing
import rescaling
import scipy.stats as s
train_df=rescaling.scaled
print(train_df)
# print(s.tmean(train_df).round(2))
df_scaled=preprocessing.scale(train_df)
df_scaled.mean(axis=0)
df_scaled.std(axis=0)
print("\n\n")

print(round(df_scaled.std(),2))
