window.addEventListener('load', function () {
    function httpGet(sentences) {
        var sentencesToSend = JSON.stringify({"sentences": sentences});
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open("POST", "http://localhost:5000/", false);
        xmlHttp.setRequestHeader("Content-Type", "application/json");
        xmlHttp.send(sentencesToSend);
        return xmlHttp.responseText;
    }

    function getSentences(text) {
        var sentencesToSend = JSON.stringify({"text": text});
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open("POST", "http://localhost:5000/tokenize", false);
        xmlHttp.setRequestHeader("Content-Type", "application/json");
        xmlHttp.send(sentencesToSend);
        return xmlHttp.responseText;
    }

    function highlightElement(e, text, hint, source) {
        var search = text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

        var re = new RegExp(search, 'g');

        if (search.length > 0) {
            e.innerHTML = e.innerHTML.replace(re, `<mark style="opacity: 1; background-color: #e57373"><a title="` + hint + `" href="` + source + `" style="color:white">$&</a></mark>`);
        }
            
    }

    var timeToWait = 0;
    if (location.hostname.match('twitter') || location.hostname.match('facebook')) {
        timeToWait = 4000;
    }
    else if (location.hostname.match('youtube')){
        while (document.body.innerText.includes("Comments") == false) {
        }
    }


    setTimeout(function () {
        var text = document.body.innerText;
        var sentences = JSON.parse(getSentences(text));
        console.log(sentences)
        var jsonString = httpGet(sentences);
        var rumorList = JSON.parse(jsonString);

        var i;
        for (i = 0; i < rumorList.length; i++) {
            if (typeof rumorList[i] != "boolean") {
                var elems = document.body.getElementsByTagName("*");
                var j;
                for (j = 0; j < elems.length; j++) {
                    if (elems[j] != null) {
                        if (elems[j].innerHTML.indexOf(sentences[i]) != -1) {
                            highlightElement(elems[j], sentences[i], rumorList[i].truth, rumorList[i].source);
                            break;
                        }
                    }
                }
            }
        }
    }, timeToWait);
    
})