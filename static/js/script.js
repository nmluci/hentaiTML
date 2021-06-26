mainTitle = document.getElementById("titleWrapper")

function generateStyledTitle() {
    let title = document.getElementById("nukeID").innerHTML;
    let mainTitle = document.getElementById("titleWrapper");

    if (mainTitle.innerHTML !== "") mainTitle.innerHTML = "";

    for (let i=0; i<title.length; i++) {
        dTitle = document.createElement('div');
        dTitle.id = "title";
        dTitle.className = "mainbase";
        dTitle.innerHTML = title.charAt(i);
        mainTitle.appendChild(dTitle);
    }
}