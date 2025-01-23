document.querySelector('form').addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent the form from submitting normally

    const fileInput = document.querySelector('#file');
    const errorMessage = document.getElementById('error-message');

    // Check if the file is CSV
    if (fileInput.files[0] && !fileInput.files[0].name.endsWith('.csv')) {
        errorMessage.style.display = 'block'; // Show the error message
        return; // Prevent form submission if the file type is incorrect
    } else {
        errorMessage.style.display = 'none'; // Hide the error message if the file is valid
    }

    // Create a FormData object with the form data
    const formData = new FormData(e.target);

    try {
        // Send the form data using fetch
        const response = await fetch('/api/upload/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        });

        const data = await response.json();

        // Display the response data in the #response div
        if (data.error) {
            document.querySelector('#response').innerText = data.error;
        } else {
            document.querySelector('#response').innerText = JSON.stringify(data, null, 2);
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
