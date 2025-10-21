from flask import Flask
from routes.recettes import recettes_bp  # Correct

app = Flask(__name__)
app.register_blueprint(recettes_bp)

if __name__ == '__main__':
    app.run(debug=True)