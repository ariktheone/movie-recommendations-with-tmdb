document.getElementById('movieForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    fetch('/recommendations', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('recommendations').innerHTML = data;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('recommendations').innerHTML = '<p class="error">An error occurred while fetching recommendations. Please try again.</p>';
    });
});

function showDetails(title) {
    var details = document.getElementById('details-' + title);
    if (details) {
        details.classList.remove('hidden');
        details.style.zIndex = 1000; // Ensure the details box is above other elements

        // Adjust position based on screen orientation
        var container = details.parentElement;
        var containerRect = container.getBoundingClientRect();
        var detailsRect = details.getBoundingClientRect();

        // Default position
        details.style.left = '170px';
        details.style.right = 'auto';

        // Adjust if the box overflows the right side of the screen
        if (containerRect.right + detailsRect.width > window.innerWidth) {
            details.style.left = 'auto';
            details.style.right = '170px';
        }
    }
}

function hideDetails(title) {
    var details = document.getElementById('details-' + title);
    if (details) {
        details.classList.add('hidden');
        details.style.zIndex = 'auto'; // Reset z-index to default
    }
}

// Close modal if clicked outside
window.onclick = function(event) {
    var modal = document.getElementById('movieModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

