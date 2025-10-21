from flask import Blueprint, render_template, request, jsonify

recettes_bp = Blueprint('recettes', __name__)

# Base de données simple d'exemples de recettes
# backend/logic.py

RECETTES = {
    'tomate': ['Salade tomate-mozzarella', 'Soupe de tomates', 'Pâtes à la sauce tomate'],
    'pomme': ['Tarte aux pommes', 'Compote de pommes', 'Smoothie pomme-banane'],
    'poulet': ['Poulet rôti', 'Curry de poulet', 'Salade de poulet'],
    'chocolat': ['Mousse au chocolat', 'Brownies', 'Fondue au chocolat']
}

def obtenir_recettes(ingredient):
    """Retourne une liste de recettes correspondant à l'ingrédient."""
    ingredient = ingredient.lower()
    return RECETTES.get(ingredient, [f"Désolé, aucune recette trouvée pour '{ingredient}'"])
