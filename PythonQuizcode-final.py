import db_base as db
import csv
import random


class QuizQuestion:
    # Question,Answer Option 1,Answer Option 2,Answer Option 3,Answer Option 4,Correct Answer
    def __init__(self, row):
        self.Question = row[0]
        self.Answer_Option_1 = row[1]
        self.Answer_Option_2 = row[2]
        self.Answer_Option_3 = row[3]
        self.Answer_Option_4 = row[4]
        self.Correct_Answer = row[5]


class ClassRoster:
    # Username, Password
    def __init__(self, row):
        self.student_id = row[0]
        self.Password = row[1]


class CsvLab(db.DBbase):

    def reset_or_create_db(self):

        try:
            sql = """
                    DROP TABLE IF EXISTS QuizQuestions;
                    DROP TABLE IF EXISTS ClassRoster;
                    DROP TABLE IF EXISTS Gradebook;

                    CREATE TABLE QuizQuestions(
                        id INTEGER PRIMARY KEY,
                        Question TEXT,
                        Answer_Option_1 TEXT,
                        Answer_Option_2 TEXT,
                        Answer_Option_3 TEXT,
                        Answer_Option_4 TEXT,
                        Correct_Answer INTEGER
                    );

                    CREATE TABLE ClassRoster(
                        id INTEGER PRIMARY KEY,
                        student_id TEXT UNIQUE,
                        password TEXT
                    );
                    
                    CREATE TABLE Gradebook(
                        id INTEGER PRIMARY KEY,
                        student_id TEXT UNIQUE,
                        num_questions TEXT,
                        num_correct TEXT
                    );
                """
            super().execute_script(sql)
        except Exception as e:
            print(e)

    def read_quiz_data(self, file_name):
        self.quiz_questions_list = []

        try:
            with open(file_name, 'r') as record:
                csv_contents = csv.reader(record)
                next(record)
                for row in csv_contents:
                    quiz = QuizQuestion(row)
                    self.quiz_questions_list.append(quiz)

        except Exception as e:
            print(e)

    def read_class_roster(self, file_name):
        self.class_roster_list = []

        try:
            with open(file_name, 'r') as record:
                csv_contents = csv.reader(record)
                next(record)
                for row in csv_contents:
                    student = ClassRoster(row)
                    self.class_roster_list.append(student)

        except Exception as e:
            print(e)

    def save_to_database(self):
        # print("Number of quiz records to save: ", len(self.quiz_questions_list))
        # print("Number of students to save to roster: ", len(self.class_roster_list))
        # print("Number of students to save to gradebook: ", len(self.class_roster_list))
        #
        # save = input("Continue? (Y/N) ").lower()

        # if save == "y":
        for item in self.quiz_questions_list:
            try:
                super().get_cursor.execute("""INSERT INTO QuizQuestions
                (Question, Answer_Option_1, Answer_Option_2, Answer_Option_3, Answer_Option_4, Correct_Answer)
                    VALUES(?, ?, ?, ?, ?, ?)""",
                    (item.Question, item.Answer_Option_1, item.Answer_Option_2, item.Answer_Option_3,
                     item.Answer_Option_4, item.Correct_Answer))

                super().get_connection.commit()

                # print("Saved quiz item: ", item.Question, item.Answer_Option_1, item.Answer_Option_2)
            except Exception as e:
                print(e)

        for item in self.class_roster_list:
            try:
                super().get_cursor.execute("""INSERT INTO ClassRoster
                        (student_id, password)
                            VALUES(?, ?)""",
                                           (item.student_id, item.Password))

                super().get_connection.commit()

                # print("Saved student to roster: ", item.student_id)
            except Exception as e:
                print(e)

        for item in self.class_roster_list:
            try:
                super().get_cursor.execute("""INSERT INTO Gradebook
                                   (student_id) VALUES(?)""", (item.student_id,))

                super().get_connection.commit()

                # print("Saved student to Gradebook: ", item.student_id)
            except Exception as e:
                print(e)

        # else:
        #     print("Save to DB aborted")

    def run_quiz(self):
        # Prompt user for username and password
        student_id = str(input("Student ID: "))
        password = str(input("Password: "))

        # Check if student exists in the database
        super().get_cursor.execute("SELECT id FROM ClassRoster WHERE student_id = ? AND password = ?",
                                   (student_id, password))
        result = super().get_cursor.fetchone()
        if result is None:
            print("Invalid username or password. Quiz aborted.")
            return

        # Student is authenticated, continue with quiz
        student_id = result[0]
        num_questions = 5
        correct_answers = 0

        # Shuffle the list of questions
        random.shuffle(self.quiz_questions_list)

        # Select the first X questions (set by num_questions) from the shuffled list
        quiz_questions = self.quiz_questions_list[:num_questions]

        for i, item in enumerate(quiz_questions):
            print(f"Question {i + 1}/{num_questions}: {item.Question}")
            print(f"1. {item.Answer_Option_1}")
            print(f"2. {item.Answer_Option_2}")
            print(f"3. {item.Answer_Option_3}")
            print(f"4. {item.Answer_Option_4}")

            user_answer = input("Enter your answer (1-4): ")
            if user_answer == item.Correct_Answer:
                correct_answers += 1
                print("Correct!")
            else:
                print("Incorrect.")

        # Update the results in the Gradebook
        try:
            super().get_cursor.execute("UPDATE Gradebook SET num_questions = ?, num_correct = ? WHERE student_id = ?",
                                       (num_questions, correct_answers, student_id))
            super().get_connection.commit()
            print("Quiz results saved.")
        except Exception as e:
            print(e)

        print(f"\nQuiz complete. You got {correct_answers} out of {num_questions} questions correct.")


csv_lab = CsvLab("QuizquestionsDB.sqlite")
csv_lab.reset_or_create_db()
csv_lab.read_quiz_data("Quiz Questions.csv")
csv_lab.read_class_roster("Class Roster.csv")
csv_lab.save_to_database()
csv_lab.run_quiz()
