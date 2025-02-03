// Mảng dữ liệu gốc (ban đầu trống)
let usersData = [];

document.addEventListener('DOMContentLoaded', () => {
    // Lấy danh sách người dùng từ API khi tải trang
    fetchUsers();
});

// Hàm fetch để lấy dữ liệu người dùng từ API backend
async function fetchUsers() {
    try {
        const response = await fetch('/search/all/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        usersData = await response.json();

        // Hiển thị dữ liệu lên bảng
        renderTable(usersData);
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}

// Hàm hiển thị bảng dữ liệu
function renderTable(data) {
    const tableBody = document.getElementById("tableBody");
    tableBody.innerHTML = ""; // Xóa nội dung bảng trước khi cập nhật

    if (data.length === 0) {
        tableBody.innerHTML = '<tr><td colspan="5">Không tìm thấy kết quả phù hợp.</td></tr>';
    } else {
        data.forEach(user => {
            const row = document.createElement('tr');

            row.innerHTML = `
                <td>${user.id}</td>
                <td>${user.fullname}</td>
                <td>${user.username}</td>
                <td>${user.email}</td>
                <td>${user.role_id}</td>
            `;

            tableBody.appendChild(row);
        });
    }
}

// Hàm tìm kiếm người dùng
function searchUsers() {
    const query = document.getElementById("searchInput").value.trim().toLowerCase();
    const filteredData = usersData.filter(user =>
        user.fullname.toLowerCase().includes(query) ||
        user.username.toLowerCase().includes(query) ||
        user.email.toLowerCase().includes(query)
    );
    renderTable(filteredData);
}


// Mở modal thêm người dùng
function openAddUserModal() {
    document.getElementById("addUserModal").style.display = "block";
}
  
// Đóng modal thêm người dùng
function closeAddUserModal() {
    document.getElementById("addUserModal").style.display = "none";
}

// Thêm người dùng mới vào database
document.getElementById("addUserForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Ngăn không cho form gửi
    // console.log("Submit form"); // Để theo dõi xem có gọi đến không

    // Lấy giá trị từ form
    const fullname = document.getElementById("fullname").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const email = document.getElementById("email").value;
    const role_id = document.getElementById("role").value;

    // Cập nhật dữ liệu vào database 
    const newUser = {
        fullname: fullname,
        username: username,
        password: password,
        email: email,
        role_id: role_id,
    };

    // Gửi dữ liệu người dùng mới lên server
    fetch("/register_user/new_user", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(newUser),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            console.log("Thêm người dùng thành công:", data);
        })
        .catch((error) => {
            console.error("Có lỗi xảy ra:", error);
        });

    // searchUsers(); // Cập nhật lại danh sách người dùng
    fetchUsers();

    closeAddUserModal();
});