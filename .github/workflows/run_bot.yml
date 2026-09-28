import requests
import datetime

def get_crypto_prices():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        btc = data.get('bitcoin', {}).get('usd', 'N/A')
        eth = data.get('ethereum', {}).get('usd', 'N/A')
        sol = data.get('solana', {}).get('usd', 'N/A')
        
        return f"🪙 **Crypto Market Update:**\n- Bitcoin (BTC): ${btc}\n- Ethereum (ETH): ${eth}\n- Solana (SOL): ${sol}"
    except Exception as e:
        return f"Could not fetch crypto prices: {e}"

def get_weather():
    try:
        # Example coordinates for New York (change if desired)
        url = "https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&current_weather=true"
        response = requests.get(url, timeout=10)
        data = response.json()
        weather = data.get('current_weather', {})
        
        temp = weather.get('temperature', 'N/A')
        wind = weather.get('windspeed', 'N/A')
        
        return f"🌤️ **Weather Update (New York):**\n- Temperature: {temp}°C\n- Wind Speed: {wind} km/h"
    except Exception as e:
        return f"Could not fetch weather: {e}"

if __name__ == "__main__":
    print("=" * 40)
    print(f"🤖 Bot Report Run Timestamp: {datetime.datetime.now()}")
    print("=" * 40)
    
    crypto_report = get_crypto_prices()
    print(crypto_report)
    print("-" * 40)
    
    weather_report = get_weather()
    print(weather_report)
    print("=" * 40)