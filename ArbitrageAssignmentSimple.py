import pandas as pd
from matplotlib import pyplot as plt
import requests


# define a pair
fsym = "BTC"
tsym = "USD"
#  https://min-api.cryptocompare.com/data/top/exchanges/full?fsym=ETH&amp;tsym;=USD
url = "https://min-api.cryptocompare.com/data/top/exchanges/full?fsym=" + \
      fsym + "&tsym=" + tsym

data = pd.read_json(url)
#print(data)


#to convert to pandas data frame
df = pd.DataFrame(data)


#print(df.Data.Exchanges)
ExchangeData = pd.DataFrame(df.Data.Exchanges)

#print(ExchangeData)
price = ExchangeData.loc[:,'PRICE']
print(type(price))
volume = ExchangeData.loc[:,'VOLUME24HOUR']
exchange = ExchangeData.loc[:,'MARKET']


for i, txt in enumerate(exchange):
    plt.annotate(txt, (volume[i],price[i]))

plt.plot(volume, price, 'ro')
plt.show()




#volume = pd.DataFrame(df.Data.Exchanges)

#print(volume)


#to print data frame
#print(df)

# to print first 5 elements and last 5 elements
#print(df.head)
#print(df.tail)

#to set index
#df = df.set_index('Day')

#df = df.set_index(1)