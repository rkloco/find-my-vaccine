console.log("Hello World");

document.getElementById("submit-button").addEventListener("click", onButtonClick)
// document.getElementById("submit-data").addEventListener("click", onSubmit)

// function onSubmit() {
//     center_id = document.getElementById("center").value;
//     vaccine_total = document.getElementById("vaccine-total");
//     pfizer_total = document.getElementById("pfizer-total");
//     moderna_total = document.getElementById("moderna-total");
//     jj_total = document.getElementById("jj-total");
//     var url = new URL("http://127.0.0.1:5000/confirm_submission"),
//         params = {centerid:center_id, vaccinetotal:vaccine_total, pfizertotal: pfizer_total, modernatotal: moderna_total, jjtotal: jj_total}
//     Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
//     fetch(url).then(response => response.json()).then(onResponse2);
// }

function onButtonClick() {
    vaccine_type = document.getElementById("vaccine-type").value;
    zip_code = document.getElementById("zip-code").value;
    console.log(zip_code);
    var url = new URL("http://127.0.0.1:5000/getlocation"),
        params = {vaccinetype:vaccine_type, zipcode:zip_code}
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
    fetch(url).then(response => response.json()).then(onResponse);
}

function onResponse(json) {
    console.log(json.type);
    document.getElementById("success").innerHTML = "Success! According to your preferences, this location is the best center for you:";
    document.getElementById("best-name").innerHTML = json.name + "; ";
    document.getElementById("best-location").innerHTML = json.location;
}

// function onResponse2(json) {
//     console.log("got here");
//     document.getElementById("success-message").innerHTML = "Success!";
// }