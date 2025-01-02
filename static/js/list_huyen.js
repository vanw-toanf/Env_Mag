document.addEventListener('DOMContentLoaded', () => {
    fetchHuyen();
});
async function fetchHuyen() {
    try {
        const response = await fetch('/statistic/huyen/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const huyen = await response.json();
        displayHuyen(huyen); // hien thi du lieu len table 
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}
function displayHuyen(huyens) {
    const tableBody = document.querySelector('#huyen .list table tbody');
    tableBody.innerHTML = '';
    huyens.forEach(huyen => {
        const row = document.createElement('tr');

        const idCell = document.createElement('td');
        idCell.textContent = huyen.id
        const nameCell = document.createElement('td');
        nameCell.textContent = huyen.name;
        const codeCell = document.createElement('td');
        codeCell.textContent = huyen.code;

        row.appendChild(idCell);
        row.appendChild(nameCell);
        row.appendChild(codeCell);

        tableBody.appendChild(row);
    });
}