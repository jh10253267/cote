from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    date_format = "%Y.%m.%d"
    today = datetime.strptime(today, date_format)
    for i in terms:
        temp = i.split()
        terms_dict[temp[0]] = int(temp[1])
    
    for i, data in enumerate(privacies):
        arr = data.split()
        date_obj = datetime.strptime(arr[0], date_format)
        result = date_obj + relativedelta(months=terms_dict[arr[1]])
        if result.day == 1:
            result -= timedelta(days=3)
        else:
            result -= timedelta(days=1)
        if today > result:
            answer.append(i+1)
    return answer