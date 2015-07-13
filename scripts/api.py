from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/api/vehicles")
def vehicles():
    """
    TODO: More data, please
    """
    data = {
        1234: {
            'make': 'BMW',
            'model': '3-series',
            'price': 40000,
            'image': 'http://www.digitaltrends.com/wp-content/uploads/2013/02/bmw-3-series-gt-leak-2_1035.jpg'
        },
        5678: {
            'make': 'Mazda',
            'model': 'Miata',
            'price': 25000,
            'image': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/2011_Mazda_MX-5_PRHT_--_04-28-2011.jpg'
        }
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
