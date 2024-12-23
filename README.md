# nocode-app

## Project Purpose

Build an End-to-End Application Without Writing Code
This guide will walk you through the process of building an end-to-end application without writing a single line of code. We will leverage various tools and services to create a complete application that follows a microservices architecture and a 3-tier approach, including Presentation, Backend, and Database layers.

## Application Overview

This application follows a microservices architecture and a 3-tier approach, consisting of Presentation, Backend, and Database layers.
Features

- Employee Details Display: The user interface (UI) is built using HTML, CSS, and JavaScript, allowing users to view employee details.
- Employee CRUD Operations: Users can add, edit, and delete employee records through the UI. The application supports an icon library and provides dark and light mode options.
- Backend and Database Integration: The backend is built using the Python Flask module, which stores all employee details in a SQLite database.
- Initial Data Loading: A database script is provided to load an initial set of data into the database, and the UI allows users to refresh the database as needed.

## Technologies Used

- Presentation Layer: HTML, CSS, JavaScript
- Backend Layer: Python Flask
- Database Layer: SQLite
- Development Tool: GitHub Copilot

## Architecture

The application follows a microservices architecture and a 3-tier approach:

- Presentation Layer: The user interface is built using HTML, CSS, and JavaScript, providing a seamless and responsive experience for users to interact with the application.
- Backend Layer: The backend is implemented using the Python Flask module, which handles all the business logic and communication with the database.
- Database Layer: The employee details are stored in a SQLite database, which can be initialized and refreshed through the provided database script.

## Prompts for DIY

### Presentation Layer:

1. Create an HTML file that shows all employee details.
2. Add 20 employees with few common departments and positions
3. Add filters for all attributes.
4. Add "Clear Filters" button on top right of the page
5. Create CSS with a minimalist dark mode theme. The background should be black, text should be white, and use a clean, sans-serif font. nclude styles for headings, titles etc
6. Enclose the filters in a box and make them look more aesthetic.
7. Change the table headers and filter labels to dark orange.
8. Make all the filters to fit in a row
9. Ability to add a new employee record. Enclose all the text boxes in a box and make them look clean.
10. Enable dark and light modes. Default mode should be dark but the user should be able to toggle
11. Convert the toggle button into a toggle switch
12. Modularize the code with best code and design practices
13. Move all the hard coded data into config files

### Backend and Database Layer:

1. Create a python flask module that exposes APIs to perform CRUD operations on employees
2. Add CORS support to the flask application
3. Create an SQLite database and fetch all the employees from the database
4. Create an initial load of 20 employees in the database
5. Modularize the code as per standard design and coding practices
6. Load initial data into database only if there are no records in the table

### Presentation and Backend layers

1. Add inline edit and delete operations
2. Add Font Awesome for icons and update the buttons to use icons
3. Use only icons and remove buttons
4. Add option to "Refresh Database" and on click, prompt the user for confirmation
5. Add Unit test cases across the modules to cover all scenarios including boundary conditions and negative scenarios

### Add Visual charts

1. Create an interactive employee dashboard with two key visualizations using HTML and JavaScript
2. Use Smooth and Curvy Layout for Tab Heads Using SVG Gooey. Also animate transitions.
3. Make all the pages responsive
4. Update the visualizations page to use icons in the tab heads and make the tabs more aesthetic.
5. Theme selected in employee-details page should be carry forwarded to visualizations page and vice versa. Show theme toggle on visaulizations page

### Enhancing the application

1. Add below attributes to employee and make all them nullable-
   Salary, Country, Hiring Date, Previous Salary, Last Promoted Date
   Make required changes in webpage, filters, routes, database to accomodate new attributes
2. Update initial load to populate all the employee attributes for 20 employees across countries
3. Remove the hiring date and last promoted date filters from the employee-details webpage.
4. Update the employee details page to show the hiring date in the data table and while adding a new record, but do not show it in the filters section.
5. Ensure that all the filters in employee page are working flawlessly. Do not add new filters for hiring date and last promoted date
6. When adding a new record, ensure all the fields are saved correctly
7. Show a floating "Chat" icon in employee detail page. On click I should be able to make a chat conversation. Anything user types should be shown as "Customer", anything the app responds should be shown as "AI Bot"
8. Create a chat endpoint in the application
9. Update the `sendMessage` function to invoke the chat route from the chat screen.
10. Generate CSS for a chat window interface. The chat window should have rounded corners and a light background color. User messages should appear in rounded bubbles with a distinct background color (e.g., purple or blue) and be aligned to the right. Include a close button in the top corner.
11. Convert chat into an independent component and make it available on all web pages
12. Create a Welcome page and modularize all pages
