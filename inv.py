import finnhub
import pandas as pd
import pandas_datareader as web

finnhub_client = finnhub.Client(api_key="buv812748v6vrjlu9ueg")

start_date = "2022-02-01"
end_date = "2022-02-07"

x = finnhub_client.indices_const(symbol = "^DJI")["constituents"]
tickers = x

scores_dict = dict()
corr_dict = dict()

for ticker in tickers:
    info = finnhub_client.stock_social_sentiment(ticker, _from = start_date, to = end_date)
    
    reddit = pd.DataFrame.from_dict(info["reddit"]).set_index('atTime')
    reddit = reddit[["mention","score"]]
    
    twitter = pd.DataFrame.from_dict(info["twitter"]).set_index('atTime')
    twitter = twitter[["mention","score"]]
    
    merged = pd.merge(reddit, twitter, left_index=True, right_index=True,
                      suffixes=('_reddit', '_twitter'))
    merged["AvgScore"] = (merged.score_reddit + merged.score_twitter)/2
    
    scores_dict[ticker] = merged.AvgScore
    
scores = pd.DataFrame.from_dict(scores_dict)
scores.index = pd.to_datetime(scores.index)
scores = scores.resample('D').max()

prices = web.DataReader(tickers, "yahoo", start = start_date, end = end_date)["Close"]

for ticker in tickers:
    corr_dict[ticker]=[prices[ticker].corr(scores[ticker])]
    
correlations = (pd.DataFrame.from_dict(corr_dict)).T

    



