import pandas as pd
import regex as re
from collections import OrderedDict
import math


import sys
import os

if sys.argv[1]!='Haryana_State_Dealer_Tax_Monitor_Sheets':
	cmd = 'find Nextcloud -maxdepth 4 -mindepth 3 -type f \\( -iname \"*.xlsx\" -o -iname \"*.xls\" \\) > path.txt'
else:
	cmd = 'find Nextcloud -maxdepth 3 -mindepth 2 -type f \\( -iname \"*.xlsx\" -o -iname \"*.xls\" \\) > path.txt'

os.system(cmd)

pd.set_option('display.max_rows', 500)

file_list = [x.strip() for x in open("path.txt").readlines()]

final_list = []



def filter_1(df):
    # companies name
    dict_company = OrderedDict()
    for i in range(df.shape[0]):
        a = str(df.iloc[i, 0])
        if a != 'nan' and a != 'Tin No.':
            if not bool(re.match('([0-9]){10,12}([a-zA-Z]){1}|([0-9]){6}\/([A-Z]){1}\/([0-9]){4}', a)):
                dict_company.update({a: i})
    return dict_company


def filter_2(df, dict_company):
    li_total_places = []
    li_total_values = []

    for j in range(df.shape[0]):
        a = str(df.iloc[j, 2])
        if bool(re.match('([Gg][Rr][Aa][Nn][Dd] )?[Tt][Oo][Tt][Aa][Ll]', a)) or a == 'current total':
            li_total_places.append(j)
            temp_li = []
            for z in range(4, 14):
                temp_li.append(df.iloc[j, z])
            li_total_values.append(temp_li)
        if a == 'Payment for the Month' or a == 'Amount reduced' or a == 'Addition During the Month':
            dict_company.update({a: j})
    return li_total_places, li_total_values, dict_company


def function(file_list):
    raw_data = pd.read_excel(file_list[0])
    df_alpha = pd.DataFrame(raw_data)


    raw_data = pd.read_excel(file_list[1])
    df_beta = pd.DataFrame(raw_data)


    dict_company_alpha = filter_1(df_alpha)
    dict_company_beta = filter_1(df_beta)

    li_total_places_alpha, li_total_values_alpha, dict_company_alpha = filter_2(df_alpha, dict_company_alpha)
    li_total_places_beta, li_total_values_beta, dict_company_beta = filter_2(df_beta, dict_company_beta)

    for key in dict_company_alpha:
        if key in dict_company_beta:
            if "Due" in str(key):
                #df_alpha_new = df_alpha.iloc[dict_company_alpha[key]:]
                #df_beta_new = df_beta.iloc[dict_company_alpha[key]:]
                break

            else:
                df_alpha_new = df_alpha.iloc[
                               dict_company_alpha[key]:li_total_places_alpha[dict_company_alpha.keys().index(key)]]
                df_beta_new = df_beta.iloc[
                              dict_company_beta[key] + 1:li_total_places_beta[dict_company_beta.keys().index(key)] + 1]

            final_list.append(df_alpha_new)
            final_list.append(df_beta_new)
    if final_list:
        result = pd.concat(final_list, ignore_index=True)
        writer = pd.ExcelWriter('Nextcloud/' + sys.argv[1] + '/final.xlsx')
        df_gamma = pd.DataFrame(result)
        df_gamma.to_excel(writer, 'Feb. sheet 8')
        writer.save()


for i in range(len(file_list) - 1):
    if i == 0:
        function([file_list[i], file_list[i + 1]])
    else:
        final_list = []
        function(['Nextcloud/' + sys.argv[1] + '/final.xlsx',file_list[i + 1]])

data = pd.read_excel('Nextcloud/' + sys.argv[1] + '/final.xlsx')
df_gamma = pd.DataFrame(data)


list_of_unwanted_data = []
for i in range(df_gamma.shape[0]):
    a = str(df_gamma.iloc[i, 0])
    if a != 'nan':
        if a == 'Tin No.':
            list_of_unwanted_data.append(i)

for j in list_of_unwanted_data:
    df_gamma = df_gamma.drop(j, axis = 0)

df_gamma = df_gamma.rename(columns={'29.02.2016':'Tin No.', 'Unnamed: 1':'DBA Entry No /Page No.', 'Unnamed: 2':'Name of the dealer', 'Unnamed: 3':'Period', 'Unnamed: 4':'VAT Tax', 'Unnamed: 5':'Int 30(2)&(3)'
                                    ,'Unnamed: 6':'Penalty', 'Unnamed: 7':'NO', 'Unnamed: 8':'Total Amount (VAT)', 'Unnamed: 9':'CST Tax',
                                    'Unnamed: 10':'Int30(2)&(3)', 'Unnamed: 11':'penalty', 'Unnamed: 12':'NO', 'Unnamed: 13':'Total Amount (CST)','Unnamed: 14':'remark' })



a = filter_2(df_gamma,filter_1(df_gamma))
print a[2]
print a[0]
wow = list(df_gamma.columns.values)


for y in range(4,13):
    sum = 0
    l = 0
    for keys in a[2]:
        for i in range(a[2][keys] + 1, a[0][l]):
            if not math.isnan(float(df_gamma.iloc[i, y])):
                sum += float(df_gamma.iloc[i, y])
        print sum

        df_gamma.ix[i + 4, wow[y]] = sum

        #y, a[0][l]
        sum = 0
        l += 1



#print df_g amma_new



writer = pd.ExcelWriter('Nextcloud/' + sys.argv[1] + '/final.xlsx')
df_gamma.to_excel(writer, 'Feb. sheet 8')
df_gamma.to_excel(writer, 'VAT')
writer.save()
