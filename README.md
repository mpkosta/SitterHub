# SitterHub

A Django web application connecting families with trusted local professionals for child care, pet care, and elderly care services.

---

## Live Demo & Ready-to-Test Environment
**https://sitterhub.onrender.com**

The application is fully deployed and configured. **No local installation, database migrations, or console commands are required.** You can test the entire lifecycle and all critical business logic directly through the frontend UI using the pre-configured accounts below.

---

## Test Accounts

To facilitate immediate testing of the role-based access control (RBAC) and business logic without using the Django Admin panel, the following accounts have been pre-configured in the live production database:

| Role | Username / Email | Password         | Access Level & Frontend Capabilities |
| :--- | :--- |:-----------------| :--- |
| **Admin** | `admin` | `softadmin1326`  | **Full UI Access.** Can delete any sitter/inquiry and manage applications directly from the frontend dashboards. Uneditable fields (like hourly rate) are manageable by this role. |
| **Sitter** | `sitter_test` | `softsitter1326` | **Sitter UI.** Can update their own profile, view received inquiries, but is blocked from deleting other sitters or accessing administrative dashboards. |
| **Client** | `client_test` | `softclient1326`               | **Client UI.** Can browse sitters, send and edit their own inquiries, and access the client dashboard. |

*Please log in using these credentials to test the full application lifecycle. All administrative actions are intentionally integrated into the main user interface to demonstrate advanced View-level permissions.*

---

