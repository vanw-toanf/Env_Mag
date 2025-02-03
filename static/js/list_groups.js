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
        groups = await response.json();
        renderTableGroup(groups); // hien thi du lieu len table 
    } catch (error) {
        console.error('Có lỗi khi lấy dữ liệu:', error);
    }
}

function renderTableGroup(data) {
    const tableBody2 = document.getElementById("tableBodyGroup");
    tableBody2.innerHTML = ""; // Xóa nội dung bảng trước khi cập nhật

    if (data.length === 0) {
        tableBody2.innerHTML = '<tr><td colspan="5">Không tìm thấy kết quả phù hợp.</td></tr>';
    } else {
        data.forEach(group => {
            const row = document.createElement('tr');

            row.innerHTML = `
                <td>${group.id}</td>
                <td>${group.group_name}</td>
                <td>${group.description}</td>
            `;

            tableBody2.appendChild(row);
        });
    }
}

function searchGroups() {
    const query = document.getElementById("searchInput").value.trim().toLowerCase();
    const filteredData = groups.filter(group =>
        group.group_name.toLowerCase().includes(query) ||
        group.description.toLowerCase().includes(query)
    );
    renderTableGroup(filteredData);
}



function openAddGroupModal() {
    document.getElementById("addGroupModal").style.display = "block";
}
  
// Đóng modal thêm người dùng
function closeAddGroupModal() {
    document.getElementById("addGroupModal").style.display = "none";
}

// Thêm người dùng mới vào database
document.getElementById("addGroupForm").addEventListener("submit", function (event) {
    // event.preventDefault(); // Ngăn không cho form gửi
    // console.log("Submit form"); // Để theo dõi xem có gọi đến không

    // Lấy giá trị từ form
    const groupname = document.getElementById("group_name").value;
    const descriptions = document.getElementById("description").value;

    // Cập nhật dữ liệu vào database 
    const newGroup = {
        group_name: groupname,
        description: descriptions
    };

    // Gửi dữ liệu người dùng mới lên server
    fetch("/create_group/new_group", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(newGroup),
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

    searchGroups(); // Cập nhật lại danh sách người dùng
    fetchGroups();

    closeAddGroupModal();
});