import json
import pandas as pd

FILES = ['English_positions.json', 'Portuguese_positions.json', 'German_positions.json']
# FILES = ['English_positions.json']


for file in FILES:
    f = open(file)
    data = json.load(f)
    f.close()
    table = []
    header = list(data.keys())
    columns = list(data[header[0]].keys())
    for col in columns:
        aux = []
        for head in header:
            aux.append(data[head][col]['sorted position'])
        table.append(aux)

    df = pd.DataFrame(data=table, index=columns)
    df.columns = header 
    df.to_excel(file.split('.')[0] +".xlsx")