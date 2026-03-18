# 🔐 Secure Pass: Modern Password Generator

![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)

A sleek, responsive, and secure password generation tool built with Django. It features a modern Glassmorphism UI, customizable generation logic, and instant "Copy to Clipboard" functionality.

## ✨ Key Features

- **💎 Modern UI:** High-end Glassmorphism design with dynamic radial gradients.
- **⚙️ Fully Customizable:** Choose password length and toggle uppercase, numbers, and special characters.
- **📋 One-Click Copy:** Instant copy functionality for generated passwords.
- **🌓 Adaptive Theme:** Designed to look great in both light and dark environments.
- **📱 Responsive Design:** Optimized for mobile and desktop screens.
- **🛡️ Secure Generation:** Uses Python's internal logic for robust character randomization.

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Installation
```bash
# Clone the repository
git clone git@github.com:Alfacentauree/password-generetor.git
cd password-generetor

# Setup Virtual Environment
python3 -m venv venv
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt
```

### 2. Database & Setup
```bash
python manage.py migrate
```

### 3. Run the App
```bash
python manage.py runserver
```
Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to start generating secure passwords!

---

## 🛠️ Technology Stack

- **Backend:** Django 4.2
- **Frontend:** HTML5, CSS3 (Modern Glassmorphism)
- **Fonts:** Inter, Poppins, JetBrains Mono
- **Deployment:** Heroku Ready (includes Procfile & WhiteNoise)

## 🤝 Contributing
Contributions are always welcome! Feel free to fork the project and submit a PR.
