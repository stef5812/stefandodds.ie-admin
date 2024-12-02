function showOverlay(overlayId) {
    const overlay = document.getElementById(overlayId);
    if (overlay) {
        overlay.classList.add("active");
    }
}

function closeOverlay(overlayId) {
    const overlay = document.getElementById(overlayId);
    if (overlay) {
        // Add the "closing" class to trigger the slide-out animation
        overlay.classList.add("closing");

        // Wait for the animation to complete before removing classes
        setTimeout(() => {
            overlay.classList.remove("active", "closing");
        }, 400); // Match the animation duration (0.4s)
    }
}

