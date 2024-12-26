document.addEventListener('DOMContentLoaded', () => {
    // Gọi API để lấy danh sách người dùng
    fetchUsers();
});
// Hàm fetch để lấy dữ liệu người dùng từ API backend
async function fetchUsers() {
    try {
        // Gọi API mới với phương thức GET
        const response = await fetch('/search/all/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const users = await response.json();

        // Gọi hàm để hiển thị dữ liệu vào bảng
        displayUsers(users);
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}
// Hàm hiển thị dữ liệu vào bảng
function displayUsers(users) {
    const tableBody = document.querySelector('#users .user-list table tbody');
    // Xóa dữ liệu cũ trong bảng (nếu có)
    tableBody.innerHTML = '';
    // Duyệt qua danh sách người dùng và tạo các dòng bảng
    users.forEach(user => {
        const row = document.createElement('tr');
        // Tạo các cột trong bảng
        const idCell = document.createElement('td');
        idCell.textContent = user.id;
        const nameCell = document.createElement('td');
        nameCell.textContent = user.fullname;

        const accountCell = document.createElement('td');
        accountCell.textContent = user.username;

        const emailCell = document.createElement('td');
        emailCell.textContent = user.email;

        const roleCell = document.createElement('td');
        roleCell.textContent = user.role_id;
        // Thêm các cột vào dòng
        row.appendChild(idCell);
        row.appendChild(nameCell);
        row.appendChild(accountCell);
        row.appendChild(emailCell);
        row.appendChild(roleCell);

        // Thêm dòng vào bảng
        tableBody.appendChild(row);
    });
}
