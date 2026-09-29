# Bike Rental System (Modernized)

This repository contains the upgraded Bike Rental System, migrated from Django to a modern **Java Spring Boot** backend and an **Angular** frontend.

## Architecture & Stack
*   **Backend:** Java 17, Spring Boot, Spring Data JPA (Hibernate), PostgreSQL/H2.
*   **Frontend:** Angular 17+, Standalone Components.
*   **Methodology:** Agile, Test-Driven Development (TDD).

## Setup Instructions

### 1. Backend (Spring Boot)
1. Ensure Java 17+ and Maven are installed.
2. Navigate to `backend-java`:
   ```bash
   cd backend-java
   ```
3. Run unit tests to verify functionality (TDD):
   ```bash
   mvn test
   ```
4. Start the application:
   ```bash
   mvn spring-boot:run
   ```
   *The server runs on http://localhost:8080*

### 2. Frontend (Angular)
1. Ensure Node.js and npm are installed.
2. Navigate to `frontend-angular`:
   ```bash
   cd frontend-angular
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Run the development server:
   ```bash
   npm start
   ```
   *The UI runs on http://localhost:4200*

## Features
*   **REST API:** Clean, standard REST endpoints for listing and renting bikes.
*   **ORM Integration:** Hibernate mapping for the `Bike` entity.
*   **Interactive UI:** Dynamic rendering of bike availability using Angular.
