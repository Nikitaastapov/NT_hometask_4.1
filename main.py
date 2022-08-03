import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)
result=[]
pattern_1 = r'^(\w+)(\s|,)(\w+)(\s|,)(\w+)?,{1,3}(\w+)?,(.+)?,(.+)?,(.+)?'
pattern_2 = r'(\+7|8)(\s)?(\()?(\d{1,3})(\))?(\s|-)?(\d{3})(\s|-)?(\d{2})(\s|-)?(\d{2})(\s)?(\()?(доб)?(\.)?(\s)?(\d+)?(\))?'
result.append(contacts_list[0])
result.append(contacts_list[1])



def CheckName(list_res):
    Check_lastname = list_res[0]
    Check_firstname = list_res[1]
    ret_res = 'not'
    for i in result[1:]:
        if i[0] == Check_lastname and i[1] == Check_firstname:
            ret_res = 'yes'
    return ret_res

def AddDubs(list_res, result):
    Check_lastname = list_res[0]
    Check_firstname = list_res[1]
    numb=2
    for i in result[1:]:
        if i[0] == Check_lastname and i[1] == Check_firstname:
            while numb <=6:
                if len(i[numb])>0 or (len(i[numb])==0 and len(list_res[numb])==0):
                    pass
                else:
                    i[numb]=list_res[numb]
                numb+=1
    return result
        

for i in contacts_list[2:]:
    item = ','.join(i)
    item = res=re.sub(pattern_1, r'\1,\3,\5,\6,\7,\8,\9', item)
    res=re.sub(pattern_2, r'+7(\4) \7-\9-\g<11> \g<14>\g<15> \g<17>', item)
    print('item', item)
    res = res.split(',')
    print('res', res)
    
    if CheckName(res)=='not':
        result.append(res)
    else:
        # print(res)
        AddDubs(res,result)
  
# pprint(result)
    
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(result)