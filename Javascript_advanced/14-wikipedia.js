function createElement(data) {
    let paragraph = document.createElement('p');
    paragraph.textContent = (data);
    document.body.appendChild(paragraph);
}

function queryWikipedia(callback) {
    let xhr = new XMLHttpRequest();
    let url = new URL ('https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Stack%20Overflow&origin=*')
    xhr.open('GET', url, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            let response = JSON.parse(xhr.responseText);
            let page = response.query.pages;
            let pageId = Object.keys(page)[0];

            callback(page[pageId].extract);
        }
    };
    xhr.send();
}

queryWikipedia(createElement);