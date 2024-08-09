from flask import Flask
from routes.auth import auth_blueprint
from routes.ai import ai_blueprint
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Реєстрація blueprint'ів
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(ai_blueprint, url_prefix='/ai')

if __name__ == "__main__":
    app.run(debug=True)


