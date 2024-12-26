
function showSection(sectionId) {
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => {
        section.classList.remove('active');
    });

    const selectedSection = document.getElementById(sectionId);
    selectedSection.classList.add('active');
}

window.onload = function() {
    showSection('users');
};



        // Mảng mẫu dữ liệu công trình nước
    const projects = [
        { id: 1, project_name: 'Công trình dưới nước', location: 'Hà Nội', status: 'Công trình nước tập trung 1', created_at: new Date(), capacity: '100%'  },
        { id: 2, project_name: 'Công trình trên cạn', location: 'Hải Phòng', status: 'Công trình nước phân tán 2', created_at: new Date(), capacity: '100%' },
        { id: 3, project_name: 'Công trình trên không', location: 'Đà Nẵng', status: 'Công trình nước tập trung 3', created_at: new Date(), capacity: '100%' },
        { id: 4, project_name: 'Công trình hư không', location: 'Cần Thơ', status: 'Công trình nước phân tán 4', created_at: new Date(), capacity: '100%' },
    ];

        // Mở modal để thêm công trình
    function openAddProjectModal() {
        document.getElementById('addProjectModal').style.display = "block";
    }

        // Đóng modal
    function closeAddProjectModal() {
        document.getElementById('addProjectModal').style.display = "none";
    }

    // Thêm công trình mới
    document.getElementById('addProjectForm').addEventListener('submit', function (event) {
        event.preventDefault(); // Ngăn không cho form gửi
        console.log("Submit form"); // Để theo dõi xem có gọi đến không
    
        // Lấy giá trị từ form
        const projectName = document.getElementById('project_name').value;
        const location = document.getElementById('location').value;
        const status = document.getElementById('status').value;
        const capacity = document.getElementById('capacity').value;
    
        // Kiểm tra các giá trị đã được lấy
        console.log(projectName, location, status, capacity);
    
        // Thêm công trình vào mảng
        const newProject = {
            id: projects.length + 1,
            project_name: projectName,
            location: location,
            status: status,
            created_at: new Date(),
            capacity: capacity,
        };
        projects.push(newProject);
    
        // Cập nhật bảng
        searchProjects(); // Cập nhật lại danh sách công trình
    
        // Đóng modal sau khi thêm thành công
        closeAddProjectModal();
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


