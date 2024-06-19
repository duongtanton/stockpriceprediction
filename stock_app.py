import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from keras.models import load_model # type: ignore
from sklearn.preprocessing import MinMaxScaler
import numpy as np

import yfinance as yf

# Fetch data from Yahoo Finance
def fetch_data(ticker):
    df = yf.download(ticker, start='2019-01-01', end='2024-06-01')
    df['Date'] = df.index
    return df

# Load data
btc_data = fetch_data('BTC-USD')
eth_data = fetch_data('ETH-USD')
ada_data = fetch_data('ADA-USD')

app = dash.Dash()
server = app.server

scaler=MinMaxScaler(feature_range=(0,1))

result = {}
def buid_data_for_display(df_nse, name):
    df_nse["Date"]=pd.to_datetime(df_nse.Date,format="%Y-%m-%d")
    df_nse.index=df_nse['Date']


    data=df_nse.sort_index(ascending=True,axis=0)
    new_data=pd.DataFrame(index=range(0,len(df_nse)),columns=['Date','Close'])

    for i in range(0,len(data)):
        new_data["Date"][i]=data['Date'][i]
        new_data["Close"][i]=data["Close"][i]

    new_data.index=new_data.Date
    new_data.drop("Date",axis=1,inplace=True)

    dataset=new_data.values

    train=dataset[0:987,:]
    valid=dataset[987:,:]

    scaler=MinMaxScaler(feature_range=(0,1))
    scaled_data=scaler.fit_transform(dataset)

    x_train,y_train=[],[]

    for i in range(60,len(train)):
        x_train.append(scaled_data[i-60:i,0])
        y_train.append(scaled_data[i,0])
        
    x_train,y_train=np.array(x_train),np.array(y_train)

    x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))

    model=load_model(name + "_saved_model.h5")

    inputs=new_data[len(new_data)-len(valid)-60:].values
    inputs=inputs.reshape(-1,1)
    inputs=scaler.transform(inputs)

    X_test=[]
    for i in range(60,inputs.shape[0]):
        X_test.append(inputs[i-60:i,0])
    X_test=np.array(X_test)

    X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
    closing_price=model.predict(X_test)
    closing_price=scaler.inverse_transform(closing_price)

    train=new_data[:987]
    valid=new_data[987:]
    valid['Predictions']=closing_price
    result[name] = {}
    result[name]["train"] = train
    result[name]["valid"] = valid

buid_data_for_display(btc_data, 'BTC')
buid_data_for_display(eth_data, 'ETH')
buid_data_for_display(ada_data, 'ADA')

app.layout = html.Div([
    html.H1("Stock Price Analysis Dashboard", style={"textAlign": "center"}),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='BTC-USD',children=[
			html.Div([
				html.H2("BTC Actual closing price",style={"textAlign": "center"}),
				dcc.Graph(
					id="BTC Actual Data",
					figure={
						"data":[
							go.Scatter(
								x=result["BTC"]["train"].index,
								y=result["BTC"]["valid"]["Close"],
								mode='markers'
							)

						],
						"layout":go.Layout(
							title='scatter plot',
							xaxis={'title':'Date'},
							yaxis={'title':'Closing Rate'}
						)
					}

				),
				html.H2("BTC LSTM Predicted closing price",style={"textAlign": "center"}),
				dcc.Graph(
					id="BTC Predicted Data",
					figure={
						"data":[
							go.Scatter(
								x=result["BTC"]["valid"].index,
								y=result["BTC"]["valid"]["Predictions"],
								mode='markers'
							)

						],
						"layout":go.Layout(
							title='scatter plot',
							xaxis={'title':'Date'},
							yaxis={'title':'Closing Rate'}
						)
					}

				)				
			])        		

        ]),
        dcc.Tab(label='ETH-USD',children=[
			html.Div([
				html.H2("ETH Actual closing price",style={"textAlign": "center"}),
				dcc.Graph(
					id="ETH Actual Data",
					figure={
						"data":[
							go.Scatter(
								x=result["ETH"]["train"].index,
								y=result["ETH"]["valid"]["Close"],
								mode='markers'
							)

						],
						"layout":go.Layout(
							title='scatter plot',
							xaxis={'title':'Date'},
							yaxis={'title':'Closing Rate'}
						)
					}

				),
				html.H2("ETH LSTM Predicted closing price",style={"textAlign": "center"}),
				dcc.Graph(
					id="ETH Predicted Data",
					figure={
						"data":[
							go.Scatter(
								x=result["ETH"]["valid"].index,
								y=result["ETH"]["valid"]["Predictions"],
								mode='markers'
							)

						],
						"layout":go.Layout(
							title='scatter plot',
							xaxis={'title':'Date'},
							yaxis={'title':'Closing Rate'}
						)
					}

				)				
			])        		

        ]),
        dcc.Tab(label='ADA-USD',children=[
			html.Div([
				html.H2("ADA Actual closing price",style={"textAlign": "center"}),
				dcc.Graph(
					id="ADA Actual Data",
					figure={
						"data":[
							go.Scatter(
								x=result["ADA"]["train"].index,
								y=result["ADA"]["valid"]["Close"],
								mode='markers'
							)

						],
						"layout":go.Layout(
							title='scatter plot',
							xaxis={'title':'Date'},
							yaxis={'title':'Closing Rate'}
						)
					}

				),
				html.H2("ADA LSTM Predicted closing price",style={"textAlign": "center"}),
				dcc.Graph(
					id="ADA Predicted Data",
					figure={
						"data":[
							go.Scatter(
								x=result["ADA"]["valid"].index,
								y=result["ADA"]["valid"]["Predictions"],
								mode='markers'
							)

						],
						"layout":go.Layout(
							title='scatter plot',
							xaxis={'title':'Date'},
							yaxis={'title':'Closing Rate'}
						)
					}

				)				
			])        		
        ]),
    ])
])

if __name__=='__main__':
	app.run_server(debug=True)