## Table of Contents
- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Advanced Features & Exam Criteria Met](#advanced-features--exam-criteria-met)
- [Application Architecture](#application-architecture)
- [Database Design](#database-design)
- [Features](#features)
- [Live Testing Instructions (Step-by-Step)](#live-testing-instructions)
- [Contributors & License](#contributors)

---

## Project Overview

SitterHub is a web-based agency platform designed to connect clients with professional care providers.

The application allows users to:

- Apply to become a sitter
- Browse available sitters
- Filter sitters by service category
- View detailed sitter profiles
- Submit hiring inquiries

The application includes both a public section (accessible without authentication) and a private section (available only to logged-in users with role-based access).
The project also demonstrates advanced Django fundamentals including custom user models, forms, class-based views (CBVs), RESTful APIs, asynchronous tasks, template inheritance, robust validation, and PostgreSQL integration.

---

## Motivation

Finding reliable care services can be time-consuming and uncertain. SitterHub centralises the discovery process into a structured platform where:

- Clients can choose sitters based on their experience or hourly hire cost
- Service categories are clearly defined and can be filtered
- Inquiries are submitted through validated forms
- Recruitment of new sitters is organised digitally

The project reflects real-world business logic implemented using clean code principles and Django best practices.

---

## Advanced Features

* **Custom User Model & Authentication:** Extended the built-in Django User model (`CustomUser`). Implemented distinct user groups (Admin, Sitter, Client) with specific UI and View-level permissions.
* **Frontend Business Logic:** Critical administrative functionalities are accessible via the main UI (not just Django Admin), protected by `LoginRequiredMixin` and `UserPassTestMixin` to prevent unauthorized URL access.
* **RESTful APIs:** Integrated **Django REST Framework (DRF)** featuring serializers and API views (`ListAPIView`, `RetrieveAPIView`) for Sitter data, secured with `IsAuthenticatedOrReadOnly`.
* **Asynchronous Processing:** Configured **Celery** and **Redis** for background task execution (e.g., sending email notifications upon application status changes).
* **Cloud Storage & Static Files:** Utilized **Cloudinary** for scalable profile image hosting and **WhiteNoise** for static file management in production.
* **Automated Testing:** Developed **29 automated tests** (Unit and Integration) covering models, forms, and view access restrictions.
* **Full CRUD:** Implemented for at least 3 models (`Application`, `Inquiry`, `Sitter`).
* **Deployment:** Fully deployed and configured on **Render.com** utilizing PostgreSQL.
* **User Groups & Permissions:** Defined multiple user groups (Admin, Sitter, Client) in the Django Admin panel with distinct permissions and access control.

---

## Application Architecture

The project is structured into six Django apps with clear separation of responsibilities:

- **common** – Homepage, custom error pages (400, 403, 404, 500), contact form, and shared UI components.
- **services** – Service categorisation (`ServiceGroup` model).
- **sitters** – Sitter profiles, DRF endpoints, update views, and M2M Language relations.
- **inquiries** – Hiring requests made by clients and received by sitters.
- **recruitment** – Job applications for new sitters with Admin tracking.
- **accounts** – Custom user model, registration, login, logout, and profile management.
---
## Security

- CSRF protection enabled via Django middleware
- Protection against SQL injection through Django ORM
- XSS protection via template auto-escaping
- Sensitive data stored in environment variables (.env)
- Role-based access control enforced via View-level permissions

---

## Database Design

The application uses PostgreSQL as its database management system.

### Models
- `Sitter` – Core professional profile.
- `ServiceGroup` – Categorises service types.
- `Inquiry` – Client request tied to a specific sitter.
- `Application` – Recruitment application.
- `Language` – Spoken languages for sitters.
- `CustomUser` – Extends Django's `AbstractUser` for custom authentication.

### Relationships
- **Many-to-Many:** `Sitter` ↔ `ServiceGroup`, `Sitter` ↔ `Language`
- **Many-to-One (ForeignKey):** `Inquiry` → `Sitter`, `Inquiry` → `CustomUser` (Client), `Application` → `CustomUser`

---

## Features

### CRUD Functionality
Full CRUD operations are implemented via Class-Based Views (making up over 90% of views) for:
- `Application` (Manageable by Applicant/Admin)
- `Inquiry` (Manageable by Client/Admin)
- `Sitter` Profile (Updateable by the Sitter, Deletable by Admin)

Each delete operation includes a confirmation step.

### Forms & Validation
The project includes 7 fully validated forms (`ApplicationForm`, `InquiryForm`, `ContactForm`, `SitterUpdateForm`, `CustomUserCreationForm`, `CustomUserChangeForm`, `CustomAuthenticationForm`).

**Validation Features:**
- Custom server-side validation (e.g., name constraints, phone number length).
- Field-level and form-level validation
- Disabled/read-only fields (e.g., email field disabled during updates, hourly rate strictly admin-controlled).
- Customised labels, help texts, and placeholders.
- Excluded unnecessary fields
- User-friendly validation messages

### Technical Note on the Contact Form
The global **Contact Form** (accessible via the main navigation) is designed for general agency inquiries. To facilitate easy testing without requiring live SMTP server credentials, the project utilizes Django's `console.EmailBackend`. When a user submits a contact form, the email is successfully processed by Django and printed directly to the server console/logs instead of an actual inbox. *(Note: Sitter-specific hiring requests are handled differently via the `Inquiry` model and are saved directly to the database and user dashboards).*

---

### Views
The project handles business logic primarily through **Class-Based Views (over 90% CBVs)** including `ListView`, `DetailView`, `CreateView`, `UpdateView`, and `DeleteView`.
- Properly handles GET and POST requests.
- Validates forms before saving and redirects upon successful submissions.
- Restricts access using robust View-level permissions (`LoginRequiredMixin`, `UserPassesTestMixin`).

---

### Templates
- **15+ templates** using the Django Template Engine.
- **10+ dynamic templates** displaying and filtering database data.
- Base template with inheritance and reusable partials (navigation, footer).
- Conditional rendering based on user authentication status and roles.
- Custom error pages (400, 403, 404, 500).
- No orphan pages; all pages are seamlessly accessible through navigation links.
- Fully responsive layout powered by Bootstrap.
- All pages are accessible through navigation links (no orphan pages)
- Consistent navigation menu and footer across all templates

---

## Live Testing Instructions

To evaluate the core business logic of the application, please follow these step-by-step testing scenarios using the provided test accounts:

### Scenario 1: End-to-End Recruitment & Admin Capabilities
1. **Submit Application:** Create an account and log in as a regular user(sitter), click "Присъедини се към нас" and submit a new Sitter application.
2. **Admin Review:** Log in as **Admin**. Navigate to the "Кандидатури (HR)" dashboard. 
3. **Status Change & Profile Generation:** Edit the application you just created and change its status to "Approved/Hired". This triggers a Django signal that automatically generates a Sitter profile.
4. **Verify Sitter:** Go to the Sitters list page and verify the new sitter now appears.
5. **Admin Deletion:** As the Admin, click the "Delete" button on the newly created sitter's profile to test the restricted SitterDeleteView. Verify the custom confirmation page routes correctly.

### Scenario 2: Client & Sitter Interactions (Inquiries)
1. **Client Action:** Log in as **Client**. Go to a Sitter's profile and click "Наеми" (Hire) to test the Create Inquiry functionality.
2. **Sitter Action:** Log out, then log in as the **Sitter**. Check your dashboard by clicking 'Запитвания' to view the received inquiry.
3. **Profile Update:** While logged in as the Sitter, test the Update functionality by editing your own profile details (Note: the hourly rate is read-only for sitters but can be changed from the admin user).

### Scenario 3: Data Validation
Submit an application or inquiry form with intentional mistakes to observe custom server-side validation errors (`clean()` logic):
* **Application Form:** Enter a phone number shorter than 10 digits, or write a short bio under 20 characters.
* **Sitter Profile Update:** Log in as a Sitter, edit your profile, and enter a negative number for "Experience (in years)" or a bio shorter than 30 characters.

### Scenario 4: Custom Error Pages & Access Control (400, 403, 404, 500)
The application handles custom error routing for better UX. To test them:
* **403 Forbidden:** Log in as a **Client**. Go to the Sitters list and click on any Sitter to view their profile. Look at the URL in your browser (it will look something like `/sitters/1/`). Manually type `edit/` or `delete/` at the very end of that URL (e.g., `/sitters/1/edit/`) and press Enter. You will be successfully blocked by the `UserPassTestMixin` and shown the custom 403 page.
* **404 Not Found:** Navigate to a non-existing URL (e.g., `/non-existing-page/`). The custom 404 template will display.
* *(Custom 400 Bad Request and 500 Internal Server Error pages are also fully implemented and will display automatically if server-level issues occur).*

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
SECRET_KEY=your-local-secret-key
DB_NAME=sitterhub_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
CLOUDINARY_URL=cloudinary://your_api_key_here
CELERY_BROKER_URL=redis://localhost:6379/0 

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

## Contributors
**Mario Kostadinov** – Developer  
*Developed as an individual project for the Django Advanced Regular Exam at SoftUni.*

## License
This project is licensed under the MIT License.  
Copyright (c) 2026 Mario Kostadinov