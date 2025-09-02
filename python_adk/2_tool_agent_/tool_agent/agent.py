from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search
from yfinance import Ticker
import dotenv
import requests
import os


dotenv.load_dotenv()


def get_current_time() -> dict:
    """get the current time formate YYYY-MM-DD HH:MM:SS"""
    return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }


def get_current_weather(city:str) -> dict:
    """Get the current weather information."""
    # api_key = dotenv.get_key(dotenv.find_dotenv(), "WEATHER_API_KEY")
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url).json()
    if res.get("cod") != 200:
        return {"error": res.get("message", "Unable to fetch weather")}
    return {
        "city": city,
        "temperature": res["main"]["temp"],
        "weather": res["weather"][0]["description"],
        "humidity": res["main"]["humidity"],
    }

def get_current_stock_price(symbol: str) -> dict:
    """Get the current stock price information."""
    ticker = Ticker(symbol)
    data = ticker.history(period="1d")
    timestamp = data.index[-1]
    if data.empty:
        return {"error": "Unable to fetch stock data"}
    return {
        "symbol": symbol,
        "time": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "price": round(data["Close"].iloc[-1], 2),

    }

root_agent=Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="A tool agent",
    instruction="""You're a specialist in Google Search.""",
    # tools=[google_search],
    # tools=[get_current_time]
    # tools=[get_current_weather],
    tools=[get_current_stock_price],
)
