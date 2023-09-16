
def EMA(period, prices):
    alpha = 2/(1+period)
    ema = [None]*(period-1) + [sum(prices[:period])/period]
    for price in prices[period:]:
        ema.append( price*alpha + ema[-1] * (1-alpha) )
    return ema

prices = list()
for i in range(int(input())):
    prices += map(float, input().strip().split(','))

slow_ema = EMA(14, prices)
fast_ema = EMA(7, prices)


ch=0
for i in range(14, len(fast_ema)):
    if fast_ema[i-1] < slow_ema[i-1] and fast_ema[i] > slow_ema[i]:
        print('BUY at %.2f' % prices[i])
        ch=1
    elif fast_ema[i-1] > slow_ema[i-1] and fast_ema[i] < slow_ema[i]:
        print('SELL at %.2f' % prices[i])
        ch=1

if ch==0:
    print("No results")


