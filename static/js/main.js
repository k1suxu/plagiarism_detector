document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);

        try {
            const response = await fetch('/check_plagiarism', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            resultDiv.textContent = `Similarity Score: ${data.similarity_score}%`;
        } catch (error) {
            console.error('Error:', error);
            resultDiv.textContent = 'An error occurred. Please try again.';
        }
    });
});