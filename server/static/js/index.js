

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

        let skills_list = document.getElementById("skills-list")

        let final_list = ""
        for (let index = 0; index < skills.length; index++) {
            const element = skills[index];
            let item = "<li>"
            item += "<h3>" +element["skill"]+"</h3>"
            item += "  -  <span><strong>RELEVANCE: </strong>" + element["relevance"] + "      <strong>DIFFICULTY: </strong>" + element["difficulty"] + "</span>"
            item += "<p id='desc-p'>" + element["desc"] + "</p>"
            item += "</li>"
            final_list += item
        }
        skills_list.innerHTML = final_list
    })
}
