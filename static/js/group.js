 // Mở modal để thêm công trình
 function openAddGroupModal() {
    document.getElementById('addGroupModal').style.display = "block";
}

    // Đóng modal
function closeAddGroupModal() {
    document.getElementById('addGroupModal').style.display = "none";
}

// Thêm công trình mới
document.getElementById('addGroupForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Ngăn không cho form gửi
    console.log("Submit form"); // Để theo dõi xem có gọi đến không

    // Lấy giá trị từ form
    const groupName = document.getElementById('group_name').value;
    const describe = document.getElementById('describe').value;


    // Kiểm tra các giá trị đã được lấy
    console.log(groupName, describe);

    // Thêm công trình vào mảng
    const newGroup = {
        id: group.length + 1,
        group_name: userName,
        describe: describe,
    };
    group.push(newGroup);

    // Cập nhật bảng
    searchGroup(); // Cập nhật lại danh sách công trình

    // Đóng modal sau khi thêm thành công
    closeAddGroupModal();
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