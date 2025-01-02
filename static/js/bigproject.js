 // Mở modal để thêm công trình
 function openAddBigProjectModal() {
    document.getElementById('addBigProjectModal').style.display = "block";
}

    // Đóng modal
function closeAddBigProjectModal() {
    document.getElementById('addBigProjectModal').style.display = "none";
}

// Thêm công trình mới
document.getElementById('addBigProjectForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Ngăn không cho form gửi
    console.log("Submit form"); // Để theo dõi xem có gọi đến không

    // Lấy giá trị từ form
    const bigprojectName = document.getElementById('bigproject_name').value;
    const b_location = document.getElementById('b_location').value;
    const b_status = document.getElementById('b_status').value;
    const b_capacity = document.getElementById('b_capacity').value;

    // Kiểm tra các giá trị đã được lấy
    console.log(bigprojectName, b_location, b_status, b_capacity);

    // Thêm công trình vào mảng
    const newBigProject = {
        id: projects.length + 1,
        bigproject_name: bigprojectName,
        b_location: b_location,
        b_status: b_status,
        created_at: new Date(),
        b_capacity: b_capacity,
    };
    projects.push(newBigProject);

    // Cập nhật bảng
    searchBigProjects(); // Cập nhật lại danh sách công trình

    // Đóng modal sau khi thêm thành công
    closeAddBigProjectModal();
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