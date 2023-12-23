import matplotlib.pyplot as plt
from tkinter import *
import requests
import json
import os

os.system('cls')
#############################
def red_green(amount):
    if amount >= 0:
        return 'green'
    else:
        return 'red'


root = Tk()

root.title('Crypto Currency Portfolio')

header = ['Name', 'Rank', 'Current Price', 
          'Price Paid', 'Profit/Loss Per', '1-Hour Change', 
          '24-HHour Change', '7-Day Change', 'Current Value', 'Profit/Loss Total']

header_name = Label(root, text=header[0], bg='White', font='Verdana 8 bold')
header_name.grid(row=0, column=1, sticky=N+S+E+W)

header_rank = Label(root, text=header[1], bg='Silver', font='Verdana 8 bold')
header_rank.grid(row=0, column=2, sticky=N+S+E+W)

header_current_price = Label(root, text=header[2], bg='White', font='Verdana 8 bold')
header_current_price.grid(row=0, column=3, sticky=N+S+E+W)

header_price_paid = Label(root, text=header[3], bg='Silver', font='Verdana 8 bold')
header_price_paid.grid(row=0, column=4, sticky=N+S+E+W)

header_pl_per = Label(root, text=header[4], bg='White', font='Verdana 8 bold')
header_pl_per.grid(row=0, column=5, sticky=N+S+E+W)

header_1_hour_change = Label(root, text=header[5], bg='Silver', font='Verdana 8 bold')
header_1_hour_change.grid(row=0, column=6, sticky=N+S+E+W)

header_24_hour_change = Label(root, text=header[6], bg='White', font='Verdana 8 bold')
header_24_hour_change.grid(row=0, column=7, sticky=N+S+E+W)

header_7_day_change = Label(root, text=header[7], bg='Silver', font='Verdana 8 bold')
header_7_day_change.grid(row=0, column=8, sticky=N+S+E+W)

header_current_value = Label(root, text=header[8], bg='White', font='Verdana 8 bold')
header_current_value.grid(row=0, column=9, sticky=N+S+E+W)

header_pl_total = Label(root, text=header[9], bg='Silver', font='Verdana 8 bold')
header_pl_total.grid(row=0, column=10, sticky=N+S+E+W)

