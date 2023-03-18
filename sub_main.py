import requests

# APIから現在のBitcoin価格を取得する
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
price = data['bpi']['JPY']['rate_float']

# 結果を出力する
print('現在のBitcoin価格は、{:,.0f}円です。'.format(price))
