import json
import requests
from pprint import pprint

print(f'Код ИФНС:')
ifns = int(input())
print(f'Муниципальное образование:')
oktmmf = int(input())

parameters = 'payeeDetails'
#40913000

data = {"ifns": ifns,
        'oktmmf': oktmmf,
        'c': 'next',
        'step': '1'}
url = 'https://service.nalog.ru/addrno.do/addrno-proc.json'
response = requests.post(url, data=data)
json_data = json.loads(response.text)

# for i in json_data['payeeDetails']:
#     print(type(i)) # тип данных str из-за запроса

# pprint(json_data)
print(f"Получатель платежа: {json_data['payeeDetails']['payeeName']}")
print(f"ИНН получателя: {json_data['payeeDetails']['payeeInn']}")
print(f"КПП получателя: {json_data['payeeDetails']['payeeKpp']}")
print(f"Банк получателя: {json_data['payeeDetails']['bankName']}")
print(f"БИК: {json_data['payeeDetails']['bankBic']}")
print(f"Корр. счет: {json_data['payeeDetails']['correspAcc']}")
print(f"Счёт получателя: {json_data['payeeDetails']['payeeAcc']}")

#--------первоначальный вариант key : value
# for key, value in json_data.items():
#     for keys, values in value:
#         print(values)
    # if parameters in key:
    #     a = value.get('payeeName')
    #     b = value.get('payeeInn')
    #     c = value.get('payeeKpp')
    #     d = value.get('bankName')
    #     e = value.get('bankBic')
    #     f = value.get('correspAcc')
    #     g = value.get('payeeAcc')
    #     print(value)
    #     print(f'Получатель платежа: {a}')
    #     print(f'ИНН получателя: {b}')
    #     print(f'КПП получателя: {c}')
    #     print(f'Банк получателя: {d}')
    #     print(f'Счёт получателя: {g}')
