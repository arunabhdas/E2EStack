from pydantic_ai import Agent
from pydantic import BaseModel
import yfinance as yf
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()

class StockPriceResult(BaseModel):
    symbol: str
    price: float
    currency: str = "USD"
    message: str

stock_agent = Agent(
    model="groq:llama3-groq-70b-8192-tool-use-preview",
    result_type=StockPriceResult,
    system_prompt="You are a helpful financial assistant that can look up stock prices. Use the get_stock_price tool to fetch current data."
)

@stock_agent.tool_plain
def get_stock_price(symbol: str) -> dict:
    ticker = yf.Ticker(symbol)
    price = ticker.fast_info.last_price
    return {
        "symbol": symbol, 
        "price": price, 
        "currency": "USD"
    }

if __name__ == "__main__":
    result = stock_agent.run_sync("What is Apple's current stock price?")
    print(f"Stock Price: ${result.data.price:.2f} {result.data.currency}")


