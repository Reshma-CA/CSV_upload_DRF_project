
document.querySelector('form').addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the form from submitting normally
    const formData = new FormData(e.target);
    
    const response = await fetch('/api/upload/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    });
    const data = await response.json();

    // Display the response
    document.querySelector('#response').innerText = JSON.stringify(data, null, 2);
});
