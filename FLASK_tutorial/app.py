from flask import Flask, render_template, request

app = Flask(__name__)
"""
name="vivek pawar"
about = "AI & ML undergraduate with hands-on experience building automation-driven backend and full-stack applications using Python, Flask, and modern web technologies. Strong focus on converting unstructured data into actionable insights through web scraping, APIs, and data analysis. Actively seeking internship roles in Python development, data analytics, or AI-assisted systems."
skills = ["programmer","python", "flask"]
projects = {
    "Linkedin Profile Analyzer": "A flask & playwright based web scraper that scraper linkedin profile data and pass it to gemini api to summarize that data and give overview about profile.",
    "Auto Portfolio Builder": "automatically generates professional portfolio based on given resume or github profile  or linkedin profile",
    "Decision-Driven Data Analysis System": "A system that performs data analysis and generates report based on the pre-defined rules"
    }
email="contact.vivekpawar@gmail.com"
"""

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/portfolio', methods=["POST"])
def portfolio():
    name = request.form.get("name")
    about = request.form.get("about","")
    email = request.form.get("email","")

    # Convert skills string into list
    skills_raw = request.form.get("skills", "")
    skills = [skill.strip() for skill in skills_raw.split(",") if skill.strip()]

     # Convert projects string into dictionary
    projects_raw = request.form.get("projects", "")
    projects = {}
    for item in projects_raw.split(";"):
        if "|" in item:
            pname, desc = item.split("|", 1) #splits into atmost 2 elements only
            projects[pname.strip()] = desc.strip()
    
    return render_template("index.html", name=name, about=about, email=email, skills=skills, projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
