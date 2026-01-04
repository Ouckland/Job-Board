
# Jobsphere — Smart Job Board Platform

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/) [![Django](https://img.shields.io/badge/django-5.2-green)](https://www.djangoproject.com/) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

🔗 **Live Demo:** [https://jobsphere-3kdi.onrender.com](https://jobsphere-3kdi.onrender.com)
👨‍💻 **Author:** [@Ouckland](https://github.com/Ouckland)
📧 **Email:** [iselekorede5@gmail.com](mailto:iselekorede5@gmail.com)
🔗 **LinkedIn:** [Korede Isele](https://www.linkedin.com/in/korede-isele-944016297/)

---

Jobsphere is a modern **Django-based job platform** that connects job seekers and employers seamlessly.
It offers **secure authentication, profile management, public profiles, job posting**, and **responsive dashboards** for both user types.

---

## Core Features

### Authentication System

* Email + password signup
* OTP verification with expiry
* Account type selection (Seeker / Employer)
* Profile completion required before login
* Session handling and welcome notifications
* Password reset via OTP

### Profile Management

* Abstract `Profile` model with shared fields
* Separate **SeekerProfile** and **EmployerProfile** models
* Full Create, Read, Update (no delete)
* Profile image and company logo upload
* Dynamic forms based on account type
* Real-time profile completion progress bar

### Public Profiles

* Each user has a public URL → `/profile/<username>/`
* Read-only profile view for visitors
* Public directory:

  * **Browse Candidates**
  * **Browse Employers**

### Dashboards

* **Job Seekers:**

  * Search & filter available jobs
  * View recommended jobs
  * Track applications and status updates

* **Employers:**

  * Post and manage jobs
  * View applicants per job
  * Monitor application stats

### Notifications

* AJAX-powered (mark as read without page reload)
* Sent for key actions (applications, profile updates, etc.)

### UI / UX

* dark theme 
* Fully responsive for mobile & desktop
* Reusable header with hamburger menu
* Glassmorphism design elements

---

## Application Review System *(In Progress)*

**For Employers:**

* View all applicants per job
* See applicant details & CV
* Update application status: Pending → Shortlisted → Interviewed → Hired / Rejected

**For Seekers:**

* Track all jobs applied to
* Monitor progress via clear status updates

---

## Future Enhancements (Phase 2)

* In-app messaging 💬
* Saved jobs & saved candidates
* Advanced job recommendations
* Employer analytics (views, reach)
* Subscription / payment system
* Async notifications with Celery + Redis

---

## Tech Stack

| Layer              | Technology                       |
| ------------------ | -------------------------------- |
| **Backend**        | Django (Python)                  |
| **Frontend**       | HTML5, CSS3, JavaScript          |
| **Database**       | SQLite (dev) / PostgreSQL (prod) |
| **Authentication** | Django auth + OTP                |
| **Hosting**        | Render (Free Tier)               |

---

## Quick Setup

```bash
# Clone the repository
git clone https://github.com/Ouckland/JobSphere.git
cd JobSphere

# Create virtual environment
python -m venv venv
# Activate venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run development server
python manage.py runserver
```


**Live Demo:** [https://jobsphere-3kdi.onrender.com](https://jobsphere-3kdi.onrender.com)


Do you want me to do that next?
