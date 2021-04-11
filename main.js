console.log("Hello World");

document.getElementById("submit-button").addEventListener("click", onButtonClick)

function onButtonClick() {
    vaccine_type = document.getElementById("vaccine-type").value;
    fetch("http://127.0.0.1:5000/getlocation?vaccine_type=" + vaccine_type).then(response => response.json()).then(onResponse);
}

function onResponse(json) {
    console.log(json.type);
    document.getElementById("best-name").innerHTML = json.name;
    document.getElementById("best-location").innerHTML = json.location;
}