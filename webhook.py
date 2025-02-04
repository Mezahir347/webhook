from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual API key
EIA_API_KEY = "YOUR_API_KEY"

# EIA API URL for Brent Crude Oil Price
EIA_URL = f"https://api.eia.gov/v2/petroleum/pri/fut/data/?api_key={iceak3EvOeahbnEL0lAU6gOcJ6TRTd4zApQnH9Fy}&frequency=daily&data[0]=value&facets[series][]=RBRTE"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()

    # Fetch data from EIA API
    response = requests.get(EIA_URL)
    data = response.json()

    # Extract latest oil price
    try:
        oil_price = data['response']['data'][0]['value']
    except (KeyError, IndexError):
        oil_price = "Unavailable"

    # Response to Dialogflow
    return jsonify({"fulfillmentText": f"The current Brent crude oil price is ${oil_price} per barrel."})

if __name__ == '__main__':
    app.run(port=5000)
