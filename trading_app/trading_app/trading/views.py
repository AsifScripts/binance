from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .binance_api import get_prices, place_order, get_order_status, cancel_order

SYMBOLS = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'ADAUSDT', 'XRPUSDT']

@login_required
def dashboard(request):
    prices = get_prices(SYMBOLS)
    return render(request, 'trading/dashboard.html', {'prices': prices})

@login_required
def place_order_view(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        side = request.POST['side']
        quantity = float(request.POST['quantity'])
        order = place_order(symbol, side, quantity)
        return render(request, 'trading/order_status.html', {'order': order})
    return render(request, 'trading/place_order.html', {'symbols': SYMBOLS})

@login_required
def order_status_view(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        order_id = int(request.POST['order_id'])
        status = get_order_status(symbol, order_id)
        return render(request, 'trading/order_status.html', {'order': status})
    return render(request, 'trading/order_status.html')

@login_required
def cancel_order_view(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        order_id = int(request.POST['order_id'])
        result = cancel_order(symbol, order_id)
        return render(request, 'trading/order_status.html', {'order': result})
    return render(request, 'trading/order_status.html')