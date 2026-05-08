# 🎟Ticket Booking System

A full-stack ticket booking system inspired by real-world platforms like BookMyShow, designed to handle concurrent booking requests using seat locking and expiry mechanisms.

## 🌐 Live Demo

Live Project: https://your-render-link.onrender.com

---

## 🚀 Key Features

- Real-time seat availability tracking
- Temporary seat locking system
- Automatic lock expiry after 60 seconds
- Booking confirmation workflow
- REST API-based backend architecture
- Concurrency handling to prevent double booking
- Interactive seat selection interface

---

## 📷 Project Preview

<img width="100%" alt="Ticket Booking System" src="screenshot.png">

---

## 🧠 Problem Statement

In real-world ticket booking platforms, multiple users may attempt to book the same seat simultaneously.

Without proper concurrency handling:
- Double booking can occur
- Data inconsistency issues arise
- Poor user experience

This project solves the problem using:
- Seat locking
- Expiry-based release
- Backend validation logic

---

## ⚙️ System Workflow

### 1️⃣ Seat Selection
User selects an available seat.

### 2️⃣ Temporary Locking
The selected seat is locked for 60 seconds so no other user can access it.

### 3️⃣ Booking Confirmation
After confirmation, seat status changes from `locked` → `booked`.

### 4️⃣ Lock Expiry
If booking is not confirmed within 60 seconds, the lock automatically expires and the seat becomes available again.

---

## 🔥 Core Concepts Implemented

- REST APIs
- Concurrency Handling
- Race Condition Prevention
- Seat Locking Mechanism
- Expiry Logic
- Backend Validation
- Database Relationships

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- SQLite

### Frontend
- HTML
- CSS
- JavaScript

---

# 📂 Project Structure

```bash
ticket-booking-system/
│
├── app.py
├── models.py
├── test_concurrency.py
├── requirements.txt
├── Procfile
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
```

---

## ▶️ Run Locally

### Clone Repository

```bash
git clone <your-github-repo-link>
cd ticket-booking-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000/
```

---

## 🧪 Concurrency Example

### User A
- Selects Seat S8
- Seat becomes temporarily locked

### User B
- Attempts to book the same seat
- Booking is denied until lock expires

This prevents duplicate bookings and race conditions.

---

## 🚀 Future Improvements

- User Authentication
- Payment Gateway Integration
- Redis-based Distributed Locking
- Real-time WebSocket Updates
- Admin Dashboard
- Dynamic Seat Pricing

---

## 💡 Learning Outcomes

Through this project, I gained practical experience in:
- Backend system design
- API development
- Database management
- Concurrency handling
- Real-world problem solving
- State management and validation logic

---

## 👩‍💻 Author

DIKSHA WAGHMARE
