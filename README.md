# 🚑PredictEM  – Emergency Medical Response System

SwiftCare is an intelligent emergency response platform designed to assist healthcare professionals in managing emergency situations efficiently.
The system integrates machine learning, optimization algorithms, caching, and real-time routing to automate patient triage, hospital selection, and ambulance dispatch.

The platform simulates a real-world emergency management system using FastAPI, Redis, PostgreSQL, and Random Forest ML models.

🌟 Key Features
🧠 AI-Powered Triage Prediction

Predicts patient triage category (Red / Yellow / Green) using a Random Forest model trained on 1000+ simulated emergency patient records.

⚡ High Performance API

Built using FastAPI with asynchronous architecture to handle high-throughput emergency requests.

🗄️ Database Integration

Patient records, triage results, and hospital information are stored in PostgreSQL using SQLAlchemy ORM.

🚀 Redis Caching

Frequently requested predictions are cached using Redis, significantly reducing API latency.

📊 Resource Optimization

Hospital resources (beds, doctors, ventilators) are optimized using Linear Programming (PuLP).

🚦 Priority Queue System

Patients are prioritized based on severity:

Red → Highest Priority
Yellow → Medium Priority
Green → Lowest Priority
🏥 Hospital Load Balancing

The system selects the hospital with the lowest load ratio to distribute patients efficiently.

🚑 Ambulance Routing

Uses Dijkstra’s Shortest Path Algorithm to determine the nearest hospital for ambulance dispatch.

🏗️ System Architecture
React Dashboard
       ↓
FastAPI Backend (Async)
       ↓
Redis Cache
       ↓
Random Forest Triage Model
       ↓
Priority Queue
       ↓
Hospital Load Balancer
       ↓
Resource Optimizer
       ↓
PostgreSQL Database
🛠️ Tech Stack
Backend

Python

FastAPI

SQLAlchemy

Redis

PostgreSQL

Docker

Machine Learning

Scikit-learn

Random Forest

Optimization

PuLP (Linear Programming)

Algorithms

Dijkstra Shortest Path

Priority Queue (Heap)

Frontend

React.js

📂 Project Structure
swiftcare/
│
├── api/
│   └── main.py
│
├── modules/
│   ├── data_processing.py
│   ├── models.py
│   ├── database.py
│   ├── models_db.py
│   ├── caching.py
│   ├── allocation.py
│   ├── priority_queue.py
│   ├── load_balancer.py
│   └── routing.py
│
├── data/
│   └── mock_patient_data.csv
│
├── swiftcare-dashboard/
│   └── React frontend
│
├── generate_data.py
├── create_tables.py
└── README.md
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/swiftcare.git
cd swiftcare
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Redis (Docker)
docker run -d -p 6379:6379 redis
5️⃣ Run PostgreSQL (Docker)
docker run -d -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=predictem postgres
6️⃣ Create Database Tables
python create_tables.py
7️⃣ Start Backend Server
uvicorn api.main:app --reload --port 8001

Swagger UI:

http://127.0.0.1:8001/docs
8️⃣ Run React Dashboard
cd swiftcare-dashboard
npm install
npm start

Open:

http://localhost:3000
🔗 API Endpoints
Triage Prediction
POST /triage

Example request:

{
  "heart_rate": 120,
  "blood_pressure": 80,
  "oxygen_level": 95,
  "injury_severity": 3
}

Response:

{
 "triage_category": "Yellow"
}
Resource Allocation
POST /allocate-resources
Ambulance Dispatch
GET /dispatch-ambulance

Response:

{
 "nearest_hospital": "Metro Hospital",
 "distance": 5
}
📈 Performance Improvements
Feature	Impact
Redis caching	Reduced API latency
Async FastAPI	Handles concurrent requests
Priority queue	Faster emergency handling
Load balancing	Prevents hospital overload
🔮 Future Enhancements

Planned improvements for future versions of SwiftCare:

🏥 Additional Dashboards

Hospital Admin Dashboard for updating hospital capacity and resources.

Monitoring Dashboard for visualizing emergency statistics and system performance.

🗺️ Live Emergency Map

Integrate Leaflet or Mapbox to visualize ambulance routes and hospital locations in real time.

📊 Real-Time Analytics

Emergency trends

Hospital load monitoring

Response time analytics

🔔 Notification System

Automated alerts to hospitals when a high-priority patient is dispatched.

☁️ Cloud Deployment

Deploy the system using Docker Compose and Kubernetes for scalable production infrastructure.

🎯 Project Goals

SwiftCare demonstrates how modern technologies such as machine learning, optimization algorithms, and distributed systems can be combined to build intelligent emergency response systems.

This project aims to simulate how AI-driven systems can assist healthcare infrastructure in reducing response time and improving patient outcomes during emergencies.

👩‍💻 Author

Prachi Sah
Software Engineer | Machine Learning & Backend Systems