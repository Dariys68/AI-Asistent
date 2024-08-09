from flask import Blueprint, request, jsonify
from models.model import create_model

ai_blueprint = Blueprint('ai', __name__)

# Глобальний стан моделі (для простоти прикладу)
model = create_model((784,))

@ai_blueprint.route('/train', methods=['POST'])
def train_model():
    data = request.get_json()
    x_train, y_train = data.get('x_train'), data.get('y_train')
    model.fit(x_train, y_train, epochs=5)
    return jsonify({"message": "Model trained successfully!"})

@ai_blueprint.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    x_input = data.get('x_input')
    prediction = model.predict(x_input)
    return jsonify({"prediction": prediction.tolist()})
