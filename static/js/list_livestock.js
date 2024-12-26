document.addEventListener('DOMContentLoaded', () => {
    fetchLivestock();
});
async function fetchLivestock() {
    try {
        const response = await fetch('/statistic/farm_with_condition/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const livestock = await response.json();
        displayLivestock(livestock); // hien thi du lieu len table 
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}
function displayLivestock(livestocks) {
    const tableBody = document.querySelector('#livestock .list table tbody');
    tableBody.innerHTML = '';
    livestocks.forEach(livestock => {
        const row = document.createElement('tr');

        const idCell = document.createElement('td');
        idCell.textContent = livestock.id
        const nameCell = document.createElement('td');
        nameCell.textContent = livestock.name;
        const ownerCell = document.createElement('td');
        ownerCell.textContent = livestock.owner;
        const registerdateCell = document.createElement('td');
        registerdateCell.textContent = livestock.register_date;
        const conditionCell = document.createElement('td');
        conditionCell.textContent = livestock.condition;

        row.appendChild(idCell);
        row.appendChild(nameCell);
        row.appendChild(ownerCell);
        row.appendChild(registerdateCell);
        row.appendChild(conditionCell);

        tableBody.appendChild(row);
    });
}