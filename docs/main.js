document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('summarize-button').addEventListener('click', function(event) {
        event.preventDefault();

        const inputText = document.getElementById('input-text').value;

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/execute", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var json = JSON.parse(xhr.responseText);
                document.getElementById('summary').innerText = json.summary;
            }
        };
        var data = JSON.stringify({
            "text": inputText
        });
        xhr.send(data);
    });
});