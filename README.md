# 🎓 Student Grade System

A simple and interactive **Student Grade System** built using **Python and Streamlit**.

The application allows students to enter their name and marks, calculates their grade, and displays a motivational message based on their performance.

## ✨ Features

* 👤 Takes the student's name as input.
* 📝 Takes marks between **0 and 100**.
* 📊 Displays a progress bar based on the entered mark.
* 🎯 Automatically calculates the grade.
* 💬 Displays a motivational quote based on the grade.
* 🎨 Uses custom CSS for a clean and attractive interface.
* 🛡️ Escapes the student's name before displaying it in HTML.
* 📱 Uses a centered and student-friendly layout.

## 📊 Grade System

| Mark   | Grade | Message                                                |
| ------ | ----- | ------------------------------------------------------ |
| 90–100 | 🏆 A  | Excellent work!                                        |
| 80–89  | 🌟 B  | Keep pushing yourself!                                 |
| 70–79  | ⭐ C   | Keep improving every day!                              |
| 60–69  | 💪 D  | Learn from your mistakes and move forward.             |
| 0–59   | ❤️ F  | Don't give up! One result does not define your future. |

## 🛠️ Technologies Used

* Python
* Streamlit
* HTML/CSS for interface styling

## 📁 Project Structure

```text
GEN AI_Streamlit/
│
├── grade_system.py
├── README.md
├── .gitignore
└── venv/
```

> The `venv` folder should not be uploaded to GitHub. Add `venv/` to `.gitignore`.

## 📦 Installation

First, install Streamlit:

```bash
pip install streamlit
```

## ▶️ Run the Application

Run the following command in the terminal:

```bash
streamlit run grade_system.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser to use the application.

## 🧑‍🎓 How It Works

1. Enter the student's name.
2. Enter the mark between 0 and 100.
3. Click **Calculate My Grade**.
4. The application calculates the grade.
5. The student's score and grade are displayed.
6. A motivational quote is shown based on the student's performance.

## 💡 Example

If the student enters:

```text
Name: Rohan
Mark: 85
```

The application displays:

```text
👋 Rohan, your score is
📊 85 / 100

🌟 B

"Great job! Keep pushing yourself and you can reach the top."
```

## 🎯 Purpose

This project was created as a beginner-friendly Streamlit application to demonstrate **user input, conditional statements, grade calculation, dynamic UI elements, and basic web interface styling using Python**.

## 👨‍💻 Author

**Rohan Arunachalam**
