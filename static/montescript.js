const calcOptions = document.getElementById("calculateForm");
const inputs1 = calcOptions.querySelectorAll(".dp");

inputs1.forEach((element) => {
    const defaultValue = element.defaultValue
    element.addEventListener("change",()=>{
        value = parseFloat(element.value)
        if(value<0){
            alert("Please enter a positive number")
            element.value = defaultValue; 
            return;
        }
        value = value.toFixed(2)
        element.value = value
    })
})