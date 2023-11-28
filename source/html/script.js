// Génération d'un nombre aléatoire entre 1 et 100
const randomNumber = Math.floor(Math.random() * 100) + 1;

// Variable pour stocker le nombre de tentatives
let attempts = 0;

// Fonction pour démarrer le jeu
function startGame() {
  const guessInput = document.getElementById('guessInput');
  const result = document.getElementById('result');
  
  // Récupère la valeur de l'entrée
  const userGuess = parseInt(guessInput.value);

  // Vérifie si le nombre est valide
  if (isNaN(userGuess)) {
    result.textContent = 'Veuillez entrer un nombre valide.';
    return;
  }

  // Incrémente le nombre de tentatives
  attempts++;

  // Vérifie si le nombre est correct
  if (userGuess === randomNumber) {
    result.textContent = `Bravo! Vous avez deviné le nombre en ${attempts} tentative(s)!`;
  } else if (userGuess < randomNumber) {
    result.textContent = 'Le nombre est plus grand. Essayez encore.';
  } else {
    result.textContent = 'Le nombre est plus petit. Essayez encore.';
  }

  // Efface la valeur de l'entrée
  guessInput.value = '';
}
