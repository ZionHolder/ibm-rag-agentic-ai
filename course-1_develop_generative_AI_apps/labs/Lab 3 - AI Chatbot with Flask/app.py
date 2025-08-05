from flask import Flask, request, jsonify, render_template
from model import llama3_response, granite_response, mixtral_response
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])

def generate():
    data = request.json
    user_message = data.get('message')
    model = data.get('model')

    if not user_message or not model:
        return jsonify({"error": "Missing message or model selection"}), 400

    system_prompt = "You are an AI assistant helping with customer inquiries. Provide a helpful and concise repsonse."

    start_time = time.time()

    try:
        if model == 'llama3':
            result = llama3_response(system_prompt, user_message)
        elif model == 'granite':
            result = granite_response(system_prompt, user_message)
        elif model == 'mixtral':
            result = mixtral_response(system_prompt, user_message)
        else:
            return jsonify({"error": "Invalid model selecction"}), 400

        result['duration'] = time.time() - start_time
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


# Next steps
# To further enhance your skills and application:

# Implement caching: Add a caching mechanism to improve performance for repeated queries.

# Explore advanced LangChain features: Look into features like memory for maintaining conversation context.

# Add more models: Try integrating other models available through watsonx.ai.

# Implement A/B testing: Create a system to compare responses from different models for the same query.

# Enhance error handling: Implement more robust error handling and logging.

# Explore IBM Cloud services: Consider integrating other IBM Cloud services to expand your application's capabilities.