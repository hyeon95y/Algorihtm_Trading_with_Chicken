import pandas as pd
import pandas_datareader.data as web
import datetime
import requests
import bs4


calls_amount = ['총건수', '강남구, 10대, 남', '강남구, 10대, 여', '강남구, 20대, 남', '강남구, 20대, 여', '강남구, 30대, 남', '강남구, 30대, 여', '강남구, 40대, 남', '강남구, 40대, 여', '강남구, 50대, 남', '강남구, 50대, 여', '강남구, 60대, 남', '강남구, 60대, 여', '강동구, 10대, 남', '강동구, 10대, 여', '강동구, 20대, 남', '강동구, 20대, 여', '강동구, 30대, 남', '강동구, 30대, 여', '강동구, 40대, 남', '강동구, 40대, 여', '강동구, 50대, 남', '강동구, 50대, 여', '강동구, 60대, 남', '강동구, 60대, 여', '강북구, 10대, 남', '강북구, 10대, 여', '강북구, 20대, 남', '강북구, 20대, 여', '강북구, 30대, 남', '강북구, 30대, 여', '강북구, 40대, 남', '강북구, 40대, 여', '강북구, 50대, 남', '강북구, 50대, 여', '강북구, 60대, 남', '강북구, 60대, 여', '강서구, 10대, 남', '강서구, 10대, 여', '강서구, 20대, 남', '강서구, 20대, 여', '강서구, 30대, 남', '강서구, 30대, 여', '강서구, 40대, 남', '강서구, 40대, 여', '강서구, 50대, 남', '강서구, 50대, 여', '강서구, 60대, 남', '강서구, 60대, 여', '관악구, 10대, 남', '관악구, 10대, 여', '관악구, 20대, 남', '관악구, 20대, 여', '관악구, 30대, 남', '관악구, 30대, 여', '관악구, 40대, 남', '관악구, 40대, 여', '관악구, 50대, 남', '관악구, 50대, 여', '관악구, 60대, 남', '관악구, 60대, 여', '광진구, 10대, 남', '광진구, 10대, 여', '광진구, 20대, 남', '광진구, 20대, 여', '광진구, 30대, 남', '광진구, 30대, 여', '광진구, 40대, 남', '광진구, 40대, 여', '광진구, 50대, 남', '광진구, 50대, 여', '광진구, 60대, 남', '광진구, 60대, 여', '구로구, 10대, 남', '구로구, 10대, 여', '구로구, 20대, 남', '구로구, 20대, 여', '구로구, 30대, 남', '구로구, 30대, 여', '구로구, 40대, 남', '구로구, 40대, 여', '구로구, 50대, 남', '구로구, 50대, 여', '구로구, 60대, 남', '구로구, 60대, 여', '금천구, 10대, 남', '금천구, 10대, 여', '금천구, 20대, 남', '금천구, 20대, 여', '금천구, 30대, 남', '금천구, 30대, 여', '금천구, 40대, 남', '금천구, 40대, 여', '금천구, 50대, 남', '금천구, 50대, 여', '금천구, 60대, 남', '금천구, 60대, 여', '노원구, 10대, 남', '노원구, 10대, 여', '노원구, 20대, 남', '노원구, 20대, 여', '노원구, 30대, 남', '노원구, 30대, 여', '노원구, 40대, 남', '노원구, 40대, 여', '노원구, 50대, 남', '노원구, 50대, 여', '노원구, 60대, 남', '노원구, 60대, 여', '도봉구, 10대, 남', '도봉구, 10대, 여', '도봉구, 20대, 남', '도봉구, 20대, 여', '도봉구, 30대, 남', '도봉구, 30대, 여', '도봉구, 40대, 남', '도봉구, 40대, 여', '도봉구, 50대, 남', '도봉구, 50대, 여', '도봉구, 60대, 남', '도봉구, 60대, 여', '동대문구, 10대, 남', '동대문구, 10대, 여', '동대문구, 20대, 남', '동대문구, 20대, 여', '동대문구, 30대, 남', '동대문구, 30대, 여', '동대문구, 40대, 남', '동대문구, 40대, 여', '동대문구, 50대, 남', '동대문구, 50대, 여', '동대문구, 60대, 남', '동대문구, 60대, 여', '동작구, 10대, 남', '동작구, 10대, 여', '동작구, 20대, 남', '동작구, 20대, 여', '동작구, 30대, 남', '동작구, 30대, 여', '동작구, 40대, 남', '동작구, 40대, 여', '동작구, 50대, 남', '동작구, 50대, 여', '동작구, 60대, 남', '동작구, 60대, 여', '마포구, 10대, 남', '마포구, 10대, 여', '마포구, 20대, 남', '마포구, 20대, 여', '마포구, 30대, 남', '마포구, 30대, 여', '마포구, 40대, 남', '마포구, 40대, 여', '마포구, 50대, 남', '마포구, 50대, 여', '마포구, 60대, 남', '마포구, 60대, 여', '서대문구, 10대, 남', '서대문구, 10대, 여', '서대문구, 20대, 남', '서대문구, 20대, 여', '서대문구, 30대, 남', '서대문구, 30대, 여', '서대문구, 40대, 남', '서대문구, 40대, 여', '서대문구, 50대, 남', '서대문구, 50대, 여', '서대문구, 60대, 남', '서대문구, 60대, 여', '서초구, 10대, 남', '서초구, 10대, 여', '서초구, 20대, 남', '서초구, 20대, 여', '서초구, 30대, 남', '서초구, 30대, 여', '서초구, 40대, 남', '서초구, 40대, 여', '서초구, 50대, 남', '서초구, 50대, 여', '서초구, 60대, 남', '서초구, 60대, 여', '성동구, 10대, 남', '성동구, 10대, 여', '성동구, 20대, 남', '성동구, 20대, 여', '성동구, 30대, 남', '성동구, 30대, 여', '성동구, 40대, 남', '성동구, 40대, 여', '성동구, 50대, 남', '성동구, 50대, 여', '성동구, 60대, 남', '성동구, 60대, 여', '성북구, 10대, 남', '성북구, 10대, 여', '성북구, 20대, 남', '성북구, 20대, 여', '성북구, 30대, 남', '성북구, 30대, 여', '성북구, 40대, 남', '성북구, 40대, 여', '성북구, 50대, 남', '성북구, 50대, 여', '성북구, 60대, 남', '성북구, 60대, 여', '송파구, 10대, 남', '송파구, 10대, 여', '송파구, 20대, 남', '송파구, 20대, 여', '송파구, 30대, 남', '송파구, 30대, 여', '송파구, 40대, 남', '송파구, 40대, 여', '송파구, 50대, 남', '송파구, 50대, 여', '송파구, 60대, 남', '송파구, 60대, 여', '양천구, 10대, 남', '양천구, 10대, 여', '양천구, 20대, 남', '양천구, 20대, 여', '양천구, 30대, 남', '양천구, 30대, 여', '양천구, 40대, 남', '양천구, 40대, 여', '양천구, 50대, 남', '양천구, 50대, 여', '양천구, 60대, 남', '양천구, 60대, 여', '영등포구, 10대, 남', '영등포구, 10대, 여', '영등포구, 20대, 남', '영등포구, 20대, 여', '영등포구, 30대, 남', '영등포구, 30대, 여', '영등포구, 40대, 남', '영등포구, 40대, 여', '영등포구, 50대, 남', '영등포구, 50대, 여', '영등포구, 60대, 남', '영등포구, 60대, 여', '용산구, 10대, 남', '용산구, 10대, 여', '용산구, 20대, 남', '용산구, 20대, 여', '용산구, 30대, 남', '용산구, 30대, 여', '용산구, 40대, 남', '용산구, 40대, 여', '용산구, 50대, 남', '용산구, 50대, 여', '용산구, 60대, 남', '용산구, 60대, 여', '은평구, 10대, 남', '은평구, 10대, 여', '은평구, 20대, 남', '은평구, 20대, 여', '은평구, 30대, 남', '은평구, 30대, 여', '은평구, 40대, 남', '은평구, 40대, 여', '은평구, 50대, 남', '은평구, 50대, 여', '은평구, 60대, 남', '은평구, 60대, 여', '종로구, 10대, 남', '종로구, 10대, 여', '종로구, 20대, 남', '종로구, 20대, 여', '종로구, 30대, 남', '종로구, 30대, 여', '종로구, 40대, 남', '종로구, 40대, 여', '종로구, 50대, 남', '종로구, 50대, 여', '종로구, 60대, 남', '종로구, 60대, 여', '중구, 10대, 남', '중구, 10대, 여', '중구, 20대, 남', '중구, 20대, 여', '중구, 30대, 남', '중구, 30대, 여', '중구, 40대, 남', '중구, 40대, 여', '중구, 50대, 남', '중구, 50대, 여', '중구, 60대, 남', '중구, 60대, 여', '중랑구, 10대, 남', '중랑구, 10대, 여', '중랑구, 20대, 남', '중랑구, 20대, 여', '중랑구, 30대, 남', '중랑구, 30대, 여', '중랑구, 40대, 남', '중랑구, 40대, 여', '중랑구, 50대, 남', '중랑구, 50대, 여', '중랑구, 60대, 남', '중랑구, 60대, 여']

def display_all(df) : 
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        display(df)
    return

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
    
def load_data_by_ticker(kospi, ticker) : 
    metadata = kospi[kospi['종목코드'] == ticker]
    
    data = pd.read_pickle('data/kospi/%s.data'%ticker)
    data.index = pd.to_datetime(data.index)
    
    data['High'] = pd.to_numeric(data['High'])
    data['Low'] = pd.to_numeric(data['Low'])
    data['Open'] = pd.to_numeric(data['Open'])
    data['Close'] = pd.to_numeric(data['Close'])
    data['Volume'] = pd.to_numeric(data['Volume'])
    
    return metadata, data

def get_call_data_for_given_ticker(calls, kospi, ticker) : 
    metadata, stock = load_data_by_ticker(kospi, ticker)
    
    # 1. stock
    #display(stock)
    
    # 2. calls
    chicken = calls[calls_amount]
    chicken.index = calls.index
    #display(chicken)
    
    # 3. merge to dataframe to get common period
    df_totest = stock.merge(chicken, how='inner', left_on=stock.index, right_on=chicken.index)
    df_totest.index = df_totest['key_0']
    df_totest = df_totest.drop(['key_0'], axis=1)
    
    return metadata['기업명'].values[0], df_totest