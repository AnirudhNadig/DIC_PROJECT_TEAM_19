document.getElementById('recommendForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const skinType = document.getElementById('skinType').value;
    const budget = document.getElementById('budget').value;
    const primaryCategory = document.getElementById('primaryCategory').value;
    const subCategory = document.getElementById('subCategory').value;
    const label = document.getElementById('label').value;

    if (!budget || parseInt(budget) <= 0) {
        alert('Please enter a valid budget greater than 0.');
        return;
    }

    const payload = {
        skin_type: skinType,
        budget: parseFloat(budget),
        primary_category: primaryCategory,
        sub_category: subCategory,
        label: label
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/recommend', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

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

function displayResults(recommendations) {
    const tableBody = document.getElementById('resultsTable').querySelector('tbody');
    tableBody.innerHTML = '';

    if (!recommendations.length) {
        const row = document.createElement('tr');
        row.innerHTML = '<td colspan="6">No recommendations found.</td>';
        tableBody.appendChild(row);
        return;
    }

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