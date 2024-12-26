document.addEventListener("DOMContentLoaded", function () {
    const loginButtonAdmin = document.querySelector(".login-button button:nth-child(1)");
    const loginButtonGuest = document.querySelector(".login-button button:nth-child(2)");
    const accountInput = document.querySelector(".account");
    const passwordInput = document.querySelector(".password");

    // Hàm xử lý đăng nhập
    async function handleLogin(role_id) {
        const username = accountInput.value;
        const password = passwordInput.value;

        // Kiểm tra xem các trường có được điền hay không
        if (!username || !password) {
            alert("Vui lòng nhập tài khoản và mật khẩu.");
            return;
        }

        // Gửi yêu cầu đăng nhập
        try {
            const response = await fetch('/login/verify/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: username,
                    password: password,
                    role_id: role_id
                }),
            });

            // Kiểm tra phản hồi từ server
            if (response.ok) {
                const data = await response.json();
                alert(data.message); // Thông báo đăng nhập thành công
                window.location.href = '/home'; // Chuyển hướng đến trang home
            } else {
                const errorData = await response.json();
                alert(errorData.detail); // Thông báo lỗi
            }
        } catch (error) {
            console.error("Error during login:", error);
            alert("Đã xảy ra lỗi, vui lòng thử lại sau.");
        }
    }

    // Sự kiện cho nút đăng nhập quản trị viên
    loginButtonAdmin.addEventListener("click", () => handleLogin(1)); // role_id của quản trị viên là 1

    // Sự kiện cho nút đăng nhập khách
    loginButtonGuest.addEventListener("click", () => handleLogin(2)); //role_id của khách là 2
});

window.onload = function() {
    resetForm();
};
