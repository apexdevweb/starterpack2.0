from flask import Blueprint, render_template, request, jsonify

recettes_bp = Blueprint('recettes', __name__)

# Base de données simple d'exemples de recettes
RECETTES = {
    'tomate': ['Salade tomate-mozzarella', 'Soupe de tomates', 'Pâtes à la sauce tomate'],
    'pomme': ['Tarte aux pommes', 'Compote de pommes', 'Smoothie pomme-banane'],
    'poulet': ['Poulet rôti', 'Curry de poulet', 'Salade de poulet'],
    'chocolat': ['Mousse au chocolat', 'Brownies', 'Fondue au chocolat']
}

@recettes_bp.route('/')
def index():
    return render_template('index.html')

@recettes_bp.route('/recette', methods=['POST'])
def recette():
    ingredient = request.form.get('ingredient', '').lower()
    
    suggestions = RECETTES.get(ingredient, [f"Désolé, aucune recette trouvée pour '{ingredient}'"])
    
    return jsonify({'suggestions': suggestions})