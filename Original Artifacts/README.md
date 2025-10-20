<div align="center">
    <u>**About the Project/Project Title**</u>
</div>
<i>This project is a MongoDB-powered web application dashboard developed for Grazioso Salvare, an international rescue-animal training company. The dashboard enables users to filter, view, and analyze dog profiles from animal shelters to identify potential candidates for search-and-rescue training.
The project consists of a backend database (MongoDB) and a frontend web application built using Dash, a Python framework for creating interactive web applications. It follows the MVC (Model-View-Controller) architecture, where:
•	Model: MongoDB stores animal shelter data.
•	View: Dash components render an interactive web dashboard.
•	Controller: A Python module implements CRUD (Create, Read, Update, Delete) operations to interact with the MongoDB database.</i> <br>


<div align="center">
  <u>**Motivation**</u>
</div>
<i>The purpose of this project is to assist Grazioso Salvare, an international rescue-animal training company, in identifying and categorizing potential search-and-rescue dogs from animal shelters. By leveraging a MongoDB database and an interactive web dashboard, this system enables efficient filtering, visualization, and analysis of dog profiles based on rescue suitability criteria.
This project aims to:
•	Automate the selection process for identifying dogs suitable for rescue training.
•	Provide an intuitive dashboard to reduce user errors and training time.
•	Enhance data accessibility for shelter operators and rescue teams.
•	Enable scalability by allowing further enhancements and open-source contributions. <br>


</i>

<div align="center">
  <br><b>Getting Started</b>
</div>

Prerequisites
Ensure you have the following installed: <br>
•	Python 3.x  
•	MongoDB  
•	Required Python libraries:  
```bash
pip install dash dash_leaflet dash_table plotly pandas pymongo
```

•	Run the dashboard by opening the ipynb file.


<div align="center">
  <br><b>Installation</b>
</div>

<h3>Programming Languages & Frameworks</h3>
<ul>
  <li><b>Python 3.x</b> – Core programming language for the backend and dashboard.</li>
  <li><b>Dash</b> – Python framework for building the interactive web dashboard.</li>
  <li><b>Plotly Express</b> – Used for creating visualizations like pie charts.</li>
  <li><b>Dash Leaflet</b> – Provides geolocation mapping features.</li>
</ul>

<h3>Database & Backend</h3>
<ul>
  <li><b>MongoDB</b> – NoSQL database for storing and retrieving animal shelter data.</li>
  <li><b>PyMongo</b> – Python library for interacting with MongoDB.</li>
</ul>

<h3>Data Processing & Visualization</h3>
<ul>
  <li><b>Pandas</b> – For data manipulation and transformation.</li>
  <li><b>NumPy</b> – Supports efficient numerical computations.</li>
  <li><b>Matplotlib</b> – Optional for additional data visualization.</li>
</ul>

<h3>Development & Execution Environment</h3>
<ul>
  <li><b>Jupyter Notebook</b> – Required to execute ProjectTwo.ipynb for running the dashboard.</li>
  <li><b>Jupyter Dash</b> – Enables Dash applications to run inside Jupyter Notebooks.</li>
</ul>

<h3>Other Dependencies</h3>
<ul>
  <li><b>Base64 (Python module)</b> – Used for encoding and displaying images (e.g., the Grazioso Salvare logo).</li>
  <li><b>Dash Table</b> – For interactive data table functionalities (filtering, sorting, pagination).</li>
</ul>

<h3>System Requirements</h3>
<ul>
  <li><b>Operating System</b>: Windows, macOS, or Linux</li>
  <li><b>Internet Connection</b>: Required for database interactions (if using a remote MongoDB server).</li>
  <li><b>Disk Space</b>: Minimal storage required (~100MB)</li>
</ul>
<br>


<div align="center">
  <br><b>Usage</b>
</div>

Code Example
Here will be the code that will have credentials to access MongoDB while also access the specified databases needed for this dashboard to work (crud.py)

This is what will allow the user to create, read, update and delete information as an “aacuser” within the admin database. While also being able to access the proper documents needed for the dashboard.<br>

![image](https://github.com/user-attachments/assets/da447728-56a1-48ed-9d24-eab195d36630)

Here will be a screenshot of the ProjectTwo.ipynb file that goes over the main code that runs the dashboard.  Where I used the crud.py file to access MongoDB and then allow the user to view a GUI or graphical user interface such as a map and graph. Which has a filter, view and information to allow the user to analyze animal shelter data.

*NOTE* - on bottom when running the ipynb file ensure that there are no errors or issues. Console should state that the Dash App is running @ (example address: 127.0.0.1:37498) <br>


![image](https://github.com/user-attachments/assets/8b476e58-ebac-4e6c-899b-529db6df55ba)
![image](https://github.com/user-attachments/assets/023e6bcf-48b9-4d92-b526-f74382c66d88)

![image](https://github.com/user-attachments/assets/860978e5-347e-4fbb-91a0-a542a1dbd646) <br>



<div align="center">
  <br><b>Tests</b>
</div>
This is how the dashboard should look. Having the logo and the title, along with the different radio buttons for filter. Then below we would have displayed information, along with a graph and a map to display types of dog in a certain location. And a map showing the location of that animal_type.

![image](https://github.com/user-attachments/assets/755051dc-1e8b-41e6-a9e6-c1ad0788fb13)<br>


<div align="center">
  <br><b>Roadmap/Features</b>
</div>


<b>Planned Enhancement</b>
<br>
- **User Authentication & Role Management**
  - Implement login functionality with role-based access control.
  - Allow different levels of permissions for shelter staff and administrators.

- **Enhanced Filtering & Search**
  - Enable multi-criteria filtering (e.g., breed, age, size, temperament).
  - Implement a keyword search feature for more refined searches.

- **Machine Learning for Dog Selection**
  - Train an AI model to suggest dogs based on success rates in past rescues.
  - Use historical data to predict the best candidates for search-and-rescue training.

- **Improved UI/UX Design**
  - Add a dark mode and customizable themes.
  - Make the interface mobile-friendly for better accessibility.

- **Automated Report Generation**
  - Generate PDF or CSV reports for adoption and rescue insights.
  - Allow users to export filtered data for offline use.

- **Database Expansion**
  - Support integration with multiple shelters beyond Austin, TX.
  - Implement a centralized database for better data sharing across locations.

**Known Issues & Fixes**
- **MongoDB Connection Handling**
  - Improve error handling for database disconnections.
  
- **Geolocation Accuracy**
  - Some locations may be missing or incorrect due to incomplete data.
  
- **Table Sorting Bugs**
  - Occasional sorting errors when multiple filters are applied.
<br>


**Contact**
- **Your name**: Nick Wyrwas
- **Email**: [nick.wyrwas@outlook.com](mailto:nick.wyrwas@outlook.com)
- **GitHub**: [https://github.com/nwyrwas](https://github.com/nwyrwas)


