# Smart Library Project

## Overview

This project aims to redefine the library experience, making it more interactive, efficient, and
user-friendly. With RFID-enabled shelves and books and occupancy sensor-based heat maps,
the Smart Library offers a glimpse into the future of library services. These technologies not
only streamline library operations but also significantly improve the accessibility and enjoyment
of library resources for users. Through this project, we also aim to demonstrate the practical
applications and benefits of IoT in academic settings, showcasing how technology can be
harnessed to enhance learning and resource management.

## Features

- RFID-enabled shelves and books
- Real-time occupancy heat maps
- Node-Red dashboard for library users
- Django based system for library staff

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Git (for cloning the repository)

### Installing

1. **Clone the repository**:
   ```sh
   git clone https://github.com/mhreteabeTD/SmartLibrary-1/

### To run the project 
1. Navigate to the project directory
2. $ docker-compose up --build -d
3. To run the Book-Management module:
4.  cd book_management
5.  python manage.py migrate
6. To access the functionalites of Book Management
7.  python manage.py createsuperuser # don't forget to save your credentials you will need it later  
8.  go to your web browser localhost:8000/admin
9.  create a normal user # the username and password should be noted
10. naviagae to localhost:8000
11. if you input the superuser credentials then you will be taken to a book management pages which allows editing books and library structure
12. if you input the normaluser credentials then you will be redirected to a page where you can search and find the location of you favorite books
13.  after that you can goto the containers each and access them

### Project Structure

    book_management/: Django application for managing library books.
    mosquitto/config/: Configuration for Mosquitto MQTT broker.
    occupancy-sensor/: Simulated occupancy sensor data scripts.
    rasberry-pi/: Simulated Raspberry Pi for edge computing.
    rfid-reader/: Simulated RFID reader services.
    docker-compose.yml: Docker services definition file.
    node-red.json: Node-RED flow configuration.
    
### Dashboard for users
Here's a visual overview of the dashboard for library users:
1. ![Smart Library Project Structure](real_time_dashbaord.png)

2. ![Smart Library Project Structure](seat_occupancy_form.png)

3. ![Smart Library Project Structure](book_finder_new.png)


### Dashboard for admin
Here's a visual overview of the dashboard for library admins:

![Smart Library Project Structure](admin_dashboard.png)

