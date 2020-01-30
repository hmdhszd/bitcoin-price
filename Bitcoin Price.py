import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
from bs4 import BeautifulSoup

root= tk.Tk() 

xlist2 = [0]
ylist2 = [0]



people = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
people_json  = people.json()
B = int(people_json["bpi"]["USD"]["rate"].split(".")[0].replace("," , ""))
xlist2.append(B)


page = requests.get("https://www.tgju.org/chart/price_dollar_rl")
soup = BeautifulSoup(page.content, 'html.parser')
D = int(soup.find("span", itemprop="price").get_text().replace("," , ""))
bitcoinrial = B * D
ylist2.append(bitcoinrial)
    


data2 = {'Year':xlist2 ,
         'Unemployment_Rate': ylist2
        }
df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])



















figure2 = plt.Figure(figsize=(15,5), dpi=200)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')


 

root.mainloop()