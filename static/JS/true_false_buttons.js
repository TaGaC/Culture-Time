const trueButton = document.getElementById('true-button');
const falseButton = document.getElementById('false-button');
const explanationDiv = document.getElementById('explanation');
const answerMessageDiv = document.getElementById('answer-message');

function setAnswer(value) {
    document.getElementById('answer').value = value;
}

// Replace this with the correct answer for the question
const correctAnswer = 'True';  // Remplacer '{{ correct_answer }}' par la bonne réponse depuis Flask

// Add event listeners to the buttons
trueButton.addEventListener('click', () => {
    const chosenAnswer = 'True';
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
    const chosenAnswer = 'False';
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
