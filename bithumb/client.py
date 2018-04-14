from bithumb.core import *
import pandas as pd


# Input Data 무결성 검사
# Ouput Data reformatting을 해야 함

class client :
    def __init__(self, conkey, seckey):
        self.api = RestApi(conkey, seckey)

    def get_transactions(self, count=10):
        r = self.api.recent_transactions(count=count)
        return pd.DataFrame(r['data'])

    def get_balance(self, currency):
        # out data format
        #{'total_krw': 0, 'in_use_krw': 0, 'available_krw': 0, 'misu_krw': 0, 'total_dash': '0.00000000',
        # 'in_use_dash': '0.00000000', 'available_dash': '0.00000000', 'misu_dash': 0, 'xcoin_last': '381000'}
        # df = pd.DataFrame()
        r = self.api.balance(currency=currency)
        # 어떻게 보여줄 것인지..
        return r['data']

    def put_order(self, type, currency, price, unit):
        r = self.api.place(type=type, price=price, units=unit, order_currency=currency)
        return (type, currency, r['order_id'])

    def get_order(self, order_desc):
        r = self.api.orders(type=order_desc[0], currency=order_desc[1], order_id=order_desc[1])
        return r

    def put_cancel(self, order_desc):
        r = self.api.cancel(type=order_desc[0], currency=order_desc[1], order_id=order_desc[1])
        return r


if __name__ == "__main__":
    c = client('CONKEY', 'SECKEY')

    r = c.get_transactions()
    print (r)

    # r = c.get_balance("DASH")
    # print (r)

    # info = c.put_order("ask", "XRP", 1000, 1000)
    # print (info)
    # r = c.get_order(info)
    # print (r)
    # r = c.put_cancel(info)
    # print(response)
