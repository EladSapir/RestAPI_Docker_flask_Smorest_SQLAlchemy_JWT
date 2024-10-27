# REST API with Flask, Docker, Flask-Smorest, SQLAlchemy, and JWT

This project is a REST API built using Flask with Docker, Flask-Smorest for API documentation, SQLAlchemy for database ORM, and JWT for authentication. The API is designed with a modular structure to support easy scalability and deployment. The application is deployed to **Render** for live access.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Live Deployment](#live-deployment)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)


## Project Overview

This REST API was developed as part of a course to demonstrate key concepts in Flask, including routing, database integration, and secure user authentication using JWT. It includes Docker for containerization and Flask-Smorest for generating interactive API documentation. 

The project uses:
- **Flask** for creating the web framework.
- **Flask-Smorest** for handling request validation and generating API documentation.
- **SQLAlchemy** for working with a relational database.
- **JWT (JSON Web Tokens)** for secure authentication.
- **Docker** for containerization and consistent deployment.

## Features

- User Registration and Authentication using JWT.
- RESTful endpoints for managing resources.
- Interactive API documentation using Flask-Smorest.
- Relational database integration using SQLAlchemy.
- Containerized using Docker for easy setup and deployment.

## Live Deployment

The API is live and deployed on **Render**.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/EladSapir/RestAPI_Docker_flask_Smorest_SQLAlchemy_JWT.git
    cd RestAPI_Docker_flask_Smorest_SQLAlchemy_JWT
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows use: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Docker to start the containers**:
    ```bash
    docker-compose up --build
    ```

## Usage

1. **Start the Application**:
    ```bash
    docker-compose up
    ```
   The application should now be accessible at `http://localhost:5000/`.

2. **Interactive API Documentation**:
   Access interactive API documentation by navigating to `http://localhost:5000/swagger-ui/` or `http://localhost:5000/redoc/` to explore and test the available endpoints.

## API Endpoints

insomnia json file with all the possible requests

## Authentication

This API uses **JWT (JSON Web Tokens)** for user authentication. To access protected endpoints, you need to:

1. Register a new user or log in with an existing user to get a **JWT** token.
2. Include the JWT token in your requests to protected endpoints by adding it to the `Authorization` header like this:

