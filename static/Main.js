function addOption(obj) {
    let option = document.createElement("div");
    let containerOne = document.createElement("div");
    let containerTwo = document.createElement("div");
    let name = document.createElement("div");
    let p = document.createElement("p");

    option.classList.add("option");
    containerOne.classList.add("container");
    containerTwo.classList.add("container");
    name.classList.add("name");

    option.appendChild(containerOne);
    option.appendChild(containerTwo);

    containerOne.appendChild(name);
    name.appendChild(p);

    p.innerHTML = obj.name;

    containerTwo.innerHTML = `										<svg width="30" height="30" class = "button">
											<circle cx="18" cy="15" r="0.5" stroke="#e8e8e8" stroke-width="2" fill="#e8e8e8" />
											<circle cx="15" cy="15" r="12" stroke="#e8e8e8" stroke-width="2" fill="none" />
											<line x1="18" y1="15" x2="13" y2="9" style="stroke:#e8e8e8;stroke-width:3" />
											<line x1="18" y1="15" x2="13" y2="21" style="stroke: #e8e8e8;stroke-width:3" />
										</svg>`

    let parent = document.querySelector(".sections");
    parent.appendChild(option);

    document.querySelector(`svg.button.${obj.name}`).addEventListener("onclick", (e) => {
      let dates = obj.dates;
      let nav = document.querySelector("nav");

      nav.classList.add("working");

      console.log(dates);

      draw(dates);
    });
}

function draw(data) {
}

document.querySelector(".icon").addEventListener("click", (e) => {
    e.stopPropagation();
    document.querySelector(".addCompany").classList.toggle("hidden");
    document.querySelector("#inputCompany").value = "";
    document.querySelector("#inputBudget").value = "";
})

document.querySelector(".addCompany").addEventListener("click", (e) => {
    e.stopPropagation();
})

let forma = document.querySelector("#forma");

forma.addEventListener("submit", (e) => {
    e.preventDefault();

    let name = document.querySelector("#inputCompany").value;
    let budget = +document.querySelector("#inputBudget").value;

    document.querySelector(".addCompany").classList.add("hidden");
    fetch("http://localhost:8080/api/partners", {method: 'POST',headers: {'Content-Type': 'application/json;charset=utf-8'}, body: JSON.stringify({"name": name, "budget": budget})}).then((r) => {
        addOption({"name": name, "budget": budget})
    })
    document.querySelector("#inputCompany").value = "";
    document.querySelector("#inputBudget").value = "";
})

document.querySelector("body").addEventListener("click", (e) => {
    document.querySelector("#inputCompany").value = "";
    document.querySelector("#inputBudget").value = "";
    document.querySelector(".addCompany").classList.add("hidden");
})
/*
  fetch("http://localhost:8080/api/partners", {method: 'POST'})
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    return response;
  })
  .then((response) => {
    console.log(response.json()["name"]);
  })
*/
