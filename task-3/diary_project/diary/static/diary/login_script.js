document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('loginForm'); 
    const errorMsg = document.getElementById('errorMsg'); 

    form.addEventListener('submit', async function(event) {
        event.preventDefault(); 

        const username = form.username.value.trim();
        const password = form.password.value.trim();

        if (!username || !password) {
            errorMsg.textContent = "Both fields are required.";
            errorMsg.classList.remove('hidden');
            return;
        }

        const response = await fetch('/login_user/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();
        if (data.success) {
            window.location.href = '/home/';
        } else {
            errorMsg.textContent = data.error;
            errorMsg.classList.remove('hidden');
        }
    });
});
