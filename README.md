# ♻️ EcoWaste - Web-Based Waste Management and Reporting System

![Django](https://img.shields.io/badge/Django-4.x-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Frontend-38BDF8)
![License](https://img.shields.io/badge/License-Educational-orange)

EcoWaste is a community-driven waste management platform that enables citizens to report waste issues, waste collectors to manage cleanup tasks, and administrators to verify completed work. The system aims to improve environmental cleanliness through transparency, accountability, and gamification.

---

## 📌 Project Overview

Rapid urbanization has increased waste generation, creating environmental and public health challenges. EcoWaste bridges the communication gap between citizens and municipal authorities by providing a centralized platform for reporting, tracking, and verifying waste cleanup activities.

The platform uses a role-based workflow and reward system to encourage community participation in maintaining a cleaner environment.

---

## ✨ Key Features

### 👤 Multi-Role Authentication System

* Reporter (Citizen)
* Collector (Waste Worker)
* Administrator

### ♻️ Waste Reporting

* Submit waste reports
* Add waste type and quantity
* Specify waste location
* Track report status

### 🚛 Collection Management

* View available collection requests
* Claim cleanup tasks
* Submit cleanup feedback

### ✅ Verification Workflow

* Admin verification and approval
* Report rejection with reasons
* Full report lifecycle tracking

### 🏆 Gamification

* Points-based reward system
* Community engagement incentives
* Performance tracking

---

## 🔄 Waste Report Lifecycle

```text
Citizen Reports Waste
          │
          ▼
      PENDING
          │
          ▼
Collector Claims Report
          │
          ▼
     COLLECTED
       /    \
      /      \
 VERIFIED   REJECTED
     │
     ▼
 Points Awarded
```

---

## 🛠 Technology Stack

| Category        | Technology          |
| --------------- | ------------------- |
| Backend         | Python, Django      |
| Frontend        | HTML5, Tailwind CSS |
| Database        | SQLite              |
| Authentication  | Django Auth         |
| Version Control | Git & GitHub        |

---

## 🏗 System Architecture

EcoWaste follows Django's **Model-View-Template (MVT)** architecture.

### Main Components

#### CustomUser

* Role Management
* Approval Status
* Reward Points

#### WasteReport

* Waste Type
* Location
* Amount
* Report Status
* Reporter & Collector Information

#### Feedback

* Cleanup Notes
* Collection Evidence

---

## 🔐 Security Features

* Django Authentication System
* Password Hashing
* Session Management
* Role-Based Authorization
* Protected Routes
* Custom Access Decorators

```python
@reporter_required
def reporter_dashboard(request):
    pass
```

---

## 📊 Functional Requirements

### User Management

* Registration
* Login
* Logout
* Role Assignment

### Waste Reporting

* Create Reports
* Track Reports
* Update Status

### Collection Management

* Claim Tasks
* Complete Collections
* Submit Feedback

### Administration

* Verify Reports
* Reject Invalid Reports
* Manage Users

---

## 🏆 Reward System

| Action              | Points |
| ------------------- | ------ |
| Submit Waste Report | +10    |
| Verified Cleanup    | +20    |

The reward system motivates users to contribute actively toward maintaining a cleaner environment.

---

## 📱 User Interface

* Responsive Design
* Mobile Friendly
* Glassmorphism Effects
* Smooth Animations
* Tailwind CSS Styling
* Shared Template Inheritance

---

## 🧪 Testing

### Authentication Testing

✔ Protected pages require login

### Authorization Testing

✔ Role restrictions enforced

### Lifecycle Testing

✔ Valid report status transitions

### Reward Testing

✔ Points allocated correctly

---

## 📂 Project Structure

```text
EcoWaste/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   └── forms.py
│
├── reports/
│   ├── models.py
│   ├── views.py
│   └── templates/
│
├── dashboard/
│   ├── views.py
│   └── templates/
│
├── static/
├── templates/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/ecowaste.git
cd ecowaste
```

### 2. Create Virtual Environment

```bash
python -m venv env
```

### 3. Activate Environment

**Windows**

```bash
env\Scripts\activate
```

**Linux/Mac**

```bash
source env/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run Server

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000
```

---

## 📸 Screenshots

Add screenshots here after deployment:

* Home Page
* Reporter Dashboard
* Collector Dashboard
* Admin Dashboard
* Waste Report Form

---

## 🔮 Future Enhancements

* AI-based Waste Detection
* Google Maps Integration
* Route Optimization
* Smart Bin Monitoring
* Mobile Application
* Real-world Reward System

---

## 📈 Benefits

* Improved Waste Management
* Increased Transparency
* Community Participation
* Better Accountability
* Cleaner Urban Environment

---

## 👨‍💻 Author

**Md. Nazmul Huda**
Department of Computer Science & Engineering
Rajshahi University of Engineering & Technology (RUET)

---

## 🎓 Academic Information

**Course:** CSE 3100 – Web Based Application Project
**Project:** EcoWaste – Web-Based Waste Management and Reporting System
**Supervisor:** Prof. Dr. Boshir Ahmed

---

## 📄 License

This project is part of the **Web Based Application Project** course at the **Department of Computer Science & Engineering, Rajshahi University of Engineering & Technology (RUET)**.


**Submitted By:**
Md. Nazmul Huda

**Supervisor:**
Prof. Dr. Boshir Ahmed
Professor, Department of CSE
Rajshahi University of Engineering & Technology (RUET)

This project was developed for academic and educational purposes only.

