import os

from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# -----------------------------
# Paramètres
# -----------------------------

VIDEO_NAME = "video.mp4"

PASSWORD = "123456PROSEC"

# -----------------------------
# Page de connexion
# -----------------------------

@app.route("/", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":

        password = request.form.get("password")

        if password == PASSWORD:

            session["connected"] = True

            return redirect(url_for("video"))

        error = "Mot de passe incorrect."

    return render_template("login.html", error=error)


# -----------------------------
# Lecture vidéo
# -----------------------------

@app.route("/video")
def video():

    if not session.get("connected"):

        return redirect(url_for("login"))

    return render_template("video.html")


# -----------------------------
# Flux vidéo
# -----------------------------

@app.route("/stream")
def stream():

    print("UPLOAD_FOLDER :", app.config.get("UPLOAD_FOLDER"))

    print("EXISTE :", os.path.exists(app.config.get("UPLOAD_FOLDER", "")))

    print("VIDEO :", os.path.exists(
        os.path.join(app.config.get("UPLOAD_FOLDER", ""), "video.mp4")
    ))

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        VIDEO_NAME
    )

# -----------------------------
# Déconnexion
# -----------------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":

    app.run(debug=True)
