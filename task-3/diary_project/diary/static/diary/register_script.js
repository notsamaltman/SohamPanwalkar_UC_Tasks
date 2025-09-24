const form = document.getElementById("registerForm");

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registerForm');
    const errorMsg = document.getElementById('errorMsg');

    form.addEventListener('submit', async (event) => {
        console.log("Submit handler fired");
        event.preventDefault();
        // Grab input values
        const username = document.getElementById('username').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password1').value.trim();
        const age = document.getElementById('age').value.trim();
        const gender = document.getElementById('gender').value;

        // Reset error
        errorMsg.classList.add('hidden');
        errorMsg.textContent = '';

        // Validation
        if (!username || !email || !password || !age || !gender) {
            errorMsg.textContent = 'All fields are required.';
            errorMsg.classList.remove('hidden');
            return;
        }

        if (password.length < 6) {
            errorMsg.textContent = 'Password must be at least 6 characters long.';
            errorMsg.classList.remove('hidden');
            return;
        }
        const response = await fetch('/register_user/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({username, email, password, age, gender}),
        });
        const data = await response.json();
        if(data.success){
            alert("Registration successful!");
            window.location.href = '/login/';
        }
        else{
            alert("Registration failed: " + data.console.error());
        }
        return;
    });
});

