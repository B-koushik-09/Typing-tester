# ⌨️ SwiftType ─ Your Ultimate Typing Companion

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://git-scm.com/download/win) 
![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**SwiftType** is a modern, minimalist web application built with Streamlit to help you measure and improve your typing speed and accuracy. Test your skills against random paragraphs, get real-time feedback, and track your progress in WPM and Accuracy Percentage.

---

## 🌟 Features

| Feature | Description |
| :--- | :--- |
| **⚡ Real-time Calculation** | Instantly calculates your **WPM** (Words Per Minute) and **Accuracy %**. |
| **🔍 Error Highlighting** | Visual comparison with color-coded feedback (Green: Correct, Red: Error). |
| **💡 Dynamic Paragraphs** | Randomized text selection to keep your practice sessions fresh. |
| **🎨 Minimal UI** | Clean, distraction-free interface designed for maximum focus. |
| **🔄 Quick Restart** | Seamlessly reset the test for another round with a single click. |

---

## 🛠️ Tech Stack

*   **Frontend/Backend:** [Streamlit](https://streamlit.io/)
*   **Metric Analysis:** Python `difflib` for intelligent text comparison.
*   **Logic:** Python 3.10+

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.10 or higher installed on your system.

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/B-koushik-09/Typing-tester
    cd typing-tester
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

Launch the application with the following command:
```bash
streamlit run app.py
```
Wait for the local server to start, and follow the link provided in your terminal (usually `http://localhost:8501`).

---

## 📖 How to Use

1.  **Analyze**: Look at the displayed paragraph in the blue text box.
2.  **Type**: Start typing the text into the large text area below. The timer starts automatically as you begin typing!
3.  **Submit**: Click the **✅ Submit** button once you've finished.
4.  **Review**: Check your WPM, Accuracy, and the detailed character comparison to find areas for improvement.

---

## 📊 Evaluation Logic

*   **WPM (Words Per Minute):** Calculated based on total words typed and total elapsed time.
*   **Accuracy:** Derived using the `SequenceMatcher` ratio between the target paragraph and your input.

---

## 📈 Roadmap / Future Improvements

- [ ] Support for multiple difficulty levels (Easy, Medium, Hard).
- [ ] Global Leaderboard to compete with other users.
- [ ] Dark/Light mode toggle for custom user experience.
- [ ] Save history to track typing speed growth over time.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

