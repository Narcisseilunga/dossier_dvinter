from flask import Flask, render_template, request, redirect, session, url_for

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

app.secret_key = "MonSuperSecret"

PASSWORD = "123456"

VIDEO_URL = "https://votre-video.mp4"


@app.route("/", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":

        if request.form["password"] == PASSWORD:

            session["ok"] = True

            return redirect("/video")

        error = "Mot de passe incorrect"

    return render_template("login.html", error=error)


@app.route("/video")
def video():

    if not session.get("ok"):

        return redirect("/")

    return render_template(
        "video.html",
        video=VIDEO_URL
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")