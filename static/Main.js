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

    containerTwo.innerHTML = `										<svg width="30" idCompany = "${obj.id}" height="30" class = "button A${obj.name}">
											<circle cx="18" cy="15" r="0.5" stroke="#e8e8e8" stroke-width="2" fill="#e8e8e8" />
											<circle cx="15" cy="15" r="12" stroke="#e8e8e8" stroke-width="2" fill="none" />
											<line x1="18" y1="15" x2="13" y2="9" style="stroke:#e8e8e8;stroke-width:3" />
											<line x1="18" y1="15" x2="13" y2="21" style="stroke: #e8e8e8;stroke-width:3" />
										</svg>`

    let parent = document.querySelector(".sections");
    parent.appendChild(option);
    document.querySelector(`svg.button.A${obj.name}`).addEventListener("click", (e) => {
        let idCompany = +e.target.getAttribute("idCompany");

        document.querySelector("nav").classList.toggle("hidden");
        document.querySelector(".addPoint").setAttribute("idCompany", idCompany);


        document.querySelector(".graph").style["background-image"] = `url('../graph.jpg')`;

        //let graph = new Image(); graph.src = "../graph.jpg"
        // let canvas = document.querySelector(".graph");
        //let context = canvas.getContext("2d");
        //context.drawImage(graph, 0, 0)
    });
}

function draw(data) {
}

document.querySelector(".addPoint").addEventListener("click", (e) => {

   let idCompany = e.target.getAttribute("idCompany")
   let cashback = document.querySelector("#Cashback").value
   let day = document.querySelector("#Day").value

    console.log(day)

   if(cashback == "" || day == "")
    return;

    document.querySelector("#Cashback").value = ""
    document.querySelector("#Day").value = ""

    console.log({"date": day, "cashback": cashback})

   fetch(`http://localhost:8080/api/partners/${idCompany}/cashback`, {method: 'PUT', headers: {'Content-Type': 'application/json;charset=utf-8'}, body: JSON.stringify({"cashback": cashback, "date": day})})
          .then((response) => {
            if (!response.ok) {
                 throw new Error(`HTTP error! Status: ${response.status}`);
            }

            return response;
             })
          .then((response) => {
            let graph = new Image();
            graph.src = "../graph.jpg"

            console.log("OK")

            document.querySelector(".graph").style["background-image"] = `url('../graph.jpg')`;

           // let canvas = document.querySelector(".graph");
            //let context = canvas.getContext("2d");
            //context.drawImage(graph, 0, 0)
          });
})

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

  fetch("http://localhost:8080/temp", {method: 'GET', mod: "cors"})
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    return response.json();
  })
  .then((response) => {
    let data = response;
    let sections = document.querySelector(".sections");
    for (x of data) {
       addOption(x);
    }
  });

//////////////////////////////////
