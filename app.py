import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

reminders = []

app.secret_key = "sdfhfgkjdshbfgthrtfd111!xgwesdgvd@@@@rtfderg"

@app.route("/", methods=["GET", "POST"])
def uploadImage():
  if request.method == "POST":
    reminder_txt = request.form.get("reminder_txt")
    filename = None

    if "reminder_image" in request.files:
      file = request.files["reminder_image"]
      if file and file.filename != '':
        filename = secure_filename(file.filename)
        file.save(os.path.join('static', filename))

      if reminder_txt or filename:
        reminders.append({
            "text": reminder_txt,
            "image": filename
        })
      print("Tung tung tung sahur")
      return redirect(url_for('uploadImage'))
  return render_template('index.html', reminders=reminders)

@app.route("/delete/<int:index>")
def deleteIndex(index):
  if 0 <= index < len(reminders):
        reminders.pop(index)
  return redirect("/")



if __name__ == "__main__":
  app.run(debug=True)