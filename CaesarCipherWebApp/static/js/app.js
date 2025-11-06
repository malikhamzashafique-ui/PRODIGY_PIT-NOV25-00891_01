// static/js/app.js

document.addEventListener('DOMContentLoaded', () => {
    const processButton = document.getElementById('process-button');

    const handleProcess = async () => {
        const message = document.getElementById('message').value;
        const shift = document.getElementById('shift').value;
        const mode = document.getElementById('mode').value;
        const resultOutput = document.getElementById('result');
        const errorMessage = document.getElementById('error-message');

        resultOutput.value = '';
        errorMessage.textContent = '';

        const data = { message, shift, mode };

        try {
            const response = await fetch('/process', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });

            const responseData = await response.json();

            if (response.ok) {
                resultOutput.value = responseData.result;
            } else {
                errorMessage.textContent = 'Error: ' + (responseData.error || 'Server issue.');
            }
        } catch (error) {
            errorMessage.textContent = 'Connection Error: Could not reach server.';
            console.error('Fetch error:', error);
        }
    };

    processButton.addEventListener('click', handleProcess);
});
