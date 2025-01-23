 // Retrieve data from localStorage
 const data = JSON.parse(localStorage.getItem('uploadResults'));

 if (data) {
     // Populate the template with data from localStorage
     document.getElementById('total-records').innerText = data.total_records;
     document.getElementById('saved-records').innerText = data.saved_records;
     document.getElementById('invalid-records').innerText = data.invalid_records;

     const errorDetailsContainer = document.getElementById('error-details');
     
     // If there are errors, display them
     if (data.errors && data.errors.length > 0) {
         let errorListHtml = '<h2>Rejected Records Details</h2><ul>';
         data.errors.forEach((error) => {
             errorListHtml += `<li class="error-item">
                 <p><strong>Row:</strong> ${JSON.stringify(error.row)}</p>
                 <p><strong>Errors:</strong></p>
                 <ul>`;
             for (const [field, messages] of Object.entries(error.errors)) {
                 errorListHtml += `<li><strong>${field}:</strong> ${messages.join(", ")}</li>`;
             }
             errorListHtml += `</ul></li>`;
         });
         errorListHtml += '</ul>';
         errorDetailsContainer.innerHTML = errorListHtml;
     } else {
         errorDetailsContainer.innerHTML = '<p class="no-errors">No errors in the uploaded file.</p>';
     }
 } else {
     // Handle case where no data is available
     alert('No data found in localStorage.');
 }