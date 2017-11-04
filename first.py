import pandas as pd
import regex as re
import numpy as np
from collections import OrderedDict

pd.set_option('display.max_rows', 500)
file_list = ['/Users/akarshan/Desktop/LTU_4_MUMBAI.xlsx', '/Users/akarshan/Desktop/Mumbai_2.xlsx']
dfbeta = pd.DataFrame()
for path in file_list:
    raw_data = pd.read_excel(path)
    df = pd.DataFrame(raw_data)


    # row count
    count_row=df.shape[0]

    dict_company = OrderedDict()
    for i in range(count_row):
        a = str(df.iloc[i, 0])
        if a != 'nan' and a != 'Tin No.':
            if not bool(re.match('([0-9]){10,12}([a-zA-Z]){1}|([0-9]){6}\/([A-Z]){1}\/([0-9]){4}', a)):
                dict_company.update({a: [i,0]})
    print dict_company

    li = []
    for j in range(count_row):
        a = str(df.iloc[j, 2])
        if bool(re.match('([Gg][Rr][Aa][Nn][Dd] )?[Tt][Oo][Tt][Aa][Ll]', a)):
            li.append(j)
    print li

    dfalpha = df.iloc[dict_company.values()[0][0]:li[0]]
    #print dfalpha
    frames = [dfbeta, dfalpha]
    dfbeta = dfalpha

result = pd.concat(frames)
print result
writer = pd.ExcelWriter('/Users/akarshan/Desktop/finally.xlsx')
df3 = pd.DataFrame(result)
df3.to_excel(writer,'Sheet')
writer.save()