const form = document.getElementById('formSubmission');
const inputs = form.querySelectorAll('input[type="number"]');
let debounceTimeout;

inputs.forEach(element => {
    element.addEventListener('input', () => {
        clearTimeout(debounceTimeout);
        if (element.value.length >= 4) {
            debounceTimeout = setTimeout(() => {
                let valueOfInput = parseFloat(element.value);
                element.value = valueOfInput.toFixed(2);
            }, 600); 
        }
    });
});
