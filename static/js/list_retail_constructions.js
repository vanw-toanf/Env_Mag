document.addEventListener('DOMContentLoaded', () => {
    fetchRetailConstructions();
});
async function fetchRetailConstructions() {
    try {
        const response = await fetch('/statistic/water_retail/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const constructions = await response.json();
        displayRetailConstructions(constructions); // hien thi du lieu len table 
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}
function displayRetailConstructions(constructions) {
    const tableBody = document.querySelector('#small-projects .project-list table tbody');
    tableBody.innerHTML = '';
    constructions.forEach((construction,index) => {
        const row = document.createElement('tr');

        const idCell = document.createElement('td');
        idCell.textContent = construction.id
        const nameCell = document.createElement('td');
        nameCell.textContent = construction.name;
        const locationCell = document.createElement('td');
        locationCell.textContent = construction.location;
        const statusCell = document.createElement('td');
        statusCell.textContent = construction.status;
        const yearCell = document.createElement('td');
        yearCell.textContent = construction.construction_year;
        const percentCell = document.createElement('td');
        percentCell.textContent = construction.chi_so_nuoc;

        row.appendChild(idCell);
        row.appendChild(nameCell);
        row.appendChild(locationCell);
        row.appendChild(statusCell);
        row.appendChild(yearCell);
        row.appendChild(percentCell);

        tableBody.appendChild(row);
    });
}