document.addEventListener("DOMContentLoaded", () => {
  fetch("http://127.0.0.1:5000/employees")
    .then((response) => response.json())
    .then((data) => {
      const tableBody = document.getElementById("employee-table-body");
      data.forEach((employee) => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${employee.id}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'name', this.textContent)">${employee.name}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'position', this.textContent)">${employee.position}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'department', this.textContent)">${employee.department}</td>
          <td contenteditable="true" onblur="updateEmployee(${employee.id}, 'email', this.textContent)">${employee.email}</td>
          <td><i class="fas fa-trash-alt" onclick="deleteEmployee(${employee.id})"></i></td>
        `;
        tableBody.appendChild(row);
      });
    });
});

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
  const table = document.querySelector("table tbody");
  const rows = table.getElementsByTagName("tr");

  for (let i = 0; i < rows.length; i++) {
    const cells = rows[i].getElementsByTagName("td");
    const id = cells[0].textContent.toLowerCase();
    const name = cells[1].textContent.toLowerCase();
    const position = cells[2].textContent.toLowerCase();
    const department = cells[3].textContent.toLowerCase();
    const email = cells[4].textContent.toLowerCase();

    if (
      id.includes(idFilter) &&
      name.includes(nameFilter) &&
      position.includes(positionFilter) &&
      department.includes(departmentFilter) &&
      email.includes(emailFilter)
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
  filterTable();
}

function addEmployee() {
  const id = document.getElementById("new-id").value;
  const name = document.getElementById("new-name").value;
  const position = document.getElementById("new-position").value;
  const department = document.getElementById("new-department").value;
  const email = document.getElementById("new-email").value;

  if (id && name && position && department && email) {
    const newEmployee = {
      id,
      name,
      position,
      department,
      email,
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
                <td>${employee.name}</td>
                <td>${employee.position}</td>
                <td>${employee.department}</td>
                <td>${employee.email}</td>
                <td><i class="fas fa-trash-alt" onclick="deleteEmployee(${employee.id})"></i></td>
            `;

        table.appendChild(newRow);

        document.getElementById("new-id").value = "";
        document.getElementById("new-name").value = "";
        document.getElementById("new-position").value = "";
        document.getElementById("new-department").value = "";
        document.getElementById("new-email").value = "";
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

function toggleMode() {
  const body = document.body;
  body.classList.toggle("dark-mode");
  body.classList.toggle("light-mode");
}

function refreshDatabase() {
  if (
    confirm(
      "Are you sure you want to refresh the database? This will reset all data."
    )
  ) {
    fetch("http://127.0.0.1:5000/refresh-database", {
      method: "POST",
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message) {
          alert(data.message);
          location.reload();
        } else {
          alert(data.error);
        }
      });
  }
}
