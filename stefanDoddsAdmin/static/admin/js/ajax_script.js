document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("load-template"); // Button to trigger the loading
    const contentDiv = document.getElementById("dynamic-container"); // Div where content will load

    button.addEventListener("click", () => {
        fetch("http://127.0.0.1:8001/dynamic-content/")
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response was not ok: " + response.statusText);
                }
                return response.text();
            })
            .then(html => {
                contentDiv.innerHTML = html; // Insert the loaded HTML into the div
            })
            .catch(error => {
                console.error("There was a problem with the fetch operation:", error);
                contentDiv.innerHTML = "<p>Error loading content.</p>";
            });
    });
});
