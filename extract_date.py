import re

# 4 type of file name
# date-num, date, DSC_, else
# However because the only thing we can extract is date
# so just check whether you can extract date or not

# test = ['20000830-123', '20020709', 'DSC_2342523', 'floating number']

def extract_date(s: str) -> str:
    
    if s.find('-') != -1:
        s = s[:s.find('-')]
    
    if s.isnumeric() and len(s)==8:
        return s[:4] + '-' + s[4:6] + '-' + s[6:]
    
    return 'nan'

# for cases in test:
#     print(extract_date(cases))