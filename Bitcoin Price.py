import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
from bs4 import BeautifulSoup

root= tk.Tk() 

xlist2 = []
ylist2 = []



myapi = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
myapi_json  = myapi.json()
B = int(myapi_json["bpi"]["USD"]["rate"].split(".")[0].replace("," , ""))
xlist2.append(B)


page = requests.get("https://www.tgju.org/chart/price_dollar_rl")
soup = BeautifulSoup(page.content, 'html.parser')
D = int(soup.find("span", itemprop="price").get_text().replace("," , ""))
ylist2.append(D)



data2 = {'Bitcoin \$':xlist2 ,
         'Bitcoin_Dolar_Rial_Rate': ylist2
        }
df2 = DataFrame(data2,columns=['Bitcoin \$','Bitcoin_Dolar_Rial_Rate'])
















figure2 = plt.Figure(figsize=(15,5), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['Bitcoin \$','Bitcoin_Dolar_Rial_Rate']].groupby('Bitcoin \$').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('Bitcoin price : ' +  str(xlist2[0]) + '\$ VS Dolar price : ' + str(ylist2[0])+ 'Rials')
ax2.set_title('Dolar price : ' + str(ylist2[0])+ ' Rials    VS    Bitcoin price : ' +  str(xlist2[0]) + ' \$')






 

root.mainloop()

