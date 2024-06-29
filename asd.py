import requests

BOT_TOKEN = '7075835530:AAHlNztDkDNWDbgJTkvgAQ8diUEdUa69Yho'  # Replace with your bot token

url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates'
response = requests.get(url)
data = response.json()

# Extract chat ID from the response
chat_id = data['result'][0]['message']['chat']['id']
print(f"Chat ID of your bot is: {chat_id}")