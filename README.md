# Full-Stack Dynamic Personal Portfolio CMS

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/bk2821120-hub/bhola-saw-portfolio)

A modern, responsive, secure, and production-ready **Personal Portfolio Content Management System (CMS)** built with **Django**, **Bootstrap 5**, and **MySQL**.

---

## 🌟 Overview

The portfolio features two completely separate interfaces:
1. **Public Portfolio Website (`/`)** — Accessible to all visitors. Fully database-driven (no hard-coded project/skill/experience text).
2. **Custom Admin/CMS Portal (`/portal/`)** — Accessible only to the authenticated portfolio owner. Full CRUD control for Profile, Projects, Skills, Education, Experience, Certifications, Achievements, Blog, Documents/Resume, and Contact Messages.
3. **Django Built-in Admin (`/django-admin/`)** — Available separately for superuser database administration.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, Django 4.2 LTS
- **Frontend:** HTML5, CSS3, Bootstrap 5.3, JavaScript (ES6+), Bootstrap Icons
- **Database:** MySQL (production-ready & PythonAnywhere compatible)
- **Configuration:** `django-environ` with `.env` file
- **File Storage:** Django Media (organized uploads for profile, projects, certificates, resume, etc.)

---

## 📂 Project Architecture

```text
bhola-saw-portfolio/
│
├── manage.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── config/
│   ├── settings.py       # MySQL, Apps, Security, Static/Media setup
│   ├── urls.py           # Root routing for Portal, Public, and Superadmin
│   ├── wsgi.py           # WSGI entry point (PythonAnywhere)
│   └── asgi.py           # ASGI entry point
│
├── apps/
│   ├── accounts/         # Portal authentication, login/logout, dashboard stats
│   ├── portfolio/        # Profile, WebsiteSetting, SocialLinks, seed command
│   ├── projects/         # Projects & Technologies CRUD
│   ├── skills/           # Skill categories & Skills CRUD
│   ├── education/        # Academic credentials CRUD
│   ├── experience/       # Career timeline CRUD
│   ├── certifications/   # Certifications & Badges CRUD
│   ├── achievements/     # Honors & Hackathons CRUD
│   ├── blog/             # Blog Articles & Tags CRUD
│   ├── documents/        # PDF & Resume Document Manager
│   ├── services/         # Freelance Services & Client Deliverables CRUD
│   └── contact/          # Inquiries inbox with budget & timeline options
│
├── templates/
│   ├── base/             # Public base layout
│   ├── public/           # 13 public pages (Home, About, Projects, etc.)
│   ├── admin_panel/      # Custom CMS portal pages & CRUD templates
│   └── components/       # Reusable UI cards, navbar, footer, pagination
│
├── static/
│   ├── css/              # style.css, responsive.css, admin.css
│   └── js/               # main.js, animations.js, admin.js
│
└── media/                # Dynamic uploads (profile, projects, resume, etc.)
```

---

## 🚀 Quick Start & Local Setup

### 1. Prerequisites
- Python 3.10 or higher
- MySQL Server installed and running locally

### 2. Create MySQL Database
Log into MySQL:
```sql
CREATE DATABASE portfolio_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Configure Environment Variables (`.env`)
Update the `.env` file in the root directory:
```env
SECRET_KEY=your-secure-secret-key
DEBUG=True

# MySQL Settings
DB_NAME=portfolio_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306

ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin Owner)
```bash
python manage.py createsuperuser
```

### 7. Seed Initial Sample Data (Bhola Kumar Profile)
```bash
python manage.py seed_data
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit:
- **Public Website:** `http://127.0.0.1:8000/`
- **Owner CMS Portal:** `http://127.0.0.1:8000/portal/login/`
- **Django Superadmin:** `http://127.0.0.1:8000/django-admin/`

---

## 🌐 URL Routes Reference

### Public Routes
| URL | View Description |
|-----|------------------|
| `/` | Home / Hero / Featured Summary |
| `/about/` | Detailed About & Bio |
| `/skills/` | Categorized Skills & Levels |
| `/projects/` | Projects Listing with Category Filters |
| `/projects/<slug>/` | Project Details & Architecture |
| `/experience/` | Professional Career Timeline |
| `/education/` | Academic Journey & Qualifications |
| `/certifications/` | Verified Credentials & Certificates |
| `/achievements/` | Awards & Hackathons |
| `/blog/` | Technical Articles & Writing |
| `/blog/<slug>/` | Full Blog Post & Tags |
| `/resume/` | Active Resume Viewer (Embedded PDF) |
| `/contact/` | Contact Form & Social Links |

### Owner CMS Portal Routes
| URL | Description |
|-----|-------------|
| `/portal/login/` | Secure Owner Authentication |
| `/portal/logout/` | End Admin Session |
| `/portal/dashboard/` | CMS Metrics & Quick Actions |
| `/portal/profile/` | Update Bio, Title, Location, Photos |
| `/portal/settings/` | Site Name, Colors, SEO Meta |
| `/portal/social-links/` | Manage Social Profile Links |
| `/portal/skills/` | Manage Skills & Stacks |
| `/portal/projects/` | Manage Projects & Demos |
| `/portal/experience/` | Manage Work Roles |
| `/portal/education/` | Manage Academic Records |
| `/portal/certifications/` | Upload & Manage Certificates |
| `/portal/achievements/` | Manage Honors & Awards |
| `/blog/` | Draft, Edit & Publish Articles |
| `/portal/documents/` | Upload Resumes & Set Active Version |
| `/portal/messages/` | Read, Filter & Delete Visitor Inquiries |

---

## ☁️ PythonAnywhere Deployment Guide

1. **Upload / Clone Repository** into your PythonAnywhere account.
2. **Create a MySQL Database** in the **Databases** tab on PythonAnywhere.
   - Note the Database Hostname, Database Name, Username, and Password.
3. **Configure `.env`** on PythonAnywhere:
   ```env
   SECRET_KEY=production-secure-random-key
   DEBUG=False
   DB_NAME=username$portfolio_db
   DB_USER=username
   DB_PASSWORD=your_mysql_password
   DB_HOST=username.mysql.pythonanywhere-services.com
   DB_PORT=3306
   ALLOWED_HOSTS=username.pythonanywhere.com
   ```
4. **Create a Virtualenv and Install Requirements:**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 portfolio-env
   pip install -r requirements.txt
   ```
5. **Run Migrations & Collect Static:**
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   python manage.py seed_data
   ```
6. **Configure Web Tab:**
   - Source directory: `/home/username/Anuraj_Po`
   - Virtualenv: `/home/username/.virtualenvs/portfolio-env`
   - Static files mapping:
     - URL: `/static/` ➔ Directory: `/home/username/Anuraj_Po/staticfiles`
     - URL: `/media/` ➔ Directory: `/home/username/Anuraj_Po/media`
7. **Configure WSGI Configuration File** (`/var/www/username_pythonanywhere_com_wsgi.py`):
   ```python
   import os
   import sys

   path = '/home/username/Anuraj_Po'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
8. **Reload the Web App.** Your portfolio CMS is live!

---

## 🛡️ Security Best Practices
- Strict CSRF Protection on all forms
- Protected routes using Django `@login_required`
- Clean decoupling of credentials via `.env`
- Passwords securely hashed with PBKDF2
- Upload validators for file types and sizes
