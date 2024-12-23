document.addEventListener("DOMContentLoaded", () => {
  const theme = localStorage.getItem("theme") || "dark-mode";
  document.body.classList.add(theme);
  if (theme === "light-mode") {
    document.getElementById("theme-toggle").checked = true;
  }
  applyThemeToElements(theme);
});

function toggleMode() {
  const body = document.body;
  body.classList.toggle("dark-mode");
  body.classList.toggle("light-mode");
  const theme = body.classList.contains("dark-mode")
    ? "dark-mode"
    : "light-mode";
  localStorage.setItem("theme", theme);
  applyThemeToElements(theme);
}

function applyThemeToElements(theme) {
  const elements = document.querySelectorAll(".visualization-box");
  elements.forEach((element) => {
    if (theme === "dark-mode") {
      element.style.backgroundColor = "#222";
      element.style.borderColor = "#555";
    } else {
      element.style.backgroundColor = "#f9f9f9";
      element.style.borderColor = "#ccc";
    }
  });
}

function saveTheme() {
  const theme = document.body.classList.contains("dark-mode")
    ? "dark-mode"
    : "light-mode";
  localStorage.setItem("theme", theme);
}
