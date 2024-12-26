document.addEventListener('DOMContentLoaded', function() {
    fetchDocuments();
});
async function fetchDocuments() {
    try {
        const response = await fetch('/statistic/documents/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const documents = await response.json();
        displayDocuments(documents); // hien thi du lieu len table 
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}
function displayDocuments(documents) {
    const tableBody = document.querySelector('#written-regulations .doc-list table tbody');
    tableBody.innerHTML = '';
    documents.forEach(document => {
        const row = document.createElement('tr');

        const titleCell = document.createElement('td');
        titleCell.textContent = document.title;
        const fileCell = document.createElement('td');
        fileCell.textContent = document.file;

        row.appendChild(titleCell);
        row.appendChild(fileCell);

        tableBody.appendChild(row);
    });
}