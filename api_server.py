from flask import Flask, request, jsonify
from chatbot_logic import analyze_user_input

# Initialize the Flask application
app = Flask(__name__)

# This is the API endpoint URL.
# It listens for HTTP POST requests at this specific address.
@app.route('/analyze_symptoms', methods=['POST'])
def analyze_symptoms_api():
    try:
        # Get the JSON data from the POST request
        user_answers = request.get_json(force=True)

        # Check if the data is valid
        if not user_answers:
            return jsonify({"error": "No data provided in the request body."}), 400

        # Call your chatbot logic function with the received data
        result = analyze_user_input(user_answers)

        # Return the result as a JSON response
        return jsonify(result)
        
    except Exception as e:
        # Handle any errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# This is the entry point to run the API server
if __name__ == '__main__':
    # Run the Flask app on a local network IP and port 5000
    # The debug=True flag is helpful for development as it reloads the server automatically on code changes
    app.run(host='0.0.0.0', port=5000, debug=True)