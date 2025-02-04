from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API endpoint (Example: Trading Economics)
API_URL = "https://api.eia.gov/series/?series_id=ELEC.SALES.CO-RES.M&api_key=iceak3EvOeahbnEL0lAU6gOcJ6TRTd4zApQnH9Fy"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    
    # Fetch oil price from API
    response = requests.get(API_URL)
    data = response.json()
    
    # Extract price (modify based on API structure)
    oil_price = data[0]['price']  

    # Response back to Dialogflow
    return jsonify({"fulfillmentText": f"The current crude oil price is ${oil_price} per barrel."})

if __name__ == '__main__':
    app.run(port=5000)
