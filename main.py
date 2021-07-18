import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


Total_list=[]
for element in contacts_list:
    i=re.split(r'\W+', str(element[0:3]))
    i_1=i.pop(0)
    i_2=i.pop()
    if len(i)<3:
       i.append('')
    element[0]=i[0]
    element[1]=i[1]
    element[2]=i[2]


    phone_pattern = re.compile(
        r"([\+7|8)]+)\s*\(?(\d{3})\)?[\s|-]*(\d{3})[\s|-]*(\d{2})[\s|-]"
        r"*(\d{2})\s*(\(?(\w+\.)\s*(\d+)\)?)*"
    )
    result = phone_pattern.sub(r"+7(\2)\3-\4-\5 \7 \8", element[5]).strip()
    element[5]=result


    Total_list.append(element)





with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(Total_list)

