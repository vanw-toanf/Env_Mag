document.addEventListener('DOMContentLoaded', function() {
    fetchStatus();
});
async function fetchStatus() {
    try {
        const response = await fetch('/statistic/history/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const history = await response.json();
        displayStatus(status); // hien thi du lieu len table 
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}
// cap nhat sau
function displayStatus(status) {
    const tableBody = document.querySelector('#written-regulations .doc-list table tbody'); // se cap nhat sau khi them bang status
    tableBody.innerHTML = '';
    status.forEach(document => {
        const row = document.createElement('tr');

        const userIDCell = document.createElement('td');
        userIDCell.textContent = document.user_id;
        const activeCell = document.createElement('td');
        activeCell.textContent = document.IsActive;
        const lastActiveCell = document.createElement('td');
        lastActiveCell.textContent = document.LastActivity;

        row.appendChild(userIDCell);
        row.appendChild(activeCell);
        row.appendChild(lastActiveCell);

        tableBody.appendChild(row);
    });
}