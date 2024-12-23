document.addEventListener("DOMContentLoaded", () => {
  loadData();
  if (document.getElementById("departmentChart")) {
    renderDepartmentChart();
  }
  if (document.getElementById("positionChart")) {
    renderPositionChart();
  }
  if (document.getElementById("positionsInDepartmentChart")) {
    renderPositionsInDepartmentChart();
  }
  document.querySelector(".tablinks").click(); // Open the first tab by default
});

function loadData() {
  fetch("http://127.0.0.1:5000/employees")
    .then((response) => response.json())
    .then((data) => {
      const tableBody = document.getElementById("employee-table-body");
      tableBody.innerHTML = ""; // Clear existing data
      data.forEach((employee) => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${employee.id}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'name', this.textContent)">${employee.name}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'position', this.textContent)">${employee.position}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'department', this.textContent)">${employee.department}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'email', this.textContent)">${employee.email}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'salary', this.textContent)">${employee.salary}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'country', this.textContent)">${employee.country}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'hiring_date', this.textContent)">${employee.hiring_date}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'previous_salary', this.textContent)">${employee.previous_salary}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'last_promoted_date', this.textContent)">${employee.last_promoted_date}</td>
          <td><i class="fas fa-trash-alt" onclick="deleteEmployee(${employee.id})"></i></td>
        `;
        tableBody.appendChild(row);
      });
    });
}

function refreshDatabase() {
  if (
    confirm(
      "Are you sure you want to refresh the database? This will reset all data."
    )
  ) {
    fetch("http://127.0.0.1:5000/reset-database", {
      method: "POST",
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message) {
          alert(data.message);
          loadData();
        } else {
          alert(data.error);
        }
      });
  }
}

function filterTable() {
  const idFilter = document.getElementById("filter-id").value.toLowerCase();
  const nameFilter = document.getElementById("filter-name").value.toLowerCase();
  const positionFilter = document
    .getElementById("filter-position")
    .value.toLowerCase();
  const departmentFilter = document
    .getElementById("filter-department")
    .value.toLowerCase();
  const emailFilter = document
    .getElementById("filter-email")
    .value.toLowerCase();
  const salaryFilter = document
    .getElementById("filter-salary")
    .value.toLowerCase();
  const countryFilter = document
    .getElementById("filter-country")
    .value.toLowerCase();
  const previousSalaryFilter = document
    .getElementById("filter-previous-salary")
    .value.toLowerCase();
  const table = document.querySelector("table tbody");
  const rows = table.getElementsByTagName("tr");

  for (let i = 0; i < rows.length; i++) {
    const cells = rows[i].getElementsByTagName("td");
    const id = cells[0].textContent.toLowerCase();
    const name = cells[1].textContent.toLowerCase();
    const position = cells[2].textContent.toLowerCase();
    const department = cells[3].textContent.toLowerCase();
    const email = cells[4].textContent.toLowerCase();
    const salary = cells[5].textContent.toLowerCase();
    const country = cells[6].textContent.toLowerCase();
    const previousSalary = cells[8].textContent.toLowerCase();

    if (
      id.includes(idFilter) &&
      name.includes(nameFilter) &&
      position.includes(positionFilter) &&
      department.includes(departmentFilter) &&
      email.includes(emailFilter) &&
      salary.includes(salaryFilter) &&
      country.includes(countryFilter) &&
      previousSalary.includes(previousSalaryFilter)
    ) {
      rows[i].style.display = "";
    } else {
      rows[i].style.display = "none";
    }
  }
}

function clearFilters() {
  document.getElementById("filter-id").value = "";
  document.getElementById("filter-name").value = "";
  document.getElementById("filter-position").value = "";
  document.getElementById("filter-department").value = "";
  document.getElementById("filter-email").value = "";
  document.getElementById("filter-salary").value = "";
  document.getElementById("filter-country").value = "";
  document.getElementById("filter-previous-salary").value = "";
  filterTable();
}

function addEmployee() {
  const id = document.getElementById("new-id").value;
  const name = document.getElementById("new-name").value;
  const position = document.getElementById("new-position").value;
  const department = document.getElementById("new-department").value;
  const email = document.getElementById("new-email").value;
  const salary = document.getElementById("new-salary").value;
  const country = document.getElementById("new-country").value;
  const hiringDate = document.getElementById("new-hiring-date").value;
  const previousSalary = document.getElementById("new-previous-salary").value;
  const lastPromotedDate = document.getElementById(
    "new-last-promoted-date"
  ).value;

  if (
    id &&
    name &&
    position &&
    department &&
    email &&
    salary &&
    country &&
    hiringDate &&
    previousSalary &&
    lastPromotedDate
  ) {
    const newEmployee = {
      id,
      name,
      position,
      department,
      email,
      salary,
      country,
      hiring_date: hiringDate,
      previous_salary: previousSalary,
      last_promoted_date: lastPromotedDate,
    };

    fetch("http://127.0.0.1:5000/employee", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newEmployee),
    })
      .then((response) => response.json())
      .then((employee) => {
        const table = document.querySelector("table tbody");
        const newRow = document.createElement("tr");

        newRow.innerHTML = `
          <td>${employee.id}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'name', this.textContent)">${employee.name}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'position', this.textContent)">${employee.position}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'department', this.textContent)">${employee.department}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'email', this.textContent)">${employee.email}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'salary', this.textContent)">${employee.salary}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'country', this.textContent)">${employee.country}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'hiring_date', this.textContent)">${employee.hiring_date}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'previous_salary', this.textContent)">${employee.previous_salary}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'last_promoted_date', this.textContent)">${employee.last_promoted_date}</td>
          <td><i class="fas fa-trash-alt" onclick="deleteEmployee(${employee.id})"></i></td>
        `;

        table.appendChild(newRow);

        document.getElementById("new-id").value = "";
        document.getElementById("new-name").value = "";
        document.getElementById("new-position").value = "";
        document.getElementById("new-department").value = "";
        document.getElementById("new-email").value = "";
        document.getElementById("new-salary").value = "";
        document.getElementById("new-country").value = "";
        document.getElementById("new-hiring-date").value = "";
        document.getElementById("new-previous-salary").value = "";
        document.getElementById("new-last-promoted-date").value = "";
      });
  } else {
    alert("Please fill in all fields");
  }
}

function updateEmployee(id, field, value) {
  fetch(`http://127.0.0.1:5000/employee/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ [field]: value }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        alert(data.error);
      }
    });
}

