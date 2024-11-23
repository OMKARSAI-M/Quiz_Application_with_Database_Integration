# Quiz_Application_with_Database_Integration
## Introduction
  This project is a fully functional Quiz Application that integrates Python programming, SQLite database management, and CSV file operations. It demonstrates my skills in backend programming, database design, and efficient data handling. This project can be easily scaled or modified to add more features.
## Features
  <ul>
  <li>Dynamic Quiz Management: Questions and student details are loaded dynamically from CSV files.</li>
  <li>Database Integration: Uses SQLite for secure data storage of quiz questions, user credentials, and results.</li>
  <li>Interactive Command-Line Interface: User-friendly CLI to log in and take quizzes.</li>
  <li>Grade Tracking: Keeps a record of quiz results in a database.</li>
  <li>Robust Error Handling: Manages exceptions to ensure smooth operations.</li>
  </ul>
  
## Technology_Stack
  <ul>
  <li>Programming Language: Python</li>
  <li>Database: SQLite</li>
  <li>CSV Management: Python csv module</li>
  <li>Database API: Python’s built-in sqlite3</li>
  </ul>

## Project Structure

```plaintext
Project Directory
│
├── Class Roster.csv            # CSV file containing student credentials
├── Quiz Questions.csv          # CSV file containing quiz questions
├── QuizquestionsDB.sqlite      # SQLite database for storing application data
├── db_base.py                  # Base class for database operations
├── PythonQuizcode-final.py     # Main program logic for running the quiz
├── db_base.cpython-313.pyc     # Compiled Python file for db_base.py
└── README.md                   # Documentation of the project
```
# How to Run
1. **Clone the Repository**
Clone the repository to your local system using:
```bash
git clone https://github.com/OMKARSAI-M/QuizApp.git
cd QuizApp
```
2. **Setup Dependencies**
Ensure Python 3.9+ is installed on your system. No additional packages are required.

3. **Prepare the Database**
The database is created automatically when the program runs. It reads data from the CSV files (Class Roster.csv and Quiz Questions.csv).
4.**Run the Application**
Execute the main script:
```bash
python PythonQuizcode-final.py
```
5. **Take the Quiz**
<ul>
<li>Enter your username and password (loaded from Class Roster.csv).</li>
<li>Answer 5 randomly selected quiz questions.</li>
<li>View your score, which is saved in the database.</li>
</ul>
