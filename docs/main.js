document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('summarize-button').addEventListener('click', function(event) {
        event.preventDefault();

        const inputText = document.getElementById('input-text').value;

        fetch('https://api.github.com/repos/AhmedNasser1601/Arabic-Summarizer/dispatches', {
            method: 'POST',
            headers: {
                'Accept': 'application/vnd.github.everest-preview+json',
                'Authorization': 'token YOUR_GITHUB_TOKEN'
            },
            body: JSON.stringify({
                event_type: 'summarize',
                client_payload: {
                    text: inputText
                }
            })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('summary').innerText = data.summary;
        });
    });
});