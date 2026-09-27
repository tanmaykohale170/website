from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TGPCET | AIML Practical Portal</title>

<style>
* { box-sizing: border-box; }

:root {
    --bg: #ffffff;
    --text: #202123;
    --side: #f7f7f8;
    --card: #ffffff;
    --border: #e5e5e5;
    --blue: #2563eb;
}

body.dark {
    --bg: #212121;
    --text: #ececec;
    --side: #171717;
    --card: #2b2b2b;
    --border: #444;
    --blue: #60a5fa;
}

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: var(--bg);
    color: var(--text);
    transition: 0.2s;
}

/* SIDEBAR */
.sidebar {
    position: fixed;
    left: 0;
    top: 0;
    width: 270px;
    height: 100vh;
    background: var(--side);
    padding: 20px 14px;
    border-right: 1px solid var(--border);
    z-index: 1000;
}

.logo {
    font-size: 25px;
    font-weight: bold;
    padding: 10px 12px 25px;
}

.search {
    width: 100%;
    padding: 12px;
    border: 1px solid var(--border);
    border-radius: 12px;
    background: var(--card);
    color: var(--text);
    margin-bottom: 20px;
}

.menu {
    list-style: none;
    padding: 0;
    margin: 0;
}

.menu li { margin: 5px 0; }

.menu a {
    display: block;
    padding: 13px 15px;
    color: var(--text);
    text-decoration: none;
    border-radius: 10px;
    font-size: 16px;
}

.menu a:hover { background: var(--border); }

.bottom {
    position: absolute;
    bottom: 20px;
    left: 14px;
    right: 14px;
}

.dark-button {
    width: 100%;
    padding: 12px;
    border: 1px solid var(--border);
    background: var(--card);
    color: var(--text);
    border-radius: 10px;
    cursor: pointer;
}

/* MAIN */
.main {
    margin-left: 270px;
    min-height: 100vh;
    padding: 30px;
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border);
    padding-bottom: 18px;
}

.topbar h2 { margin: 0; }

/* PROFILE */
.profile {
    margin-top: 35px;
    padding: 30px;
    border: 1px solid var(--border);
    border-radius: 18px;
    background: var(--card);
}

.profile h1 { margin-top: 0; }

.info {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin-top: 20px;
}

.info-box {
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 18px;
}

.info-box b {
    display: block;
    margin-bottom: 7px;
}

/* PROFESSOR */
.professor {
    margin-top: 25px;
    padding: 25px;
    border: 1px solid var(--border);
    border-radius: 18px;
    background: var(--card);
    display: flex;
    align-items: center;
    gap: 25px;
}

.professor-image {
    width: 120px;
    height: 120px;
    object-fit: cover;
    border-radius: 50%;
    background: var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 48px;
}

.professor h2 {
    margin: 0 0 8px;
}

.professor p {
    margin: 5px 0;
}

/* PRACTICALS */
.section-title { margin-top: 35px; }

.practicals {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 18px;
}

.card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 18px;
}

.card h3 { margin-top: 0; }

.card button {
    border: none;
    padding: 9px 15px;
    border-radius: 8px;
    background: var(--blue);
    color: white;
    cursor: pointer;
}

.card button:hover { opacity: 0.9; }

/* SEARCH RESULT */
#searchResult {
    margin-top: 15px;
    padding: 15px;
    border-radius: 10px;
    display: none;
    background: var(--card);
    border: 1px solid var(--border);
}

/* MODAL */
.modal-backdrop {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.55);
    align-items: center;
    justify-content: center;
    z-index: 2000;
    padding: 20px;
}

.modal {
    width: min(600px, 100%);
    background: var(--card);
    color: var(--text);
    border-radius: 16px;
    padding: 25px;
    border: 1px solid var(--border);
    box-shadow: 0 15px 50px rgba(0,0,0,0.25);
}

.modal-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}

.modal-head h2 { margin: 0; }

.modal-close {
    border: none;
    background: transparent;
    color: var(--text);
    font-size: 22px;
    cursor: pointer;
}

.output-box {
    padding: 18px;
    border-radius: 12px;
    background: var(--side);
    border: 1px solid var(--border);
    line-height: 1.6;
    white-space: pre-line;
}

/* CHAT BUTTON */
.chat-button {
    position: fixed;
    right: 25px;
    bottom: 25px;
    border: none;
    background: #2563eb;
    color: white;
    padding: 15px 22px;
    border-radius: 30px;
    font-size: 16px;
    cursor: pointer;
    box-shadow: 0 5px 20px #0004;
    z-index: 900;
}

/* MOBILE */
@media(max-width: 750px) {
    .sidebar { width: 220px; }

    .main {
        margin-left: 220px;
        padding: 18px;
    }

    .info { grid-template-columns: 1fr; }

    .practicals { grid-template-columns: 1fr; }
}

