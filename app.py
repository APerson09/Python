from flask import Flask, render_template, request, redirect

app = Flask(__name__)

reminders = []

app.secret_key = "sdfhfgkjdshbfgthrtfd111!xgwesdgvd@@@@rtfderg"

@app.route("/", methods=["GET", "POST"])
def home():
  if request.method == "POST":
    new_reminder = request.form.get("reminder_txt")

    if new_reminder:
      reminders.append(new_reminder)
      return redirect("/")
  
  return render_template("index.html", reminders=reminders)

@app.route("/delete/<int:index>")
def deleteIndex(index):
  if 0 <= index < len(reminders):
        reminders.pop(index)
  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True)