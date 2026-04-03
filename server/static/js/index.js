

async function analyze() {
    let job_input = document.getElementById("job-input")
    let job_value = job_input.value
    let location_input = document.getElementById("location-input")
    let location_value = location_input.value

    fetch("/analyze", {
        method: "post",
        headers: {
        "Content-Type": "application/json",
        },  
        body: JSON.stringify({job:job_value, location:location_value})
    })
}
