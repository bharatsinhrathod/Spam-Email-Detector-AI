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
<img width="1906" height="919" alt="Home" src="https://github.com/user-attachments/assets/e200a237-<img width="1897" height="909" alt="Login" src="https://github.com/user-attachments/assets/bdf886d1-4d30-4a62-9e21-355cb0245e37" /><img width="1876" height="906" alt="Admin" src="https://github.com/user-attachments/assets/20261ea7-5fcd-4fee-a5b5-85a85cd427aa" />

f1dc-4d0c-ad01-bf2f789960f1" />

<img width="1895" height="906" alt="Detector" src="https://github.com/user-attachments/assets/cb822240-8ed7-48e5-9876-934486a02573" />

## 🛠️ Tech Stack![Uploading Login.png…]()


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
