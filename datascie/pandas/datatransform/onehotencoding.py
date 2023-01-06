import pandas as pd
import numpy as np
from sklearn import preprocessing
import scipy.stats as s
data={
    "co1":[1,2,3,4],
    "co2":[2,3,4,3],
    "co3":[1,3,4,33],
    "co4":[11,2,32,4],
    "text_col":['A','B','C','B']
}
df=pd.DataFrame(data)
ohenc=preprocessing.OneHotEncoder(handle_unknown='ignore')
newdf=pd.DataFrame(ohenc.fit_transform(df[["text_col"]]).toarray())
df=df.join(newdf)
print(df)