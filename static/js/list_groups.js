document.addEventListener('DOMContentLoaded', () => {
    fetchGroups();
});
async function fetchGroups() {
    try {
        const response = await fetch('/search/group/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const groups = await response.json();
        displayGroups(groups); // hien thi du lieu len table 
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}

function displayGroups(groups) {
    const tableBody = document.querySelector('#group .user-list table tbody');
    tableBody.innerHTML = '';
    groups.forEach((group,index) => {
        const row = document.createElement('tr');

        const sttCell = document.createElement('td');
        sttCell.textContent = index + 1; // STT bắt đầu từ 1

        const nameCell = document.createElement('td');
        nameCell.textContent = group.group_name;
        const descriptionCell = document.createElement('td');
        descriptionCell.textContent = group.description;

        row.appendChild(sttCell);
        row.appendChild(nameCell);
        row.appendChild(descriptionCell);

        tableBody.appendChild(row);
    });
}