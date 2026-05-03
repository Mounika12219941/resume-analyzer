from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# simple skill list
skills_list = ["python", "java", "c++", "sql", "html", "css", "javascript", "react", "node", "machine learning"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    job_desc = request.form.get("jobdesc")
    file = request.files.get("resume")
    
    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        content = file.read().decode("utf-8", errors="ignore")
file.seek(0)
file.save(filepath)

        # word count
        words = len(content.split())


        # skill detection
        found_skills = []
        for skill in skills_list:
            if skill in content.lower():
                found_skills.append(skill)
                match_count = 0

if job_desc:
    job_desc = job_desc.lower()
    for skill in skills_list:
        if skill in content.lower() and skill in job_desc:
            match_count += 1

    match_percent = int((match_count / len(skills_list)) * 100)
else:
    match_percent = 0
                if not found_skills:
                     found_skills = ["No major skills detected"]
                    score = min(100, words // 10 + len(found_skills) * 10)
                    if words < 100:
    suggestion = "Your resume is too short. Add more skills, projects, and experience."
else:
    suggestion = "Good resume length

        return render_template("result.html", words=words, skills=found_skills, score=score, suggestion=suggestion)

    return "Upload failed"

if __name__ == "__main__":
    app.run(debug=False)
