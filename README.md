# 🚲 Bike Rental System

A full-stack **Bike Rental System** built using **Python** and **Django**. This web application allows users to register, browse available bikes, rent bikes, return rented bikes, and manage their bookings through a simple and user-friendly interface. An admin dashboard is also provided for efficient bike and rental management.

---

## 📌 Project Overview

The Bike Rental System simplifies the process of renting bicycles by providing an online platform where customers can easily view available bikes, make bookings, and return bikes after use. Administrators can manage bike inventory and monitor rentals through the Django admin panel.

---

## ✨ Features

### 👤 User Features

- User Registration
- User Login & Logout
- Browse Available Bikes
- View Bike Details
- Book Bikes
- Return Bikes
- View My Rentals
- Responsive Web Interface

### 🔧 Admin Features

- Add New Bikes
- Update Bike Details
- Delete Bikes
- Manage Bike Availability
- Monitor Customer Rentals
- Django Admin Dashboard

---

## 🛠 Tech Stack

- Python
- Django
- SQLite3
- HTML5
- CSS3
- Bootstrap
- Django ORM

---

## 📂 Project Structure

```
BikeRentalSystem/
│
├── BikeRentalSystem/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── rentals/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   ├── migrations/
│   └── admin.py
│
├── manage.py
├── db.sqlite3
└── README.md
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/PraneethKumar-33/BikeRentalSystem.git
```

### Navigate to Project Folder

```bash
cd BikeRentalSystem
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install django
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 📋 Main Modules

### Authentication

- User Registration
- User Login
- User Logout

### Bike Management

- Add Bikes
- Edit Bikes
- Delete Bikes
- Bike Availability

### Rental Management

- Book Bikes
- Return Bikes
- View Rental History

### Dashboard

- Admin Dashboard
- Customer Dashboard

---

## 🗄 Database

This project uses **SQLite3** as its backend database.

Django ORM is used for all database operations including:

- Create
- Read
- Update
- Delete (CRUD)

---

## 📄 Templates Included

- Home Page
- Register
- Login
- Bike Listings
- Bike Details
- Book Bike
- Return Bike
- My Rentals
- Admin Dashboard
- Base Template

---

## 🔒 Authentication

The system includes secure user authentication with:

- User Registration
- Login & Logout
- Session Management
- Admin Access Control

---

## 🎯 Future Improvements

- Online Payment Gateway
- Bike Search & Filters
- Customer Reviews & Ratings
- Email Notifications
- QR Code-Based Rentals
- REST API Integration
- Cloud Deployment
- Docker Support

---

## 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Django Framework
- Python Programming
- MVC Architecture
- CRUD Operations
- Django ORM
- User Authentication
- URL Routing
- HTML Templates
- Form Handling
- SQLite Database

---

## 👨‍💻 Author

**Praneeth Kumar**

- GitHub: https://github.com/PraneethKumar-33
- LinkedIn: https://www.linkedin.com/in/praneeth-kumar-5013aa325/

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

Feedback and contributions are always welcome!
