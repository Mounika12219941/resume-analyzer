from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# simple skill list
skills_list = ["python", "java", "c++", "sql", "html", "css", "javascript"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("resume")
    
    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # read file content (simple text only)
        content = file.read().decode("utf-8", errors="ignore")

        # word count
        words = len(content.split())

        # skill detection
        found_skills = []
        for skill in skills_list:
            if skill in content.lower():
                found_skills.append(skill)

        return render_template("result.html", words=words, skills=found_skills)

    return "Upload failed"

if __name__ == "__main__":
    app.run(debug=False)
