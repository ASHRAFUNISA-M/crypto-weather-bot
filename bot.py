import requests
from datetime import datetime

def get_crypto_prices():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        
        btc = data.get('bitcoin', {}).get('usd', 'N/A')
        ethereum = data.get('ethereum', {}).get('usd', 'N/A')
        sol = data.get('solana', {}).get('usd', 'N/A')
        
        return f"BTC: ${btc} | ETH: ${ethereum} | SOL: ${sol}"
    except Exception as e:
        return f"Could not fetch crypto prices: {e}"

def get_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=12.9292&longitude=77.6268&current=temperature_2m,weather_code"
        response = requests.get(url)
        data = response.json()
        
        temp = data.get('current', {}).get('temperature_2m', 'N/A')
        return f"Temperature: {temp}°C"
    except Exception as e:
        return f"Could not fetch weather: {e}"

def generate_html():
    crypto_report = get_crypto_prices()
    weather_report = get_weather()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Crypto & Weather Live Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #0f172a;
                color: #f8fafc;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background-color: #1e293b;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.5);
                max-width: 400px;
                width: 100%;
                text-align: center;
            }}
            h1 {{ font-size: 22px; color: #38bdf8; margin-bottom: 20px; }}
            .section {{
                background: #0f172a;
                padding: 15px;
                margin: 15px 0;
                border-radius: 8px;
                font-size: 16px;
            }}
            .footer {{ font-size: 12px; color: #94a3b8; margin-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Live Status Dashboard</h1>
            <div class="section">
                <strong>🪙 Crypto Prices</strong><br>
                {crypto_report}
            </div>
            <div class="section">
                <strong>🌤️ Weather Report</strong><br>
                {weather_report}
            </div>
            <div class="footer">Last updated: {timestamp}</div>
        </div>
    </body>
    </html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Successfully generated index.html!")

if __name__ == "__main__":
    generate_html()
