from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and columns
model = joblib.load('bengaluru_price_model.pkl')
model_columns = joblib.load('model_columns.pkl')

# Extract location list
location_columns = sorted([col for col in model_columns if col not in ['total_sqft', 'bath', 'bhk']])

@app.route('/')
def home():
    return render_template('index.html', locations=location_columns)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        total_sqft = float(request.form['total_sqft'])
        bath = int(request.form['bath'])
        bhk = int(request.form['bhk'])
        location = request.form['location']

        # Create DataFrame with model columns
        input_data = pd.DataFrame([[0]*len(model_columns)], columns=model_columns)
        input_data.at[0, 'total_sqft'] = total_sqft
        input_data.at[0, 'bath'] = bath
        input_data.at[0, 'bhk'] = bhk

        if location in model_columns:
            input_data.at[0, location] = 1

        predicted_price = model.predict(input_data)[0]

        # Avoid negative values
        if predicted_price < 0:
            predicted_price = abs(predicted_price)

        return render_template(
            'index.html',
            prediction_text=f"💰 Estimated Price: ₹ {round(predicted_price, 2)} Lakhs",
            locations=location_columns
        )
    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f"⚠️ Error: {str(e)}",
            locations=location_columns
        )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
