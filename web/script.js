document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("shorten-form");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", async function(event) {
        event.preventDefault();
        
        const urlInput = document.getElementById("url");
        const url = urlInput.value;

        const response = await fetch(`/short/${encodeURIComponent(url)}`);
        const data = await response.json();

        if (data.success) {
            resultDiv.innerHTML = `Shortened URL: <a href="${data.data.link}" target="_blank">${data.data.link}</a>`;
        } else {
            resultDiv.innerHTML = `Error: ${data.error}`;
        }

        urlInput.value = "";
    });
});
