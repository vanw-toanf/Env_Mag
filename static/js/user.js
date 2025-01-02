 // Mở modal để thêm công trình
 function openAddUserModal() {
    document.getElementById('addUserModal').style.display = "block";
}

    // Đóng modal
function closeAddUserModal() {
    document.getElementById('addUserModal').style.display = "none";
}

// Thêm công trình mới
document.getElementById('addUserForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Ngăn không cho form gửi
    console.log("Submit form"); // Để theo dõi xem có gọi đến không

    // Lấy giá trị từ form
    const userName = document.getElementById('user_name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const role = document.getElementById('capacity').value;

    // Kiểm tra các giá trị đã được lấy
    console.log(userName, email, phone, role);

    // Thêm công trình vào mảng
    const newUser = {
        id: user.length + 1,
        user_name: userName,
        email: email,
        phone: phone,
        created_at: new Date(),
        role: role,
    };
    user.push(newUser);

    // Cập nhật bảng
    searchUser(); // Cập nhật lại danh sách công trình

    // Đóng modal sau khi thêm thành công
    closeAddUserModal();
});





// Tìm kiếm công trình
function searchProjects() {
const searchInput = document.getElementById('search-input').value.toLowerCase().trim();
const tbody = document.getElementById('project-tbody');

// Xóa các hàng cũ
tbody.innerHTML = '';

// Kiểm tra nếu giá trị tìm kiếm là số (cho trường hợp tìm ID)
const isNumeric = !isNaN(searchInput) && searchInput !== '';
const isDate = !isNaN(Date.parse(searchInput)); // Kiểm tra nếu giá trị tìm kiếm là ngày

// Lọc và hiển thị công trình dựa trên nhiều tiêu chí
projects
    .filter(project => {
        if (isNumeric) {
            // Tìm theo ID
            return project.id.toString() === searchInput;
        } else if (isDate) {
            // Tìm theo ngày tạo
            return new Date(project.created_at).toLocaleDateString().includes(searchInput);
        } else {
            // Tìm theo tên công trình hoặc địa điểm
            return project.project_name.toLowerCase().includes(searchInput) || 
                   project.location.toLowerCase().includes(searchInput);
        }
    })
    .forEach(project => {
        const row = `<tr>
            <td>${project.id}</td>
            <td>${project.project_name}</td>
            <td>${project.location}</td>
            <td>${project.status}</td>
            <td>${new Date(project.created_at).toLocaleDateString()}</td>
            <td>${project.capacity}</td>
            <td>
                <button class="edit-btn" onclick="editProject(${project.id})">Sửa</button>
                <button class="delete-btn" onclick="deleteProject(${project.id})">Xóa</button>
            </td>
        </tr>`;
        tbody.innerHTML += row;
    });
}


// Gọi hàm tìm kiếm khi trang được tải để hiển thị tất cả công trình
    searchProjects();

// Đăng ký sự kiện cho ô tìm kiếm
    document.getElementById('search-input').addEventListener('input', searchProjects);