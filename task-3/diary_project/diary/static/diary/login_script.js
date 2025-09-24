const form = document.getElementById('loginForm');
const errorMsg = document.getElementById('errorMsg');

form.addEventListener('submit', function(event) {

    const username = form.username.value.trim();
    const password = form.password.value.trim();

    // Example validation logic
    if (username === "" || password === "") {
        errorMsg.textContent = "Both fields are required.";
        errorMsg.classList.remove('hidden');
        return;
    }

    if (username !== "user" || password !== "password") {
        errorMsg.textContent = "Invalid credentials.";
        errorMsg.classList.remove('hidden');
        return;
    }

    errorMsg.classList.add('hidden');
    alert("Login successful!");
   
});
