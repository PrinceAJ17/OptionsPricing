///FOR OPTIONS CALCULATOR///
const calcOptions = document.getElementById('formSubmission');
const inputs1 = calcOptions.querySelectorAll('input[type="number"]');

inputs1.forEach(element => {
    element.addEventListener("change",()=>{
        value = parseFloat(element.value)
        value = value.toFixed(2)
        element.value = value
    })
})
///FOR SP PARAMETER///
const heatMap = document.getElementById("heatSubmission")
const inputs2 = heatMap.querySelectorAll('input[type="number"]');

inputs2.forEach(element => {
    element.addEventListener("change",()=>{
        value = parseFloat(element.value)
        value = value.toFixed(2)
        element.value = value
    })
})
///FOR VOLATILITY PARAMETER///
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

minVol.addEventListener("change", () => {
    const minValue = parseFloat(minVol.value);
    maxVol.min = minValue; // Update the min of maxVol to be the new min
});

maxVol.addEventListener("change", () => {
    const maxValue = parseFloat(maxVol.value);
    minVol.max = maxValue; // Update the max of minVol to be the new max
});


