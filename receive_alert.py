from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("🚨 تنبيه جديد من TradingView:")
    print(data)
    return jsonify({"status": "تم الاستلام"}), 200

if __name__ == '__main__':
    app.run()
