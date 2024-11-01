# from flask import Flask, request, jsonify, render_template
# import pickle

# # Load model and vectorizer
# with open('model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)
# with open('vectorizer.pkl', 'rb') as vectorizer_file:
#     vectorizer = pickle.load(vectorizer_file)

# app = Flask(__name__)

# # Home route with HTML form
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Prediction route
# @app.route('/predict', methods=['POST'])
# def predict():
#     input_text = request.form.get('text')  # Get the input text
    
#     # Check if input is empty
#     if not input_text or input_text.strip() == "":
#         return jsonify({"error": "Input text is required"}), 400  # Return error message

#     # Transform the input text and make prediction
#     input_vector = vectorizer.transform([input_text])
#     prediction = model.predict(input_vector)
   
#     # Map prediction to sentiment label
#     sentiment = "Positive" if prediction[0] == 1 else "Negative" if prediction[0] == -1 else "Neutral"
    
#     # Return JSON response
#     return jsonify({"sentiment": sentiment})

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template
import pickle

# Load the model and vectorizer
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

app = Flask(__name__)

# Home route with HTML form
@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment_result = None  # Variable to hold sentiment result
    input_text = ""

    if request.method == 'POST':
        input_text = request.form.get('text')  # Get the input text
        
        # Check if input is empty
        if not input_text or input_text.strip() == "":
            sentiment_result = "Input text is required."  # Return error message
        else:
            # Transform the input text and make prediction
            input_vector = vectorizer.transform([input_text])
            prediction = model.predict(input_vector)
    
            # Map prediction to sentiment label
            sentiment_result = "Positive" if prediction[0] == 1 else "Negative" if prediction[0] == -1 else "Neutral"
    
    return render_template('index.html', sentiment=sentiment_result, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
