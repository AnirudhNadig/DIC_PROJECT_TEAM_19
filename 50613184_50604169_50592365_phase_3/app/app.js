document.getElementById('recommendForm').addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent default form submission

    // Get input values
    const skinType = document.getElementById('skinType').value;
    const budget = document.getElementById('budget').value;
    const primaryCategory = document.getElementById('primaryCategory').value;
    const subCategory = document.getElementById('subCategory').value;
    const label = document.getElementById('label').value;

    // Validate budget
    if (!budget || parseInt(budget) <= 0) {
        alert('Please enter a valid budget greater than 0.');
        return;
    }

    // Prepare the request payload
    const payload = {
        skin_type: skinType,
        budget: parseFloat(budget),
        primary_category: primaryCategory,
        sub_category: subCategory,
        label: label
    };

    try {
        // Call the Flask API deployed on Fly.io
        const response = await fetch('https://dic-project.fly.dev/recommend', { // Update API URL
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        // Handle response
        if (response.ok) {
            const data = await response.json();
            displayResults(data);
        } else {
            const error = await response.json();
            alert(error.error || 'An error occurred. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please check the console for details.');
    }
});

// Function to display recommendations in the table
function displayResults(recommendations) {
    const tableBody = document.getElementById('resultsTable').querySelector('tbody');
    tableBody.innerHTML = ''; // Clear existing results

    recommendations.forEach((rec) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${rec.ProductName}</td>
            <td>${rec.PrimaryCategory}</td>
            <td>${rec.SubCategory}</td>
            <td>${rec.Label}</td>
            <td>${rec.Rank.toFixed(2)}</td>
            <td>$${rec.Price.toFixed(2)}</td>
        `;
        tableBody.appendChild(row);
    });
}
