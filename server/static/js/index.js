

async function analyze() {
    let job_input = document.getElementById("job-input")
    let job_value = job_input.value
    let location_input = document.getElementById("location-input")
    let location_value = location_input.value

    fetch("/analyze", {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },  
        body: JSON.stringify({job:job_value, location:location_value})
    }).then(response => {
        if (!response.ok) {
            throw new Error('Request failed');
        }else{
            return response.json();
        }
    }).then(data => {
        let over = data["overview"]
        let skills = data["skills"]

        let overview_title = document.getElementById("overview-title")
        overview_title.innerHTML = "<strong>OVERVIEW</strong>"
        let overview_p = document.getElementById("overview-p")
        overview_p.innerHTML = over
    })
}
