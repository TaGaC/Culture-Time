const trueButton = document.getElementById('true-button');
const falseButton = document.getElementById('false-button');
const explanationDiv = document.getElementById('explanation');
const answerMessageDiv = document.getElementById('answer-message');

function setAnswer(answer, button) {
    const chosenAnswer = answer;
    const correctAnswer = trueButton.getAttribute('data-correct-answer');

    if (chosenAnswer === correctAnswer & button === "trueButton") {
        answerMessageDiv.innerText = "Correct!";
        answerMessageDiv.classList.add('text-green-700'); // Ajouter la classe de couleur verte
        answerMessageDiv.classList.remove('text-red-700'); // Retirer la classe de couleur rouge
        trueButton.classList.add('bg-green-700'); // Ajouter la classe de couleur de fond verte
        falseButton.classList.remove('bg-red-700'); // Retirer la classe de couleur de fond rouge
    }
    if (chosenAnswer === correctAnswer & button === "falseButton") {
        answerMessageDiv.innerText = "Correct!";
        answerMessageDiv.classList.add('text-green-700'); // Ajouter la classe de couleur verte
        answerMessageDiv.classList.remove('text-red-700'); // Retirer la classe de couleur rouge
        falseButton.classList.add('bg-green-700'); // Ajouter la classe de couleur de fond verte
        trueButton.classList.remove('bg-red-700'); // Retirer la classe de couleur de fond rouge
    }
    if (chosenAnswer !== correctAnswer) {
        answerMessageDiv.innerText = "Incorrect!";
        answerMessageDiv.classList.add('text-red-700'); // Ajouter la classe de couleur rouge
        answerMessageDiv.classList.remove('text-green-700'); // Retirer la classe de couleur verte
        if (button === "trueButton") {
            trueButton.classList.add('bg-red-700'); // Ajouter la classe de couleur de fond rouge
            falseButton.classList.add('bg-green-700'); // Retirer la classe de couleur de fond verte
        }
        if (button === "falseButton") {
            falseButton.classList.add('bg-red-700'); // Ajouter la classe de couleur de fond rouge
            trueButton.classList.add('bg-green-700'); // Retirer la classe de couleur de fond verte
        }
    }
    


    
    
    explanationDiv.classList.remove('hidden');
}

trueButton.addEventListener('click', () => {
    const chosenAnswer = trueButton.getAttribute('data-answer');
    setAnswer(chosenAnswer, "trueButton");
});

falseButton.addEventListener('click', () => {
    const chosenAnswer = falseButton.getAttribute('data-answer');
    setAnswer(chosenAnswer, "falseButton");
});
