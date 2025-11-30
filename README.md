# 📧 SpamShield AI - Intelligent Email Spam Detector

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

**SpamShield AI** is a Full-Stack Web Application that uses Machine Learning to detect whether an email is **Spam** or **Safe (Ham)**. It features a modern "Glassmorphism" UI, secure user authentication, and an administrative dashboard to track user growth.

## 🚀 Features

* **Machine Learning Engine:** Uses a Naive Bayes classifier trained on thousands of email samples.
* **Real-time Detection:** Instant analysis of email text with visual feedback (Safe/Spam indicators).
* **Secure Authentication:** User Login and Registration system with hashed passwords.
* **Admin Dashboard:** Specialized panel to view registered users and monitor platform growth.
* **Modern UI/UX:** Responsive design featuring Glassmorphism, CSS animations, and Dark Mode.

## 🛠️ Tech Stack

* **Backend:** Python, Flask, SQLAlchemy (Database)
* **Machine Learning:** Scikit-learn, Pandas, Joblib (Model Persistence)
* **Frontend:** HTML5, CSS3 (Custom animations & Glassmorphism)
* **Database:** SQLite (Local storage)

## 📂 Project Structure

```bash
Spam-Email-Detector-AI/
│
├── app.py                # Main Flask Application (Backend & Routes)
├── train_model.py        # ML Training Script (Run this first)
├── spam_model.pkl        # Trained Model (Generated file)
├── vectorizer.pkl        # Text Vectorizer (Generated file)
├── requirements.txt      # List of dependencies
├── instance/             # Database storage
│
└── templates/            # Frontend HTML files
    ├── home.html         # Landing Page
    ├── login.html        # Authentication Page
    ├── detector.html     # User Dashboard (The Spam Checker)
    └── admin.html        # Admin Control Panel
