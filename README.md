# Gravior Salvare Dog Training: Python Dash Demo

<p align="center">
<a href="https://dog-training-demo-app.onrender.com"><img src="logo.png" width="250" alt="Gravior Salvare Logo"></a>

<br>
<a href="https://dog-training-demo-app.onrender.com">Click to visit Demo Site</a>
</p>


## About
Gravior Salvare is working with several animal shelters in the Austin, TX area. We have been asked to develop an 
application to match available animals at the shelter for training as rescue dogs. Certain dogs, based on age, 
breed, sex, and other attributes, are able to be trained for different roles: Water Rescue, Mountain Rescue, and 
Disaster Rescue. We have been tasked with developing a dashboard that identifies the dogs that are available for 
each type of training, and their location displayed on a map.



## Description
Python language was chosen or ease of development and the availability of dashboard libraries. We chose dash as our library due to good integration with Jupyter, our preferred IDE. We developed the system with a Mongodb database to allow a flexible schema and future growth. As an unstructured database, we can add additional fields without causing any downstream issues in the future.

## Dash Framework
The Dash framework has three components (Develop Data Visualization Interfaces in Python With Dash – Real Python, n.d.).:

    1. Web server functionality using Flask
    2. User interactivity using React.js
    3. Chart and graphics generation using Plotly.js
    
Dash uses core components, html, and callback functions to create an dashboard application that can be deployed easily, anywhere.

## Best Practices
The application uses a modular structure with CRUD operations in a separate file that can be reused in other applications needing Mongodb CRUD operations. In addition each method within the file is encapsulated within a single repository class that hides the implementation detals from each application that uses the module. 

I also separated setup code within the Notebook from the Dashboard code to make debugging easier. Within all code, comments are used to describe what various methods and dash components are designed to do and how they interact through their callbacks. Use of whitespace and keeping ine length small, readability is improved. Using these techniques, the application is aintainable, readable, and adaptable.

As a computer scientist starting a project, it is essential to carefully review client requirements and ensure that they are well understood. Creating basic pseudocode, program flow, and mock-ups of the required visual elements before actually coding is necessary to make the overall process more efficient and less error-prone. Developing the database proceeds similarly. It is important to understand the data, although thr use of Mongodb simplifies this, as it does not have a fixed schema. Designing databases requires understanding the data that needs to be captured to provide the analysis required by the client and the data that will be needed to populate the applcation's other elements.

Computer scientists, analysts, and other data and IT professionals role within a organization are to provide solutions to business problems. The focus must be on solutions that balance performance and cost while providing deliverables that maximize value. Cloe communication between business stakeholders, project managers, developers, testers, data scientists, and analysts is essential to complete all computer and data projects successfully.
    


## REFERENCES

Develop Data Visualization Interfaces in Python With Dash – Real Python. (n.d.). Realpython. 	https://realpython.com/python-dash/.
