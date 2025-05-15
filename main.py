from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

quiz_questions = [
    {
        "question": "Co znamená HTML?",
        "options": {
            "A": "HyperText Markup Language",
            "B": "Home Tool Multi Language",
            "C": "Hot Text Mail Line"
        },
        "correct": "A"
    },
    {
        "question": "Na co slouží CSS?",
        "options": {
            "A": "Na psaní kódu serveru",
            "B": "Na připojení do databáze",
            "C": "Na stylování webových stránek"
        },
        "correct": "C"
    },
    {
        "question": "Který jazyk běží v prohlížeči a umožňuje interakci s uživatelem?",
        "options": {
            "A": "Python",
            "B": "JavaScript",
            "C": "SQL"
        },
        "correct": "B"
    },
    {
        "question": "Co dělá Flask?",
        "options": {
            "A": "Je to grafický program",
            "B": "Je to herní engine",
            "C": "Je to Python framework pro webové aplikace"
        },
        "correct": "C"
    },
    {
        "question": "Jaký je správný zápis HTML nadpisu?",
        "options": {
            "A": "<heading>",
            "B": "<h1>",
            "C": "<title>"
        },
        "correct": "B"
    },
    {
        "question": "K čemu slouží <form> v HTML?",
        "options": {
            "A": "Na vytváření obrázků",
            "B": "Na vytváření tabulek",
            "C": "Na odesílání dat (např. kvíz)"
        },
        "correct": "C"
    },
    {
        "question": "Co je to IP adresa?",
        "options": {
            "A": "Poštovní adresa",
            "B": "Jedinečné číslo počítače v síti",
            "C": "Kód barvy v CSS"
        },
        "correct": "B"
    },
    {
        "question": "Jaký je výstup Python kódu print(2 + 3 * 4)?",
        "options": {
            "A": "20",
            "B": "14",
            "C": "24"
        },
        "correct": "B"
    },
    {
        "question": "Který z těchto programů můžeš použít jako kódovací editor?",
        "options": {
            "A": "Spotify",
            "B": "Visual Studio Code",
            "C": "YouTube"
        },
        "correct": "B"
    },
    {
        "question": "Co znamená značka <a href='/'>Domů</a> v HTML?",
        "options": {
            "A": "Zobrazí obrázek",
            "B": "Vytvoří odkaz",
            "C": "Změní barvu textu"
        },
        "correct": "B"
    },
]

@app.route("/")
def home():
    name = "Petr"
    age = randint(10, 80)
    return render_template("home.html", user_name=name, user_age=age)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    result = None
    correct_count = 0
    #NOVINKA
    user_answers = []    

    if request.method == "POST":
        for i, q in enumerate(quiz_questions):
            user_answer = request.form.get(f"q{i}")
            #NOVINKA
            is_correct = user_answer == q["correct"]
            if is_correct:
                correct_count += 1
            user_answers.append({
                "question": q["question"],
                "options": q["options"],
                "user_answer": user_answer,
                "correct_answer": q["correct"],
                "is_correct": is_correct
            })
        result = f"Máš {correct_count} správných odpovědí z {len(quiz_questions)}!"

    return render_template("quiz.html", questions=quiz_questions, result=result, user_answers=user_answers)

if __name__ == "__main__":
    app.run(debug=True)