def lookup():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '100',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'f24be374-c2ce-4f13-b9c6-cfd4c6652e6b',
    }

    try:
        response = requests.get(url, params=parameters, headers=headers)
        data = json.loads(response.content)

        my_portfolio = [
            {
                'sym': 'BTC',
                'amount_owned': 2,
                'price_paid_per': 2000
            },
            {
                'sym': 'ETH',
                'amount_owned': 6,
                'price_paid_per': 300
            },
            {
                'sym': 'LUNA',
                'amount_owned': 11,
                'price_paid_per': 120
            },
            {
                'sym': 'SOL',
                'amount_owned': 10,
                'price_paid_per': 120
            },
            {
                'sym': 'BNB',
                'amount_owned': 3,
                'price_paid_per': 120
            },
        ]
        
        portfolio_profit_loss = 0
        total_current_value = 0
        row_count = 1
        pie = []
        pie_size = []
        for x in data['data']:
            for coin in my_portfolio:
                if coin['sym'] == x['symbol']:
                    # profit calculation
                    total_paid = float(coin['amount_owned']) * float(coin['price_paid_per'])
                    current_value = float(coin['amount_owned']) * float(x['quote']['USD']['price'])
                    profit_loss = current_value - total_paid
                    portfolio_profit_loss += profit_loss
                    profit_loss_per_coin = (float(x['quote']['USD']['price']) * float(coin['amount_owned'])) - total_paid
                    total_current_value += current_value
                    pie.append(x['name'])
                    pie_size.append(coin['amount_owned'])

                    #print(x['name'])
                    #print(' Current Price: ${0:.2f}'.format(float(x['quote']['USD']['price'])))
                    #print(' Profit/Loss Per Coin: ${0:.2f}'.format(float(profit_loss_per_coin)))
                    #print(' Rank: {0:.0f}'.format(float(x['cmc_rank'])))
                    #print(' Total Paid: ${0:.2f}'.format(float(total_paid)))
                    #print(' Current Value: ${0:.2f}'.format(float(current_value)))
                    #print(' Profit/Loss: ${0:.2f}'.format(float(profit_loss)))
                    #print('-----------------------------------------')
                    
                    name = Label(root, text=x['name'], bg='White')
                    name.grid(row=row_count, column=1, sticky=N+S+E+W)

                    rank = Label(root, text=x['cmc_rank'], bg='Silver')
                    rank.grid(row=row_count, column=2, sticky=N+S+E+W)

                    current_price = Label(root, text='${0:.2f}'.format(float(x['quote']['USD']['price'])), bg='White')
                    current_price.grid(row=row_count, column=3, sticky=N+S+E+W)

                    price_paid = Label(root, text='${0:.2f}'.format(float(coin['price_paid_per'])), bg='Silver')
                    price_paid.grid(row=row_count, column=4, sticky=N+S+E+W)

                    pl_per = Label(root, text='${0:.2f}'.format(float(profit_loss_per_coin)), bg='White', fg=red_green(float(profit_loss_per_coin)))
                    pl_per.grid(row=row_count, column=5, sticky=N+S+E+W)

                    one_hr_change = Label(root, text='{0:.2f}%'.format(float(x['quote']['USD']['percent_change_1h'])), bg='Silver',fg=red_green(float(x['quote']['USD']['percent_change_1h'])))
                    one_hr_change.grid(row=row_count, column=6, sticky=N+S+E+W)

                    tf_hr_change = Label(root, text='{0:.2f}%'.format(float(x['quote']['USD']['percent_change_24h'])), bg='White', fg=red_green(float(x['quote']['USD']['percent_change_24h'])))
                    tf_hr_change.grid(row=row_count, column=7, sticky=N+S+E+W)

                    seven_day_change = Label(root, text='{0:.2f}%'.format(float(x['quote']['USD']['percent_change_7d'])), bg='Silver', fg=red_green(float(x['quote']['USD']['percent_change_7d'])))
                    seven_day_change.grid(row=row_count, column=8, sticky=N+S+E+W)

                    current_value = Label(root, text='${0:.2f}'.format(float(current_value)), bg='White')
                    current_value.grid(row=row_count, column=9, sticky=N+S+E+W)

                    pl_total = Label(root, text='${0:.2f}'.format(float(profit_loss)), bg='Silver', fg=red_green(float(profit_loss)))
                    pl_total.grid(row=row_count, column=10, sticky=N+S+E+W)
                    
                    row_count += 1
                    
        portfolio_profits = Label(root, text='P/L: ${0:.2f}'.format(float(portfolio_profit_loss)), bg='Silver', fg=red_green(float(portfolio_profit_loss)))
        portfolio_profits.grid(row=row_count, column=1, sticky=W, padx=10, pady=10)
        
        root.title('Crypto Currency Portfolio - Portfolio Value: ${0:.2f}'.format(float(total_current_value)))
        #total_current_value_output = Label(root, text='P/L: ${0:.2f}'.format(float(total_current_value)), bg='Silver', fg=red_green(float(total_current_value)))
        #total_current_value_output.grid(row=row_count+1, column=1, sticky=W, padx=10, pady=10)
        api = ""
        update_button = Button(root, text="Update Prices", command=lookup)
        update_button.grid(row=row_count, column=10, sticky=E+S, padx=10, pady=10)
        
        def graph(labels, sizes):
            labels = pie
            sizes = pie_size
            colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red']
            patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
            plt.legend(patches, labels, loc="best")
            plt.axis('equal')
            plt.tight_layout()
            plt.show()
        
        graph_button = Button(root, text='Pie Chart', command= lambda: graph(pie, pie_size))
        graph_button.grid(row=row_count, column=8, sticky=E+S, padx=10, pady=10)
        
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: {e}")

    root.mainloop()

lookup()


