import pandas as pd
import pandas_datareader.data as web
import datetime
import requests
import bs4

def download_stock_data(file_name, company_code, year1, month1, date1, year2, month2, date2) :
    start = datetime.datetime(year1, month1, date1)
    end = datetime.datetime(year2, month2, date2)
    df = web.DataReader("%s.KS" % (company_code), "yahoo", start, end)
    
    df.to_pickle(file_name)
    
    return df

def load_stock_data(file_name) :
    df = pd.read_pickle(file_name)
    return df

# '퀀트전략 파이썬으로 세워라' 데이터 가공 파트 참조 
# selenium을 이용한 크롤링보다 조금 더 간단하게 진행함

def download_stock_data_from_naver(file_name, symbol, timeframe, count):
    
    #making url
    
    url_a = 'https://fchart.stock.naver.com/sise.nhn?requestType=0'
    url_insert =  url_a+'&symbol='+symbol+'&timeframe='+timeframe+'&count='+count

    #convert into bs(beautifulsoup) object
    
    price_raw = requests.get(url_insert)
    price_bs = bs4.BeautifulSoup(price_raw.text, 'lxml')
    price_list = price_bs.find_all('item')
    
    #empty sheets
    
    date_list = []
    open_list = []
    high_list = []
    low_list = []
    close_list = []
    volume_list = []
    adj_close_list = []
    
    #split the data into date/open/high/low/close/volume
    #close - 차트에서 끌어오기 때문에 수정종가로 자동반영
    
    for piece in price_list:
        temp = piece['data']
        dp = temp.split('|')
        
        date_list.append(dp[0])
        open_list.append(dp[1])
        high_list.append(dp[2])
        low_list.append(dp[3])
        close_list.append(dp[4])
        volume_list.append(dp[5])
        adj_close_list.append('')
    
    #dataframe으로 합치기
    
    dp_to_df = pd.DataFrame({'open': open_list, 'high': high_list, 'low': low_list, 'close': close_list, 'vol': volume_list}, index=date_list)
    
    dp_to_df = pd.DataFrame({'High':high_list,
                            'Low':low_list,
                            'Open':open_list,
                            'Close':close_list,
                            'Volume':volume_list,
                            'Adj Close':adj_close_list}, index=date_list)
    
    dp_to_df.to_pickle(file_name)
    
    return dp_to_df
    