import pandas as pd
import sys


df = pd.read_csv('./pythonplag/plag.csv')
target = '110034561洪聖博'
if len(sys.argv) == 2: target = sys.argv[1]

df = df.loc[df['student1'] == target, ['student2', 'similarity']].sort_values(by='similarity', ascending=False)
df = df[df['similarity'] > 80]
print(df)