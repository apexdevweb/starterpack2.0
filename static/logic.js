document.addEventListener("DOMContentLoaded", () => {
    const texteIntro = "Bonjour je suis Solline l'intélligence artificiel culinaire qui vas vous assister dans la découverte du restaurant";
    const elementIntro = document.getElementById("intro_texte");

    afficherLettreParLettre(elementIntro, texteIntro, 35);
});


async function envoyerQuestion() {
    const ingredient = document.getElementById('user_question').value.trim();
    if (!ingredient) return alert("Veuillez entrer un ingrédient !");
    
    const response = await fetch('/recette', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `user_question=${encodeURIComponent(ingredient)}`
    });

    const data = await response.json();
    const liste = document.getElementById('Ai_response');
    liste.innerHTML = ''; // On efface les anciennes réponses

    if (data.suggestions && data.suggestions.length > 0) {
        for (const recette of data.suggestions) {
            const li = document.createElement('li');
            liste.appendChild(li);
            await afficherLettreParLettre(li, recette); // Animation ici ✨
        }
    } else {
        const li = document.createElement('li');
        await afficherLettreParLettre(li, "Aucune recette trouvée.");
        liste.appendChild(li);
    }
}

/**
 * Affiche un texte lettre par lettre dans un élément HTML
 * @param {HTMLElement} element - L’élément dans lequel écrire
 * @param {string} texte - Le texte à afficher
 */
 function afficherLettreParLettre(element, texte, vitesse = 40) {
    return new Promise(resolve => {
        let index = 0;
        element.textContent = ''; // réinitialiser avant d'écrire
        const interval = setInterval(() => {
            element.textContent += texte[index];
            index++;

            if (index >= texte.length) {
                clearInterval(interval);
                resolve();
            }
        }, vitesse);
    });
}