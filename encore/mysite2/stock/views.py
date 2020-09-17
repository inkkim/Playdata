from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
def get_data(symbol, buy_date):
    url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(symbol)

    with urlopen(url) as doc:
        soup = BeautifulSoup(doc, "lxml", from_encoding="euc-kr")
        cur_price = soup.find('strong', id='_nowVal')  # ①
        cur_rate = soup.find('strong', id='_rate')  # ②
        cur_date = soup.find('')
        stock = soup.find('title')  # ③
        stock_name = stock.text.split(':')[0].strip()  # ④
        end_point = '1,000'
        flag1, flag2 = True, True
    for page in range(1, 999):
        target = []
        url_page = 'http://finance.naver.com/item/sise_day.nhn?code={}&page={}'.format(symbol, page)
        soup_page = BeautifulSoup(urlopen(url_page), 'lxml', from_encoding='euc-kr')
        date = soup_page.find('table').find_all('td', align='center')
        for day in date:
            target.append(str(day.text).replace('.', ''))
            if str(buy_date) in target:
                row = soup_page.find_all('tr', onmouseover = 'mouseOver(this)')
                for idx in row:
                    date_price = idx.find_all('td')
                    target_date = date_price[0].text.replace('.', '')
                    price = date_price[1].text
                    if target_date == str(buy_date):
                        end_point = price # str
                        print('break ====')
                        flag1 = False
                        break
            if flag1 ==False:
                print('flag1 ====')
                flag2 = False
                break
        if flag2 ==False:
            print('flag2 ====')
            break

    return cur_price.text, cur_rate.text.strip(), stock_name, end_point


def main_view(request):
    querydict = request.GET.copy()
    mylist = querydict.lists()  # ⑤
    rows = []
    total = 0
# 특정 날짜에 샀던 종목을 기준으로 현재 수익률 나타내기
    # 종목코드 -> 매수날짜
    # 매수날짜를 기준으로 현재 수익이 얼만지?
    for x in mylist:
        cur_price, cur_rate, stock_name, end_point = get_data(x[0],x[1][1])  # ⑥
        price = cur_price.replace(',', '')
        buy_price = end_point.replace(',', '')
        buy_price_date = x[1][1]
        stock_count = format(int(x[1][0]), ',')  # ⑦
        sum = int(price) * int(x[1][0])
        stock_sum = format(sum, ',')
        sell_price = int(cur_price.replace(',', ''))
        # (팔 때 * 주식 수) / (살 때 * 주식 수)
        cur_revenue = (sell_price) / (int(buy_price.replace(',', '')))
        revenue_rate = round(cur_revenue, 2)
        # (팔 때 * 주식 수) - (살 때 * 주식 수)
        money = (sell_price * int(x[1][0])) - (int(buy_price) * int(x[1][0]))
        buy_date = datetime.strptime(x[1][1], '%Y%m%d').date()
        sell_date = datetime.now().date()
        total_money = format(money, ',')
        rows.append([stock_name, buy_date, end_point, sell_date, cur_price, stock_count, str(revenue_rate) + '%',
            total_money])  # ⑧
        total = total + money  # ⑨

    total_amount = format(total, ',')
    values = {'rows' : rows, 'total' : total_amount}  # ⑩
    return render(request, 'index.html', values)  # ⑪
#