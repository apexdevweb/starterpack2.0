async function envoyerIngredient() {
    const ingredient = document.getElementById('user_question').value;
    
    const response = await fetch('/recette', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `user_question=${ingredient}`
    });
    
    const data = await response.json();
    const liste = document.getElementById('Ai_response');
    liste.innerHTML = '';
    data.suggestions.forEach(recette => {
        const li = document.createElement('li');
        li.textContent = recette;
        liste.appendChild(li);
    });
}