from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

class AlpacaTrader:
    def __init__(self, key, secret, base_url):
        self.client = TradingClient(key, secret, paper=True)

    def place_order(self, symbol, signal, qty=1):
        side = OrderSide.BUY if signal == 1 else OrderSide.SELL
        try:
            order_data = MarketOrderRequest(
                symbol=symbol,
                qty=qty,
                side=side,
                time_in_force=TimeInForce.GTC
            )
            order = self.client.submit_order(order_data)
            print(f"Order submitted: {side.value} {qty} {symbol}")
            return order
        except Exception as e:
            print("Error submitting order:", e)
            return None