@media(max-width: 550px) {
    .sidebar {
        width: 75px;
        padding: 10px;
    }

    .logo {
        font-size: 0;
        text-align: center;
    }

    .logo::after {
        content: "TG";
        font-size: 22px;
    }

    .menu a {
        text-align: center;
        font-size: 0;
    }

    .menu a span { font-size: 22px; }

    .search {
        font-size: 0;
        padding: 12px 5px;
    }

    .bottom {
        left: 10px;
        right: 10px;
    }

    .dark-button { font-size: 0; }

    .dark-button span { font-size: 20px; }

    .main { margin-left: 75px; }

    .professor {
        flex-direction: column;
        text-align: center;
    }
}
</style>
</head>

<body>

<!-- SIDEBAR -->
<div class="sidebar">
    <div class="logo">TGPCET</div>

    <input
        class="search"
        id="searchBox"
        type="text"
        placeholder="🔍 Search"
        oninput="searchWebsite()"
    >

    <ul class="menu">
        <li><a href="#images"><span>🖼️</span> Images</a></li>
        <li><a href="#library"><span>📚</span> Library</a></li>
        <li><a href="#projects"><span>📁</span> Projects</a></li>
        <li><a href="#scheduled"><span>🕒</span> Scheduled</a></li>
        <li><a href="#plugins"><span>🔌</span> Plugins</a></li>
    </ul>

    <div class="bottom">
        <button class="dark-button" onclick="darkMode()">
            <span>🌙</span> Dark Mode
        </button>
    </div>
</div>

<!-- MAIN CONTENT -->
<div class="main">

    <div class="topbar">
        <h2>TGPCET Machine Learning</h2>
        <div>🎓 AIML</div>
    </div>

    <!-- PROFILE -->
    <section class="profile">
        <h1>Welcome to Machine Learning Practicals</h1>

        <p>
            This website contains Machine Learning practical programs,
            outputs and student information.
        </p>

        <div class="info">

            <div class="info-box">
                <b>👨‍🎓 Student Name</b>
                Tanmay N. Kohale
            </div>

            <div class="info-box">
                <b>🆔 Roll Number</b>
                26510113
            </div>

            <div class="info-box">
                <b>🏫 Department</b>
                Artificial Intelligence and Machine Learning
            </div>

            <div class="info-box">
                <b>👨‍🏫 Machine Learning Coordinator</b>
                Prof. Praney Sir
            </div>

        </div>
    </section>

    <!-- FACULTY -->
    <section class="professor">
        <div class="professor-image">👨‍🏫</div>

        <div>
            <h2>AIML Faculty</h2>
            <p><strong>Coordinator:</strong> Prof. Praney Sir</p>
            <p>Department: Artificial Intelligence and Machine Learning</p>
        </div>
    </section>

    <div id="searchResult"></div>

    <!-- PRACTICALS -->
    <h2 class="section-title" id="projects">
        📁 Machine Learning Practicals
    </h2>

    <div class="practicals">

        <div class="card practical-card"
             data-search="practical 1 introduction machine learning">
            <h3>Practical 1</h3>
            <p>Introduction to Machine Learning</p>
            <button onclick="showOutput(1)">View Output</button>
        </div>

        <div class="card practical-card"
             data-search="practical 2 data preprocessing">
            <h3>Practical 2</h3>
            <p>Data Preprocessing</p>
            <button onclick="showOutput(2)">View Output</button>
        </div>

        <div class="card practical-card"
             data-search="practical 3 linear regression">
            <h3>Practical 3</h3>
            <p>Linear Regression</p>
            <button onclick="showOutput(3)">View Output</button>
        </div>

        <div class="card practical-card"
             data-search="practical 4 logistic regression">
            <h3>Practical 4</h3>
            <p>Logistic Regression</p>
            <button onclick="showOutput(4)">View Output</button>
        </div>

        <div class="card practical-card"
             data-search="practical 5 decision tree classification">
            <h3>Practical 5</h3>
            <p>Decision Tree Classification</p>
            <button onclick="showOutput(5)">View Output</button>
        </div>

        <div class="card practical-card"
             data-search="practical 6 k nearest neighbors knn">
            <h3>Practical 6</h3>
            <p>K-Nearest Neighbors (KNN)</p>
            <button onclick="showOutput(6)">View Output</button>
        </div>

        <div class="card practical-card"
             data-search="practical 7 support vector machine svm">
            <h3>Practical 7</h3>
            <p>Support Vector Machine</p>
            <button onclick="showOutput(7)">View Output</button>
        </div>

        <div class="card practical-card"
             data-search="practical 8 artificial neural network ann">
            <h3>Practical 8</h3>
            <p>Artificial Neural Network</p>
            <button onclick="showOutput(8)">View Output</button>
        </div>

        <div class="card practical-card"
             data-search="practical 9 machine learning model evaluation">
            <h3>Practical 9</h3>
            <p>Machine Learning Model Evaluation</p>
            <button onclick="showOutput(9)">View Output</button>
        </div>

    </div>

    <!-- OTHER SECTIONS -->
    <section class="card" id="images">
        <h2>🖼️ Images</h2>
        <p>Add your practical diagrams, graphs and college images here.</p>
    </section>

    <section class="card" id="library">
        <h2>📚 Library</h2>
        <p>Machine Learning notes, programs and study material.</p>
    </section>

    <section class="card" id="scheduled">
        <h2>🕒 Scheduled</h2>
        <p>Practical submission and study schedule.</p>
    </section>

    <section class="card" id="plugins">
        <h2>🔌 Plugins</h2>
        <p>Useful Machine Learning tools and resources.</p>
    </section>

