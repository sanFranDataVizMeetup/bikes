from flask import Flask, render_template, redirect, request, flash
import model
import datetime

CONN = None
CURSOR = None

app = Flask(__name__)
app.secret_key = 'Bike\App\Secret\Key'


@app.route("/", methods=["GET"])
def index():
    return redirect("/survey")


@app.route("/survey", methods=["GET"])
def get_survey():
    return render_template("survey.html")


@app.route("/survey", methods=["POST"])
def process_survey():

    incident_date_from_input = request.form.get("date_incident")
    date_incident = datetime.datetime.strptime(incident_date_from_input, "%m/%d/%Y")

    new_incident = model.Incident(
        date_incident=date_incident,
        injury_severity=request.form.get("injury_severity"),
        road_cond_slope=request.form.get("road_cond_slope"),
        bike_path=request.form.get("bike_path"),
        riding_impaired=request.form.get("riding_impaired"),
        comments=request.form.get("comments"),
        date_reported=datetime.datetime.utcnow()
    )
    model.db_session.add(new_incident)
    model.db_session.commit()

    return redirect("/thankyou")


@app.route("/thankyou", methods=["GET"])
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
