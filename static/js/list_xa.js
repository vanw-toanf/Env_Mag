document.addEventListener('DOMContentLoaded', () => {
    fetchXa();
});
async function fetchXa() {
    try {
        const response = await fetch('/statistic/xa/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const xa = await response.json();
        displayXa(xa); // hien thi du lieu len table 
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}
function displayXa(xa){
    const tableBody = document.querySelector('#xa .list table tbody');
    tableBody.innerHTML = '';
    xa.forEach(xa => {
        const row = document.createElement('tr');

        const idCell = document.createElement('td');
        idCell.textContent = xa.id
        const nameCell = document.createElement('td');
        nameCell.textContent = xa.name;
        const codeCell = document.createElement('td');
        codeCell.textContent = xa.code;

        row.appendChild(idCell);
        row.appendChild(nameCell);
        row.appendChild(codeCell);

        tableBody.appendChild(row);
    });
}