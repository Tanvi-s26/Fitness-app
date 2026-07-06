\# 🏋️ FitTrack — Fitness Tracking App with Social Features



A full-stack fitness tracking web application built with Python (Flask), PostgreSQL, and deployed on AWS with a complete DevOps pipeline. This project is part of a portfolio showcasing end-to-end application development and cloud infrastructure skills.



\---



\## 📌 Project Overview



FitTrack allows users to log workouts, track their fitness progress, follow friends, and get AI-powered workout recommendations — all in one place.



\---



\## 🚀 Tech Stack



| Layer | Technology |

|-------|-----------|

| Frontend | HTML, CSS, JavaScript |

| Backend | Python, Flask |

| Database | PostgreSQL |

| Containerisation | Docker |

| Cloud | AWS (EC2, RDS, S3) |

| Reverse Proxy | Nginx |

| CI/CD | GitHub Actions |

| Monitoring | AWS CloudWatch |



\---



\## ✨ Features



\- 👤 User registration and authentication

\- 🏃 Workout logging (type, duration, calories)

\- 📊 Progress tracking with charts

\- 👥 Social feed — follow friends and see their activity

\- 💡 Workout recommendations based on history

\- 📱 Responsive design for mobile and desktop



\---



\## 🗂️ Project Structure



```

fitness-app/

│

├── app.py                  # Main Flask application entry point

├── requirements.txt        # Python dependencies

├── Dockerfile              # Docker container configuration

├── docker-compose.yml      # Multi-container setup

├── .github/

│   └── workflows/

│       └── deploy.yml      # GitHub Actions CI/CD pipeline

│

├── templates/              # HTML templates (Jinja2)

│   ├── base.html

│   ├── index.html

│   ├── login.html

│   └── dashboard.html

│

├── static/                 # CSS, JS, images

│   ├── css/

│   └── js/

│

├── models/                 # Database models

│   ├── user.py

│   └── workout.py

│

├── routes/                 # Flask route blueprints

│   ├── auth.py

│   └── workout.py

│

└── README.md

```



\---



\## ⚙️ Local Setup



\### Prerequisites



\- Python 3.10+

\- Git

\- PostgreSQL (or Docker)



\### Steps



```bash

\# 1. Clone the repository

git clone https://github.com/Tanvi-s26/Fitness-app.git

cd Fitness-app



\# 2. Create and activate virtual environment

python -m venv venv



\# Windows

venv\\Scripts\\activate



\# Mac/Linux

source venv/bin/activate



\# 3. Install dependencies

pip install -r requirements.txt



\# 4. Set up environment variables

cp .env.example .env

\# Edit .env with your database credentials



\# 5. Run the app

python app.py

```



The app will be running at `http://127.0.0.1:5000`



\---



\## 🐳 Running with Docker



```bash

docker-compose up --build

```



\---



\## ☁️ AWS Deployment Architecture



```

User → Nginx (Reverse Proxy)

&#x20;          ↓

&#x20;     EC2 Instance (Flask App)

&#x20;          ↓

&#x20;     RDS (PostgreSQL)     S3 (Static Files)

```



\---



\## 🔄 CI/CD Pipeline



Every push to the `main` branch triggers GitHub Actions to:



1\. Run tests

2\. Build Docker image

3\. Push to Amazon ECR

4\. Deploy to EC2 automatically



\---



\## 📅 Development Journey



This project was built as a day-by-day learning series:



| Day | Focus |

|-----|-------|

| Day 1 | Project setup, Flask basics, Git |

| Day 2 | HTML templates, user registration UI |

| Day 3 | Database setup, user auth (login/register) |

| Day 4 | Workout logging, social feed |

| Day 5 | Docker, AWS EC2 deployment |

| Day 6 | CI/CD pipeline, monitoring |



\---



\## 👩‍💻 Author



\*\*Tanvi\*\* — Master's student passionate about DevOps and cloud infrastructure.



\- GitHub: \[@Tanvi-s26](https://github.com/Tanvi-s26)




