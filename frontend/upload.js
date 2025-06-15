// upload.js
document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById("pdfFile");
    const status = document.getElementById("uploadStatus");

    if (!fileInput.files.length) {
        status.textContent = "Please select a PDF file.";
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        status.textContent = "Uploading...";
        const response = await fetch("http://localhost:8000/upload", {
            method: "POST",
            body: formData,
        });

        const result = await response.json();
        if (response.ok) {
            status.textContent = `✅ PDF processed. ${result.chunks} chunks ready.`;
            setTimeout(() => {
                window.location.href = "chat.html";
            }, 1000);
        } else {
            status.textContent = "❌ Upload failed. " + (result.detail || "");
        }
    } catch (err) {
        status.textContent = "❌ Error uploading PDF.";
        console.error(err);
    }
});
