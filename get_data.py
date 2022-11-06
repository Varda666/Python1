import json

with open('data.json', 'r') as f:
    data = json.load(f)
keys = data.keys()
data1 = data['data']


list_tokens = []
list_wallets = []
list_telegram = []
for variable in data1:
    token = variable["_id"]["token"]
    list_tokens.append(token)
    if 'team' in variable["pair"].keys():
        wallet = variable["pair"]["team"]["wallet"]
        list_wallets.append(wallet)
    else:
        wallet = None
        list_wallets.append(wallet)
    if 'links' in variable["token"].keys():
        if "telegram" in variable["token"]['links'].keys():
            telegram = variable["token"]['links']["telegram"]
            list_telegram.append(telegram)
    else:
        telegram = None
        list_telegram.append(telegram)

list_new_tokens = []
for i in range(len(list_tokens)):
    var = list_tokens[i]
    if var in list_tokens.pop(i):
        list_tokens.insert(i, var)
        new_tokens = f"{list_tokens[i]}_{i}"
        list_new_tokens.append(new_tokens)
    else:
        list_new_tokens.append(list_tokens[i])


print(len(list_new_tokens))
print(len(set(list_new_tokens)))

print(list_wallets)
print(list_telegram)

list_price = []
for var in data1:
    if "price" in var.keys():
        price = var["price"]
        list_price.append(price)
    else:
        price = None
        list_price.append(price)

print(list_price)

list_volume24 = []
for var in data1:
    if "volume24h" in var.keys():
        volume = var["volume24h"]
        list_volume24.append(volume)
    else:
        volume = None
        list_volume24.append(volume)
print(list_volume24)

dict_all = {}
for t in list_tokens:
    dict_all['token'] = t
for w in list_wallets:
    dict_all['wallet'] = w
for tel in list_telegram:
    dict_all['telegram'] = tel
for p in list_price:
    dict_all['price'] = p
for v in list_volume24:
    dict_all['volume'] = v

    print(dict_all)




''' Достать price, volume 24h. сделать словарь'''
