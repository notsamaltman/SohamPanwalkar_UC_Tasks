const form = document.getElementById("verifyForm");
const email = sessionStorage.getItem("email");
const text = document.getElementById("changeOnLoad");
text.textContent = "Verification Code for "+email;

form.addEventListener('submit',async (event)=>{
    event.preventDefault();

    const code = form.code.value.trim();

    const response = await fetch('/verify_user/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({email, code}),
})
    const data =await response.json();
    if(data.success){
        alert("Account created successfully! redirecting you to login page");
        window.location.href='/login/';
        return;
    }
    else{
        alert("error: "+data.error);
        return;
    }
});