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
# Sample Quiz Question
Below are a few sample quiz questions included in the project:

| Question                                   | Option 1    | Option 2    | Option 3    | Option 4    | Correct Answer |
|-------------------------------------------|-------------|-------------|-------------|-------------|----------------|
| What is the capital of France?            | Paris       | London      | Berlin      | Madrid      | Paris          |
| What is 2 + 2?                             | 3           | 4           | 5           | 6           | 4              |
| Who wrote "To Kill a Mockingbird"?        | Harper Lee  | Mark Twain  | J.K. Rowling| Jane Austen | Harper Lee     |
| What is the largest planet in our solar system? | Mars    | Earth       | Jupiter     | Saturn      | Jupiter        |


# How to Run
1. **Clone the Repository**
Clone the repository to your local system using:
```bash
git clone https://github.com/OMKARSAI-M/Quiz_Application_with_Database_Integration.git
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
  
# How It Works
1. **Database Initialization**
The CsvLab class initializes the SQLite database, creates tables, and resets existing data.
Tables:
  <ul>
  <li>QuizQuestions: Stores quiz data.</li>
  <li>ClassRoster: Manages user credentials.</li>
  <li>Gradebook: Tracks quiz performance.</li>
  </ul>
  
2. **CSV File Parsing**
Quiz questions and user credentials are parsed from the Quiz Questions.csv and Class Roster.csv files respectively.

3. **Interactive Quiz** 
Users log in using credentials. Random questions are presented, and the program tracks and stores results.

4. **Error Handling**
Comprehensive error handling ensures a seamless user experience even with unexpected inputs.

# Code Highlights
## Database Base Class
Efficient abstraction for database operations:
```bash
class DBbase:
    def __init__(self, db_name):
        self._conn = sqlite3.connect(db_name)
        self._cursor = self._conn.cursor()
```
## Quiz Execution Logic
Dynamic question retrieval and grading:
```bash
def run_quiz(self):
    random.shuffle(self.quiz_questions_list)
    for item in quiz_questions:
        print(f"Question: {item.Question}")
```
# Future Enhancements
<ul>
<li>Add GUI using frameworks like Tkinter or PyQt.</li>
<li>Introduce timer-based quizzes.</li>
<li>Implement user registration and admin dashboard.</li>
<li>Support export of gradebook data to CSV or Excel.</li>
</ul>

# Contributors
<li>Omkar (GitHub: OMKARSAI-M)</li>
Feel free to reach out for collaboration or suggestions!
