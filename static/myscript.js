///COLOR PARAMETER///
document.addEventListener("DOMContentLoaded",()=>{
    const colors = document.getElementById("heatmapColors")
    const selected = colors.getAttribute("data-selected")
    if(selected){
        colors.value = selected;
    }
})


///INPUT TYPE PARAMETER///
const calcOptions = document.getElementById("formSubmission");
const inputs1 = calcOptions.querySelectorAll('input[type="number"]');

inputs1.forEach(element => {
    element.addEventListener("change",()=>{
        value = parseFloat(element.value)
        value = value.toFixed(2)
        element.value = value
    })
})

/// VOLATILITY PARAMETER///
const minVol = document.querySelector("#minVolatility")
const num = document.querySelector(".myNum1")

minVol.addEventListener("input", () => {
    num.textContent = minVol.value
})

const maxVol = document.querySelector("#maxVolatility")
const num2 = document.querySelector(".myNum2")

maxVol.addEventListener("input", ()=>{
    num2.textContent = maxVol.value
})



