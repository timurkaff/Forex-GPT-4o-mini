import yfinance as yf

def get_data(symbol, num_candles=100):
    data = yf.download(symbol, period="5d", interval="1h")
    
    # Ограничиваем количество последних свечей
    data = data.tail(num_candles)
    
    # Удаляем ненужные столбцы
    data = data.drop(columns=['Adj Close', 'Volume'])
    
    # Убираем временную зону из индексов
    data.index = data.index.tz_localize(None)
    
    return data