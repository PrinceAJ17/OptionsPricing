const form = document.getElementById('formSubmission');
const inputs = form.querySelectorAll('input[type="number"]');

inputs.forEach(element => {
    element.addEventListener("change",()=>{
        value = parseFloat(element.value)
        value = value.toFixed(2)
        element.value = value
    })
})