</div>

<!-- CHAT BUTTON -->
<button class="chat-button" onclick="showMessage()">💬 Chat</button>

<!-- OUTPUT MODAL -->
<div class="modal-backdrop" id="outputModal"
     onclick="if(event.target === this) closeModal()">

    <div class="modal">
        <div class="modal-head">
            <h2 id="modalTitle">Practical Output</h2>
            <button class="modal-close" onclick="closeModal()">✕</button>
        </div>

        <div class="output-box" id="modalBody"></div>
    </div>
</div>

<!-- CHAT MODAL -->
<div class="modal-backdrop" id="chatModal"
     onclick="if(event.target === this) closeChat()">

    <div class="modal">
        <div class="modal-head">
            <h2>💬 TGPCET ML Assistant</h2>
            <button class="modal-close" onclick="closeChat()">✕</button>
        </div>

        <p>Welcome to the TGPCET Machine Learning website.</p>

        <div class="output-box">
Student: Tanmay N. Kohale
Roll No: 26510113
Department: Artificial Intelligence and Machine Learning
Coordinator: Prof. Praney Sir
        </div>
    </div>
</div>

<script>

/* DARK MODE */
function darkMode() {
    document.body.classList.toggle("dark");

    localStorage.setItem(
        "darkMode",
        document.body.classList.contains("dark") ? "on" : "off"
    );
}

if (localStorage.getItem("darkMode") === "on") {
    document.body.classList.add("dark");
}


/* SEARCH */
function searchWebsite() {
    const input = document
        .getElementById("searchBox")
        .value
        .trim()
        .toLowerCase();

    const result = document.getElementById("searchResult");
    const cards = document.querySelectorAll(".practical-card");

    let matches = 0;

    cards.forEach(card => {
        const text = card.dataset.search || "";
        const show = !input || text.includes(input);

        card.style.display = show ? "" : "none";

        if (show && input) {
            matches++;
        }
    });

    if (!input) {
        result.style.display = "none";
        return;
    }

    result.textContent =
        matches +
        " practical" +
        (matches === 1 ? "" : "s") +
        ' found for "' +
        input +
        '".';

    result.style.display = "block";
}


/* PRACTICAL OUTPUT */
const practicalOutputs = {
    1: [
        "Introduction to Machine Learning",
        "Machine Learning enables systems to learn patterns from data and make predictions or decisions."
    ],

    2: [
        "Data Preprocessing",
        "Typical stages include handling missing values, encoding categorical data, scaling numerical features, and splitting data into training and testing sets."
    ],

    3: [
        "Linear Regression",
        "A fitted regression line is generated from training data and can be used to predict a continuous target."
    ],

    4: [
        "Logistic Regression",
        "The classifier estimates class probabilities and assigns observations to a class."
    ],

    5: [
        "Decision Tree Classification",
        "A tree of feature-based decisions is trained to classify observations."
    ],

    6: [
        "K-Nearest Neighbors (KNN)",
        "Each sample is classified using the majority class among its nearest neighbors."
    ],

    7: [
        "Support Vector Machine",
        "An SVM learns a decision boundary that separates classes using a maximum-margin approach."
    ],

    8: [
        "Artificial Neural Network",
        "A neural network learns weights through training and produces predictions for new inputs."
    ],

    9: [
        "Machine Learning Model Evaluation",
        "Common evaluation outputs include accuracy, precision, recall, F1-score, confusion matrix, and regression error metrics."
    ]
};


function showOutput(number) {
    const data = practicalOutputs[number] || [
        "Practical Output",
        "No output has been added yet."
    ];

    document.getElementById("modalTitle").textContent =
        "Practical " + number + ": " + data[0];

    document.getElementById("modalBody").textContent = data[1];

    document.getElementById("outputModal").style.display = "flex";
}


function closeModal() {
    document.getElementById("outputModal").style.display = "none";
}


/* CHAT */
function showMessage() {
    document.getElementById("chatModal").style.display = "flex";
}


function closeChat() {
    document.getElementById("chatModal").style.display = "none";
}


/* ESC KEY */
document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
        closeModal();
        closeChat();
    }
});

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    print("TGPCET AIML Practical Portal")
    print("Open: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