function deleteEmployee(id) {
  fetch(`http://127.0.0.1:5000/employee/${id}`, {
    method: "DELETE",
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.message) {
        const row = document.querySelector(
          `tr td:first-child:contains(${id})`
        ).parentElement;
        row.remove();
      } else {
        alert(data.error);
      }
    });
}

function renderDepartmentChart() {
  fetch("http://127.0.0.1:5000/employees")
    .then((response) => response.json())
    .then((data) => {
      const departmentCounts = data.reduce((acc, employee) => {
        acc[employee.department] = (acc[employee.department] || 0) + 1;
        return acc;
      }, {});

      const ctx = document.getElementById("departmentChart").getContext("2d");
      new Chart(ctx, {
        type: "bar",
        data: {
          labels: Object.keys(departmentCounts),
          datasets: [
            {
              label: "Employee Count",
              data: Object.values(departmentCounts),
              backgroundColor: "rgba(75, 192, 192, 0.2)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
          plugins: {
            chart3d: {
              enabled: true,
              alpha: 10,
              beta: 15,
              depth: 50,
            },
          },
        },
      });
    });
}

function renderPositionChart() {
  fetch("http://127.0.0.1:5000/employees")
    .then((response) => response.json())
    .then((data) => {
      const positionCounts = data.reduce((acc, employee) => {
        acc[employee.position] = (acc[employee.position] || 0) + 1;
        return acc;
      }, {});

      const ctx = document.getElementById("positionChart").getContext("2d");
      new Chart(ctx, {
        type: "pie",
        data: {
          labels: Object.keys(positionCounts),
          datasets: [
            {
              label: "Employee Count",
              data: Object.values(positionCounts),
              backgroundColor: [
                "rgba(255, 99, 132, 0.2)",
                "rgba(54, 162, 235, 0.2)",
                "rgba(255, 206, 86, 0.2)",
                "rgba(75, 192, 192, 0.2)",
                "rgba(153, 102, 255, 0.2)",
                "rgba(255, 159, 64, 0.2)",
              ],
              borderColor: [
                "rgba(255, 99, 132, 1)",
                "rgba(54, 162, 235, 1)",
                "rgba(255, 206, 86, 1)",
                "rgba(75, 192, 192, 1)",
                "rgba(153, 102, 255, 1)",
                "rgba(255, 159, 64, 1)",
              ],
              borderWidth: 1,
            },
          ],
        },
        options: {
          plugins: {
            chart3d: {
              enabled: true,
              alpha: 10,
              beta: 15,
              depth: 50,
            },
          },
        },
      });
    });
}

function renderPositionsInDepartmentChart() {
  fetch("http://127.0.0.1:5000/employees")
    .then((response) => response.json())
    .then((data) => {
      const departmentPositions = data.reduce((acc, employee) => {
        if (!acc[employee.department]) {
          acc[employee.department] = {};
        }
        acc[employee.department][employee.position] =
          (acc[employee.department][employee.position] || 0) + 1;
        return acc;
      }, {});

      const departments = Object.keys(departmentPositions);
      const positions = [...new Set(data.map((employee) => employee.position))];

      const datasets = positions.map((position) => ({
        label: position,
        data: departments.map(
          (department) => departmentPositions[department][position] || 0
        ),
        backgroundColor: getRandomColor(),
      }));

      const ctx = document
        .getElementById("positionsInDepartmentChart")
        .getContext("2d");
      new Chart(ctx, {
        type: "bar",
        data: {
          labels: departments,
          datasets: datasets,
        },
        options: {
          scales: {
            x: {
              stacked: true,
            },
            y: {
              stacked: true,
              beginAtZero: true,
            },
          },
          plugins: {
            chart3d: {
              enabled: true,
              alpha: 10,
              beta: 15,
              depth: 50,
            },
          },
        },
      });
    });
}

function getRandomColor() {
  const letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function openTab(evt, tabName) {
  const tabcontent = document.getElementsByClassName("tabcontent");
  for (let i = 0; i < tabcontent.length; i++) {
    tabcontent[i].classList.remove("active");
  }
  const tablinks = document.getElementsByClassName("tablinks");
  for (let i = 0; i < tablinks.length; i++) {
    tablinks[i].classList.remove("active");
  }
  document.getElementById(tabName).classList.add("active");
  evt.currentTarget.classList.add("active");
}

function toggleChat() {
  const chatWindow = document.getElementById("chat-window");
  chatWindow.style.display =
    chatWindow.style.display === "none" || chatWindow.style.display === ""
      ? "flex"
      : "none";
}

function sendMessage() {
  const chatInput = document.getElementById("chat-input");
  const chatBody = document.getElementById("chat-body");
  const message = chatInput.value.trim();
  if (message) {
    const customerMessage = document.createElement("div");
    customerMessage.className = "chat-message customer";
    customerMessage.textContent = `Customer: ${message}`;
    chatBody.appendChild(customerMessage);
    chatInput.value = "";

    fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    })
      .then((response) => response.json())
      .then((data) => {
        const botMessage = document.createElement("div");
        botMessage.className = "chat-message ai-bot";
        botMessage.textContent = `AI Bot: ${data.response}`;
        chatBody.appendChild(botMessage);
        chatBody.scrollTop = chatBody.scrollHeight;
      });
  }
}
