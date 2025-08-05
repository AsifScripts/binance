import time
from binance.client import Client
from binance.exceptions import BinanceAPIException

# ✅ Use your Testnet API credentials
API_KEY = '42ed02a3f3700eccd761a106542365747362aa3b1890825b35961fa195e714b9'
API_SECRET = '5111b4420062b973fa7949cdeaa7884d8d334adfa75d0516eb8b91b372fa566b'

# ✅ Initialize client for Binance TESTNET
client = Client(API_KEY, API_SECRET)
client.API_URL = 'https://testnet.binance.vision/api'  # <-- Testnet endpoint

# try: print(client.get_account()) 
# except Exception as e: print(e)

def sync_time():
    """Synchronize local time with Binance server time to avoid timestamp errors."""
    try:
        server_time = client.get_server_time()['serverTime']
        local_time = int(time.time() * 1000)
        offset = server_time - local_time
        client.timestamp_offset = offset
    except BinanceAPIException as e:
        print(f"Time sync error: {e.message}")

def get_prices(symbols):
    """Get current prices for a list of symbols."""
    prices = {}
    for symbol in symbols:
        try:
            ticker = client.get_symbol_ticker(symbol=symbol)
            prices[symbol] = ticker['price']
        except BinanceAPIException as e:
            prices[symbol] = f"Error: {e.message}"
    return prices

def place_order(symbol, side, quantity):
    """Place a market order for a given symbol."""
    sync_time()
    try:
        order = client.create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        return order
    except BinanceAPIException as e:
        return {'error': e.message}

def get_order_status(symbol, order_id):
    """Get the status of an order."""
    sync_time()
    try:
        return client.get_order(symbol=symbol, orderId=order_id)
    except BinanceAPIException as e:
        return {'error': e.message}

def cancel_order(symbol, order_id):
    """Cancel an active order."""
    sync_time()
    try:
        return client.cancel_order(symbol=symbol, orderId=order_id)
    except BinanceAPIException as e:
        return {'error': e.message}
