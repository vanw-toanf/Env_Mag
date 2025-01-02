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
    const tableBody = document.querySelector('.user-list table tbody');
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

// document.addEventListener('DOMContentLoaded', () => {
//     const allUsersButton = document.querySelector('#allUsersButton');
//     const searchButton = document.querySelector('#searchButton');
//     const usernameInput = document.querySelector('#searchInput');

//     // Hiển thị toàn bộ người dùng khi nhấn nút "Hiển thị tất cả"
//     allUsersButton.addEventListener('click', fetchAllUsers);

//     // Tìm kiếm người dùng khi nhấn nút "Tìm kiếm"
//     searchButton.addEventListener('click', () => {
//         const username = usernameInput.value.trim();
//         if (username) {
//             fetchUserByUsername(username);
//         } else {
//             alert("Vui lòng nhập tên người dùng để tìm kiếm.");
//         }
//     });

//     // Hiển thị toàn bộ người dùng mặc định khi tải trang
//     fetchAllUsers();
// });

// // Hàm lấy tất cả người dùng
// async function fetchAllUsers() {
//     try {
//         const response = await fetch('/search/all/', {
//             method: 'GET',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//         });

//         if (!response.ok) {
//             throw new Error(`HTTP error! status: ${response.status}`);
//         }

//         const users = await response.json();
//         displayUsers(users);
//     } catch (error) {
//         console.error('Có lỗi khi lấy dữ liệu:', error);
//     }
// }

// // Hàm tìm kiếm người dùng theo username
// async function fetchUserByUsername(username) {
//     try {
//         const response = await fetch(`/search/user/${username}`, {
//             method: 'GET',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//         });

//         if (!response.ok) {
//             throw new Error(`HTTP error! status: ${response.status}`);
//         }

//         const user = await response.json();
//         displayUsers([user]); // Hiển thị một người dùng dưới dạng danh sách
//     } catch (error) {
//         console.error('Có lỗi khi lấy dữ liệu:', error);
//         alert('Không tìm thấy người dùng hoặc có lỗi xảy ra.');
//     }
// }

// // Hàm hiển thị danh sách người dùng
// function displayUsers(users) {
//     const tableBody = document.querySelector('#users .user-list table tbody');
//     tableBody.innerHTML = ''; // Xóa dữ liệu cũ trong bảng

//     if (users.length > 0) {
//         users.forEach(user => {
//             const row = document.createElement('tr');
//             const idCell = document.createElement('td');
//             idCell.textContent = user.id;
//             const nameCell = document.createElement('td');
//             nameCell.textContent = user.fullname;
//             const accountCell = document.createElement('td');
//             accountCell.textContent = user.username;
//             const emailCell = document.createElement('td');
//             emailCell.textContent = user.email;
//             const roleCell = document.createElement('td');
//             roleCell.textContent = user.role_id;

//             row.appendChild(idCell);
//             row.appendChild(nameCell);
//             row.appendChild(accountCell);
//             row.appendChild(emailCell);
//             row.appendChild(roleCell);

//             tableBody.appendChild(row);
//         });
//     } else {
//         const row = document.createElement('tr');
//         const noDataCell = document.createElement('td');
//         noDataCell.setAttribute('colspan', '5');
//         noDataCell.textContent = 'Không tìm thấy người dùng.';
//         row.appendChild(noDataCell);
//         tableBody.appendChild(row);
//     }
// }