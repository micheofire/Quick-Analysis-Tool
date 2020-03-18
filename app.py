from flask import Flask, request, render_template, session, redirect
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
from flask_jsonpify import jsonpify
import plotly.graph_objects as go

app = Flask(__name__)

start = datetime.datetime(2007, 1, 1)
end = datetime.datetime.now()



@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')



#HISTORICAL TABLE AND HISTORICAL PLOT WITH ROLLING AVERAGE FOR APPLE STOCK
@app.route('/table/AAPL')
def table_AAPL():
    df = web.DataReader('AAPL', 'yahoo', start, end)
    df_sort = df.sort_index(axis=0, ascending=False)
    return df_sort.to_html(header="true", table_id="table")
@app.route('/rolling_mean/AAPL')
def rolling_mean_AAPL():
    df = web.DataReader('AAPL', 'yahoo', start, end)
    close_px = df['Adj Close']
    mavg = close_px.rolling(window=100).mean()
    mavg.tail(10)

    df['Date'] = df.index
    
    #USING PLOTLY FOR INTERACTIVE VISULIZATION
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.Date, y=df['Adj Close'], name="Adj Close",
                             line_color='deepskyblue'))

    fig.add_trace(go.Scatter(x=df.Date, y=mavg[:], name="Moving Average",
                             line_color='dimgray'))

    fig.update_layout(title_text='APPLE STOCK PRICE CHART',
                      xaxis_rangeslider_visible=True)
    return fig.to_html()



#HISTORICAL TABLE AND HISTORICAL PLOT WITH ROLLING AVERAGE FOR GOOGLE STOCK
@app.route('/table/GOOG')
def table_GOOG():
    df = web.DataReader('GOOG', 'yahoo', start, end)
    df_sort = df.sort_index(axis=0, ascending=False)
    return df_sort.to_html(header="true", table_id="table")
@app.route('/rolling_mean/GOOG')
def rolling_mean_GOOG():
    df = web.DataReader('GOOG', 'yahoo', start, end)
    close_px = df['Adj Close']
    mavg = close_px.rolling(window=100).mean()
    mavg.tail(10)

    df['Date'] = df.index
    
    #USING PLOTLY FOR INTERACTIVE VISULIZATION
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.Date, y=df['Adj Close'], name="Adj Close",
                             line_color='deepskyblue'))

    fig.add_trace(go.Scatter(x=df.Date, y=mavg[:], name="Moving Average",
                             line_color='dimgray'))

    fig.update_layout(title_text='GOOGLE STOCK PRICE CHART',
                      xaxis_rangeslider_visible=True)
    return fig.to_html()

#HISTORICAL TABLE AND HISTORICAL PLOT WITH ROLLING AVERAGE FOR MICROSOFT STOCK
@app.route('/table/MICR')
def table_MICR():
    df = web.DataReader('MICR', 'yahoo', start, end)
    df_sort = df.sort_index(axis=0, ascending=False)
    return df_sort.to_html(header="true", table_id="table")
@app.route('/rolling_mean/MICR')
def rolling_mean_MICR():
    df = web.DataReader('MICR', 'yahoo', start, end)
    close_px = df['Adj Close']
    mavg = close_px.rolling(window=100).mean()
    mavg.tail(10)

    df['Date'] = df.index
    
    #USING PLOTLY FOR INTERACTIVE VISULIZATION
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.Date, y=df['Adj Close'], name="Adj Close",
                             line_color='deepskyblue'))

    fig.add_trace(go.Scatter(x=df.Date, y=mavg[:], name="Moving Average",
                             line_color='dimgray'))

    fig.update_layout(title_text='MICROSOFT STOCK PRICE CHART',
                      xaxis_rangeslider_visible=True)
    return fig.to_html()

#HISTORICAL TABLE AND HISTORICAL PLOT WITH ROLLING AVERAGE FOR TESCO STOCK
@app.route('/table/TSCO')
def table_TSCO():
    df = web.DataReader('TSCO', 'yahoo', start, end)
    df_sort = df.sort_index(axis=0, ascending=False)
    return df_sort.to_html(header="true", table_id="table")
@app.route('/rolling_mean/TSCO')
def rolling_mean_TSCO():
    df = web.DataReader('TSCO', 'yahoo', start, end)
    close_px = df['Adj Close']
    mavg = close_px.rolling(window=100).mean()
    mavg.tail(10)

    df['Date'] = df.index
    
    #USING PLOTLY FOR INTERACTIVE VISULIZATION
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.Date, y=df['Adj Close'], name="Adj Close",
                             line_color='deepskyblue'))

    fig.add_trace(go.Scatter(x=df.Date, y=mavg[:], name="Moving Average",
                             line_color='dimgray'))

    fig.update_layout(title_text='TESCO STOCK PRICE CHART',
                      xaxis_rangeslider_visible=True)
    return fig.to_html()


if __name__ == "__main__":
    app.run(debug = True)