document.addEventListener('DOMContentLoaded', function() {
    fetchHistory();
});
async function fetchHistory() {
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
        const histories = await response.json();
        displayHistory(histories); // hien thi du lieu len table 
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}  
function displayHistory(histories) {
    const tableBody = document.querySelector('#history .list table tbody');
    tableBody.innerHTML = '';
    histories.forEach(history => {
        const row = history.createElement('tr');

        const userIDCell = history.createElement('td');
        userIDCell.textContent = history.user_id;
        const logintimeCell = history.createElement('td');
        logintimeCell.textContent = history.login_time;
        const ipCell = history.createElement('td');
        ipCell.textContent = history.ip_address;

        row.appendChild(userIDCell);
        row.appendChild(logintimeCell);
        row.appendChild(ipCell);

        tableBody.appendChild(row);
    });
}