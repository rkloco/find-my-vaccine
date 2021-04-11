document.getElementById("submit-data").addEventListener("click", onSubmit)

function onSubmit() {
    center_id = document.getElementById("center").value;
    vaccine_total = document.getElementById("vaccine-total").value;
    pfizer_total = document.getElementById("pfizer-total").value;
    moderna_total = document.getElementById("moderna-total").value;
    jj_total = document.getElementById("jj-total").value;
    var url = new URL("http://127.0.0.1:5000/confirm_submission"),
        params = {centerid:center_id, vaccinetotal:vaccine_total, pfizertotal:pfizer_total, modernatotal:moderna_total, jjtotal:jj_total}
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))
    fetch(url).then(response => response.json()).then(onResponse2);
}

function onResponse2(json) {
    document.getElementById("success-message").innerHTML = "Success! You have successfully submitted your data.";
}