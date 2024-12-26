document.addEventListener('DOMContentLoaded', function() {
    fetchProcessing();
});
async function fetchProcessing() {
    try {
        const response = await fetch('/statistic/processing/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const processing = await response.json();
        displayProcessing(processing); // hien thi du lieu len table 
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}
function displayProcessing(processings) {
    const tableBody = document.querySelector('#processing-facility .processing-list table tbody');
    tableBody.innerHTML = '';
    processings.forEach((processing,index) => {
        const row = document.createElement('tr');

        const idCell = document.createElement('td');
        idCell.textContent = processing.id
        const nameCell = document.createElement('td');
        nameCell.textContent = processing.processing_name;
        const dateCell = document.createElement('td');
        dateCell.textContent = processing.processing_date;
        const locationCell = document.createElement('td');
        locationCell.textContent = processing.processing_address;
        const productCell = document.createElement('td');
        productCell.textContent = processing.processing_product;

        row.appendChild(idCell);
        row.appendChild(nameCell);
        row.appendChild(dateCell);
        row.appendChild(locationCell);
        row.appendChild(productCell);

        tableBody.appendChild(row);
    });
}