function validarContrasenia() {
    var contraseniaInput = document.getElementById("contrasenia");
    var errorContrasenia = document.getElementById("errorContrasenia");
    
    var expresionRegular = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
    
    if (!expresionRegular.test(contraseniaInput.value)) {
        errorContrasenia.style.color = "red";
        return true;
    } else {
        errorContrasenia.style.color = "";
        return false;
    }
}