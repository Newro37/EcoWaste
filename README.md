# ♻️ EcoWaste - Web-Based Waste Management and Reporting System

EcoWaste is a community-driven waste management platform that enables citizens to report waste issues, waste collectors to manage cleanup tasks, and administrators to verify completed work. The system aims to improve environmental cleanliness through transparency, accountability, and gamification.

## 📌 Project Overview

Rapid urbanization has increased waste generation, creating environmental and public health challenges. EcoWaste bridges the communication gap between citizens and municipal authorities by providing a centralized platform for reporting, tracking, and verifying waste cleanup activities.

The platform uses a role-based workflow and reward system to encourage community participation in maintaining a cleaner environment.

---

## 🚀 Features

### 👤 User Roles

#### Reporter (Citizen)

* Register and log in securely
* Report waste issues with location details
* Track submitted reports
* Earn points for verified reports

#### Collector (Waste Worker)

* View available waste collection tasks
* Claim pending reports
* Mark tasks as collected
* Submit cleanup feedback
* Earn points for verified collections

#### Administrator

* Approve collector accounts
* Monitor system activities
* Verify or reject collected reports
* Manage report lifecycle

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

## 🎯 Objectives

* Provide a secure role-based waste reporting system.
* Enable citizens to report waste easily.
* Improve communication between citizens and waste collectors.
* Introduce a gamified reward system.
* Ensure accountability through administrative verification.
* Promote environmental awareness and community engagement.

---

## 🛠 Technology Stack

### Backend

* Python 3
* Django Framework

### Frontend

* HTML5
* Tailwind CSS

### Database

* SQLite (Development)
* PostgreSQL (Future Production Upgrade)

### Version Control

* Git

---

## 🏗 System Architecture

EcoWaste follows Django's **Model-View-Template (MVT)** architecture.

### Core Components

#### CustomUser Model

Stores:

* User Role

  * REPORTER
  * COLLECTOR
  * ADMIN
* Account Status

  * PENDING
  * APPROVED
* Reward Points

#### WasteReport Model

Stores:

* Waste Type
* Location
* Amount
* Status
* Reporter Information
* Collector Information
* Verification Information

#### Feedback Model

Stores:

* Cleanup Notes
* Collection Evidence

---

## 🔐 Security Features

* Django Authentication System
* Password Hashing
* Role-Based Access Control
* Custom Authorization Decorators
* Session Protection
* Dashboard Access Restrictions

Example Authorization:

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

* Create waste reports
* Specify waste type
* Provide location details

### Task Management

* View pending reports
* Claim collection tasks
* Submit collection feedback

### Verification

* Approve completed cleanups
* Reject invalid submissions
* Provide rejection reasons

### Gamification

* Reward points for participation
* Encourage community engagement

---

## 🏆 Point System

| Action                    | Points |
| ------------------------- | ------ |
| Successful Waste Report   | 10     |
| Verified Waste Collection | 20     |

The point system motivates users to actively participate in environmental cleanup efforts.

---

## 📱 User Interface Features

* Responsive Design
* Mobile-Friendly Layout
* Glassmorphism UI Components
* Smooth Animations
* Tailwind CSS Styling
* Template Inheritance Structure

---

## 🧪 Testing

The following tests were performed:

### Authentication Testing

* Unauthorized users cannot access protected pages.

### Authorization Testing

* Users cannot access dashboards outside their roles.

### Lifecycle Testing

* Correct report status transitions.

### Point Allocation Testing

* Automatic reward assignment after verification.

---

## 📈 Benefits

* Improved waste management efficiency
* Increased transparency
* Community participation
* Accountability through verification
* Cleaner urban environments

---

## ⚠ Current Limitations

* Manual report verification
* No real-time GPS tracking
* No route optimization
* No smart-bin integration
* No external reward/payment system

---

## 🔮 Future Enhancements

* AI-based waste detection from images
* Google Maps integration
* Route optimization for collectors
* Smart waste-bin integration
* Real-world reward redemption system
* Mobile application development

---


## 📄 License

This project was developed as an academic project for educational and research purposes.
