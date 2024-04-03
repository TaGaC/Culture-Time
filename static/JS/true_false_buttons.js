const trueButton = document.getElementById('true-button');
const falseButton = document.getElementById('false-button');
const explanationDiv = document.getElementById('explanation');
const answerMessageDiv = document.getElementById('answer-message');

function setAnswer(value) {
    document.getElementById('answer').value = value;
}

// Replace this with the correct answer for the question
const correctAnswer = '{{ bonne_reponse }}';  // Remplacer '{{ bonne_reponse }}' par la bonne réponse depuis Flask

// Add event listeners to the buttons
trueButton.addEventListener('click', () => {
    const chosenAnswer = '{{ reponses[0] }}';  // Remplacer '{{ reponses[0] }}' par la première réponse depuis Flask
    if (chosenAnswer === correctAnswer) {
        trueButton.classList.add('bg-green-700');
        falseButton.classList.add('bg-red-700');
        answerMessageDiv.innerText = "Correct!";
    } else {
        trueButton.classList.add('bg-red-700');
        falseButton.classList.add('bg-green-700');
        answerMessageDiv.innerText = "Incorrect!";
    }
    explanationDiv.classList.remove('hidden');
});

falseButton.addEventListener('click', () => {
    const chosenAnswer = '{{ reponses[1] }}';  // Remplacer '{{ reponses[1] }}' par la deuxième réponse depuis Flask
    if (chosenAnswer === correctAnswer) {
        falseButton.classList.add('bg-green-700');
        trueButton.classList.add('bg-red-700');
        answerMessageDiv.innerText = "Correct!";
    } else {
        falseButton.classList.add('bg-red-700');
        trueButton.classList.add('bg-green-700');
        answerMessageDiv.innerText = "Incorrect!";
    }
    explanationDiv.classList.remove('hidden');
});
