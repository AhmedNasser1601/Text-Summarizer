document.getElementById("summarizeForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    const inputText = document.getElementById("inputText").value;
    const minLength = parseInt(document.getElementById("minLength").value, 10);
    const maxLength = parseInt(document.getElementById("maxLength").value, 10);

    if (maxLength <= minLength) {
        alert("Max Length must be greater than Min Length");
        return;
    }

    document.getElementById("loading").classList.remove("hidden");
    document.getElementById("submitButton").disabled = true;

    const response = await fetch("/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            text: inputText,
            min_length: minLength,
            max_length: maxLength,
        }),
    });

    const data = await response.json();
    document.getElementById("summary").textContent = data.summary;
    document.getElementById("loading").classList.add("hidden");
    document.getElementById("submitButton").disabled = false;
});

function changeLength(id, delta) {
    const input = document.getElementById(id);
    let value = parseInt(input.value, 10);
    value = Math.max(0, value + delta);
    input.value = value;
}