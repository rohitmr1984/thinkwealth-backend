from fastapi import FastAPI
import pandas as pd
import pandas_ta as ta
import vectorbt as vbt

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "Python backend is running"}

@app.post("/backtest")
def backtest_strategy(strategy: dict):
    # Example strategy input: {"ema_fast":20, "ema_slow":50}
    df = pd.DataFrame({
        "Close": [100,101,102,103,102,101,105,107,106,108]
    })
    
    df['ema_fast'] = ta.ema(df['Close'], length=strategy.get("ema_fast", 20))
    df['ema_slow'] = ta.ema(df['Close'], length=strategy.get("ema_slow", 50))
    
    entries = df['ema_fast'] > df['ema_slow']
    exits = df['ema_fast'] < df['ema_slow']

    pf = vbt.Portfolio.from_signals(
        close=df['Close'],
        entries=entries,
        exits=exits
    )

    return {
        "final_value": float(pf.total_return()),
        "sharpe": float(pf.sharpe_ratio()),
        "trades": int(pf.trades.count())
    }
