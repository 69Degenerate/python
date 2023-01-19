import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('db.sqlite3') 
c = conn.cursor()
                 
c.execute('''SELECT * FROM api_std''')

df = pd.DataFrame(c.fetchall(), columns = ['id','n','r','e','d'])
print (df.info())

df.groupby('sport')['players'].sum().plot(kind="pie")