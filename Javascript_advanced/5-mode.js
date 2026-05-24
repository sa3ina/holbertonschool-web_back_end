function changeMode (size, weight, transform, background, color) {
    return function () {
        document.body.style.fontSize = size + "px";
        document.body.style.fontWeight = weight;
        document.body.style.textTransform = transform;
        document.body.style.backgroundColor = background;
        document.body.style.color = color;
      };
}

function main () {
    const spooky = changeMode(9, "bold", "uppercase", "pink", "green");
    const darkMode = changeMode(12, "bold", "capitalize", "black", "white");
    const screamMode = changeMode(12, "normal", "lowercase", "white", "black");

    const paragraph = document.createElement("p");
    paragraph.innerHTML = "Welcome Holberton!";
    document.body.appendChild(paragraph);

    const button_spooky = document.createElement("button");
    button_spooky.innerHTML = "Spooky";
    document.body.appendChild(button_spooky);

    const button_dark_mode = document.createElement("button");
    button_dark_mode.innerHTML = "Dark mode";
    document.body.appendChild(button_dark_mode);

    const button_scream_mode = document.createElement("button");
    button_scream_mode.innerHTML = "Scream mode";
    document.body.appendChild(button_scream_mode);

    button_spooky.addEventListener("click", () => spooky());
    button_dark_mode.addEventListener("click", () => darkMode());
    button_scream_mode.addEventListener("click", () => screamMode());
}

main();