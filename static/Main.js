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

  containerTwo.innerHTML = `<svg width="30" height="30" class = "button ${obj.name}">
                              <circle cx="15" cy="15" r="12" stroke="#0B1957" stroke-width="2" fill="none" />
                              <circle cx="15" cy="17" r="1" stroke="#0B1957" stroke-width="1" fill="#0B1957" />
                              <line x1="8" y1="12" x2="15" y2="17" style="stroke:#0B1957;stroke-width:3" />
                              <line x1="15" y1="17" x2="22" y2="12" style="stroke:#0B1957;stroke-width:3" />
                            </svg>`

  let parent = document.querySelector(".sections");
  parent.appendChild(option);

  document.querySelector(`.${obj.name}`).addEventListener("onclick", (e) => {
    let info = obj.info;
  });
}
