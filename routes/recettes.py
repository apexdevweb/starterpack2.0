from flask import Blueprint, render_template, request, jsonify
from backend.logic import obtenir_recettes

recettes_bp = Blueprint('recettes', __name__)

@recettes_bp.route('/')
def index():
    return render_template('index.html')

@recettes_bp.route('/recette', methods=['POST'])
def recette():
    ingredient = request.form.get('user_question', '')
    suggestions = obtenir_recettes(ingredient)
    return jsonify({'suggestions': suggestions})