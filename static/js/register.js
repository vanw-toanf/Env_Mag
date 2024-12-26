document.getElementById("user-register-btn").addEventListener("click", () => {
    console.log("User Register clicked");
    registerUser("user");
});

document.getElementById("admin-register-btn").addEventListener("click", () => {
    registerUser("admin");
});

function registerUser(role) {
    // Lấy dữ liệu từ form
    const fullname = document.getElementById("fullname").value.trim();
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const confirmPassword = document.getElementById("confirm-password").value.trim();
    const email = document.getElementById("email").value.trim();

    // Kiểm tra mật khẩu nhập lại
    if (password !== confirmPassword) {
        alert("Mật khẩu nhập lại không khớp. Vui lòng kiểm tra lại!");
        return;
    }

    // Chuẩn bị dữ liệu gửi đi
    const requestData = {
        fullname: fullname,
        username: username,
        password: password,
        email: email,
    };

    // Xác định endpoint API
    const endpoint = role === "user" ? "/register_user/new_user" : "/register_user/new_admin";

    // Gửi request tới API
    fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(requestData),
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then((data) => {
        alert("Đăng ký thành công!");
        console.log("Đăng ký thành công:", data);
        window.location.href = "/home";
        // Xóa dữ liệu trong form sau khi đăng ký thành công
        document.getElementById("fullname").value = "";
        document.getElementById("username").value = "";
        document.getElementById("password").value = "";
        document.getElementById("confirm-password").value = "";
        document.getElementById("email").value = "";
    })
    .catch((error) => {
        console.error("Lỗi khi đăng ký:", error);
        alert("Đăng ký thất bại. Vui lòng thử lại!");
    });
}

window.onload = function() {
    resetForm();
};
