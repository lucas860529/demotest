import os
import pandas as pd
import re

try:
    with open("./plag.txt", 'r') as f:
        rule = re.compile(r'^Comparing\s(.*)_[0-9]{6}_assignsubmission_file.+-(.*)_[0-9]{6}_assignsubmission_file.*:\s([0-9]+\.[0-9]+)')
        rows = []
        for l in f.readlines():
            g = re.findall(rule, l)
            if len(g) == 1: rows.append(g[0])
        df = pd.DataFrame(rows, columns=['student1', 'student2', 'similarity'])
        df.to_csv('plag.csv')
        
except FileNotFoundError:
    print('generating plag.txt ...')
    os.system("java -jar jplag-2.12.1-SNAPSHOT-jar-with-dependencies.jar -l python3 ./students >> plag.txt")
    print('Finish! please restart this program')
        