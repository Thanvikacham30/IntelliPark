from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/booking")
def booking():
    return render_template("booking_vehicle.html")

@app.route("/slots")
def slots():
    return render_template("parking_slots.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")

if __name__ == "__main__":
    app.run(debug=True)