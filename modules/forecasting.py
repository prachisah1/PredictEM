from prophet import Prophet
import pandas as pd

def forecast_demand(data):

    df = pd.DataFrame(data)

    df.columns = ["ds", "y"]

    model = Prophet()

    model.fit(df)

    future = model.make_future_dataframe(periods=7)

    forecast = model.predict(future)

    return forecast[["ds", "yhat"]]