# SitterHub

A Django web application connecting families with trusted local professionals for child care, pet care, and elderly care services.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Application Architecture](#application-architecture)
- [Database Design](#database-design)
- [Features](#features)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Testing](#testing)
- [Contributors](#contributors)
- [License](#license)

---

## Project Overview

SitterHub is a web-based agency platform designed to connect clients with professional care providers.

The application allows users to:

- Apply to become a sitter
- Browse available sitters
- Filter sitters by service category
- View detailed sitter profiles
- Submit hiring inquiries

In compliance with the Django Basics Regular Exam requirements:

- User authentication and Django User management are intentionally excluded.
- All CRUD functionality is accessible via a public "Beta" dashboard interface to ensure full evaluation of the business logic.

The project demonstrates Django fundamentals including models, forms, class-based views, function-based views, template inheritance, validation, and PostgreSQL integration.

---

## Motivation

Finding reliable care services can be time-consuming and uncertain. SitterHub centralises the discovery process into a structured platform where:

- Clients can choose sitters based on their experience or hourly hire cost
- Service categories are clearly defined and can be filtered
- Inquiries are submitted through validated forms
- Recruitment of new sitters is organised digitally

The project reflects real-world business logic implemented using clean code principles and Django best practices.

---

## Application Architecture

The project is structured into five Django apps with clear separation of responsibilities:

- **common** – Homepage, static pages, contact form, shared components
- **services** – Service categorisation (`ServiceGroup` model)
- **sitters** – Sitter profiles - list and detail views
- **inquiries** – Hiring requests made by clients
- **recruitment** – Job applications for new sitters

The architecture follows:

- Strong cohesion and loose coupling
- Clear separation of concerns
- Reusable template components
- Clean URL structure and consistent navigation

---

## Database Design

The application uses PostgreSQL as its database management system.

### Models

- `Sitter` – Core professional profile
- `ServiceGroup` – Categorises service types
- `Inquiry` – Client request tied to a specific sitter
- `Application` – Recruitment application

### Relationships

- **Many-to-Many:** `Sitter` ↔ `ServiceGroup`
- **Many-to-One (ForeignKey):** `Inquiry` → `Sitter`

The models include:

- Custom validation logic
- Meaningful field constraints
- Encapsulated business logic methods
- Proper use of Django model best practices

---

## Features

### CRUD Functionality

Full CRUD operations are implemented for:

- `Application`
- `Inquiry`

Each delete operation includes a confirmation step.

---

### Forms & Validation

The project includes:

- `ApplicationForm`
- `InquiryForm`
- `ContactForm`

Features:

- Custom server-side validation
- Field-level and form-level validation
- Customised labels and placeholders
- Disabled/read-only fields (e.g., email field during update)
- Excluded unnecessary fields
- User-friendly validation messages

---

### Views

The project uses a mix of:

- Class-Based Views (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`)
- Function-Based Views where appropriate

The views properly:

- Handle GET and POST requests
- Validate forms before saving
- Redirect after successful submissions

---

### Templates

- 15 templates using Django Template Engine
- 7+ dynamic templates displaying database data
- Base template with inheritance
- Reusable partial templates (nav and footer)
- Custom 404 error page
- No orphan pages
- URL-based filtering functionality
- Bootstrap-based responsive layout

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mpkosta/SitterHub.git
cd SitterHub
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root directory and add your local PostgreSQL credentials:

```env
DEBUG=True
DB_NAME=sitterhub_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## Running the Application

Make sure PostgreSQL is installed and running locally before applying migrations.

Apply migrations to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the application in your browser:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Usage & Initial Data Setup

To test the dynamic features of the site, you will need to populate the database with some initial data.

1. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
2. **Navigate to the admin panel:** [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
3. **Create the following entries:**
   * 2–3 `ServiceGroup` entries (e.g., Baby Care, Dog Care, Cat care)
   * 2–3 `Sitter` profiles
   * Assign the service groups to the sitters using the admin interface
   * Upload a sitter photo for better experience (otherwise it stays grey with 'No Photo' text)

---

## Testing Instructions

### Data Validation Testing
Submit an application form with the following intentional mistakes:
* A phone number shorter than 10 digits
* A name containing numeric characters

*Observe the custom server-side validation errors triggered by the `clean()` logic.*

### CRUD Testing - Applications (Кандидатури)
1. You can click on the **"Кандидатствай тук"** on the homepage, or **"Присъедини се към нас"** on the nav bar to create an application for a sitter.
2. Navigate to the **"Кандидатури (Beta)"** dashboard from the main navigation.
3. Edit an existing application and observe:
   * The visually disabled email field (cannot be edited).
   * The application status update dropdown menu.
4. Delete an application to verify the custom confirmation page routes correctly.

### CRUD Testing - Inquiries (Запитвания)
1. Go to the sitter's list page and click **"Изпрати запитване"** to test the Create functionality. You can also go to a specific Sitter's profile and click **"Наеми"**(their name)
2. Navigate to the **"Запитвания (Beta)"** dashboard from the main navigation to view the list.
3. Edit an existing inquiry to test the Update functionality.
4. Delete an inquiry to verify the custom confirmation page routes correctly.

### Custom 404 Page Testing
By default, the project runs with:
```env
DEBUG=True
```
When `DEBUG=True`, Django displays its default technical debug error page instead of the custom `404.html` template. 

**To test the custom 404 page:**
1. Temporarily update your `.env` file:
   ```env
   DEBUG=False
   ```
2. Restart the development server in your terminal.
3. Navigate to a non-existing URL, for example: [http://127.0.0.1:8000/non-existing-page/](http://127.0.0.1:8000/non-existing-page/)
4. The custom SitterHub 404 template should now be displayed.

*(Note: After testing, you may switch `DEBUG=True` again for development purposes).*

---

## Contributors
**Mario Kostadinov** – Developer  
*Developed as an individual project for the Django Basics Regular Exam at SoftUni.*

## License
This project is licensed under the MIT License.  
Copyright (c) 2026 Mario Kostadinov