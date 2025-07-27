from flask import Flask, request, jsonify
from flask_cors import CORS # Used to handle Cross-Origin Resource Sharing

app = Flask(__name__)
CORS(app) # This enables CORS for all routes, allowing Flowise/your frontend to access it

@app.route('/mock-forecast', methods=['GET'])
def mock_forecast():
    product_id = request.args.get('product_id', 'unknown product')
    period = request.args.get('period', 'next month')

    # Simple mock logic based on product_id
    if "bolt" in product_id.lower():
        forecast = 1500
        units = "units"
    elif "nut" in product_id.lower():
        forecast = 2000
        units = "units"
    else:
        forecast = 1000
        units = "units"

    return jsonify({
        "product_id": product_id,
        "period": period,
        "forecast": forecast,
        "units": units,
        "message": f"Mock forecast for {product_id} for {period} is {forecast} {units}."
    })

@app.route('/mock-reorder-point', methods=['GET'])
def mock_reorder_point():
    product_id = request.args.get('product_id', 'unknown product')

    # Simple mock logic
    if "bolt" in product_id.lower():
        reorder_point = 300
    elif "nut" in product_id.lower():
        reorder_point = 400
    else:
        reorder_point = 200

    return jsonify({
        "product_id": product_id,
        "reorder_point": reorder_point,
        "message": f"Mock reorder point for {product_id} is {reorder_point} units."
    })

@app.route('/mock-risk-assessment', methods=['GET'])
def mock_risk_assessment():
    product_id = request.args.get('product_id', 'unknown product')

    # Simple mock logic
    if "critical" in product_id.lower():
        risk_level = "High"
        details = "Critical item with fluctuating supply."
    elif "bolt" in product_id.lower():
        risk_level = "Medium"
        details = "Standard item, monitor seasonal peaks."
    else:
        risk_level = "Low"
        details = "Stable supply and demand."

    return jsonify({
        "product_id": product_id,
        "risk_level": risk_level,
        "details": details,
        "message": f"Mock risk assessment for {product_id}: {risk_level}. Details: {details}"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000) # Runs on http://127.0.0.1:5000