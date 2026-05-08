from flask import Flask, render_template, jsonify, request
from models import db, Event, Seat
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create DB + Sample Data
def create_tables():
    with app.app_context():
        db.create_all()

        if not Event.query.first():
            event = Event(name="Avengers Movie")
            db.session.add(event)
            db.session.commit()

            # Create 20 seats
            for i in range(1, 21):
                seat = Seat(seat_number=f"S{i}", event_id=event.id)
                db.session.add(seat)

            db.session.commit()


# API: Get all seats
@app.route("/seats")
def get_seats():
    release_expired_locks()
    seats = Seat.query.all()
    data = []

    for seat in seats:
        data.append({
            "id": seat.id,
            "seat_number": seat.seat_number,
            "status": seat.status
        })

    return jsonify(data)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# API: Book a seat
@app.route("/book", methods=["POST"])
def book_seat():
    data = request.get_json()
    seat_id = data.get("seat_id")

    seat = Seat.query.get(seat_id)

    if not seat:
        return jsonify({"message": "Seat not found"}), 404

    # Only allow booking if seat is locked
    if seat.status != "locked":
        return jsonify({"message": "Seat must be locked before booking"}), 400

    seat.status = "booked"
    seat.lock_time = None
    db.session.commit()

    return jsonify({"message": "Seat booked successfully"})



LOCK_DURATION = 60  # seconds

@app.route("/lock", methods=["POST"])
def lock_seat():
    release_expired_locks()
    data = request.get_json()
    seat_id = data.get("seat_id")

    seat = Seat.query.get(seat_id)

    if not seat:
        return jsonify({"message": "Seat not found"}), 404

    # If already booked
    if seat.status == "booked":
        return jsonify({"message": "Seat already booked"}), 400

    # If locked, check expiry
    if seat.status == "locked":
        if seat.lock_time and datetime.utcnow() - seat.lock_time < timedelta(seconds=LOCK_DURATION):
            return jsonify({"message": "Seat is temporarily locked"}), 400

    # Lock the seat
    seat.status = "locked"
    seat.lock_time = datetime.utcnow()
    db.session.commit()

    return jsonify({"message": "Seat locked successfully"})

def release_expired_locks():
    seats = Seat.query.filter_by(status="locked").all()
    for seat in seats:
        if seat.lock_time and datetime.utcnow() - seat.lock_time > timedelta(seconds=LOCK_DURATION):
            seat.status = "available"
            seat.lock_time = None
    db.session.commit()

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)