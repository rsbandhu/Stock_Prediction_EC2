from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from model import predict, convert

app = FastAPI()

#pydantic models
class StockIn(BaseModel):
    ticker: str
    days: int

class StockOut(StockIn):
    forecast: dict

@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    ticker = payload.ticker
    days = payload.days

    prediction_list = predict(ticker, days)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {
        "ticker": ticker,
        "days": days,
        "forecast": convert(prediction_list)}
    return response_object
'''
@app.get("/ping")
def pong():
    return {"ping": "pong!"}
'''
### Answers to questions

## How does the Prophet Algorithm differ from an LSTM?
### Answer:
### Prphet algorithm is an additive model where different seasonal dependencies (such as weekly, monthly dependence) are explicitly modeled using ARIMA.

## Why does an LSTM have poor performance against ARIMA and Profit for Time Series?
### Answer: 
### LSTM can't take into account cyclical behavor effectively. There is no natural way to extract the cyclical time dependence of an event using LSTM. 
### Where as ARIMA explicitly models the cyclical nature of the data

## What is exponential smoothing and why is it used in Time Series Forecasting?
### Answer: 
### Exponential smoothing updates the estimates based not only on the current observation but also on the past observations.
### Observations that are n time steps behind contribute with an weight that is exponentially small i.e. proportional to exp (-kn)
### They are used to smooth out high frequency noise in the data

## What is stationarity? What is seasonality? Why Is Stationarity Important in Time Series Forecasting?

### Answers: 
### Stationarity means the dynamics is not time dependent. We have the same correlation / covariance matrix that doesn't depend on time.
### Seasonality means someething that have similar behavior that depends on the season, e.g. rainfall by month is a seasonal behavior.

### How is seasonality different from cyclicality? Fill in the blanks:
### Answer: __ Cyclicality_ is predictable, whereas __ seasonality_ is not.
