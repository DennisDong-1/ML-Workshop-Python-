# 🔧 Student Score Tracker CLI App
# A terminal-based app that:
#   Takes student names and subject scores
#   Calculates average, highest, lowest scores
#   Allows searching for a student
#   Saves and loads data from a file

import os
import json
from statistics import mean

class StudentScoreTracker:
    def __init__(self):
        self.students = {}
        self.data_file = "studentScores.txt"
        self.load_data()

    def display_menu(self):
        print("STUDENT SCORE TRACKER")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student Statistics")
        print("4. Search for a Student")
        print("5. Save Data")
        print("6. Exit")

    def add_student(self):
        name = input("Enter student name: ").strip()
        if name in self.students:
            print(f"{name} already exists!")
            return
        
        subjects = {}
        while True:
            subject = input("Enter subject name (or 'exit' if finished): ").strip()
            if subject.lower() == 'exit':
                break
            try:
                score = float(input("Enter score for {subject}: "))
                if score < 0 or score > 100:
                    print("Score must be between 0 and 100")
                    continue
                subjects[subject] = score
            except ValueError:
                print("Invalid score. Please enter a number.")

        if subjects:
            self.students[name] = subjects
            print(f"{name} added successfully!")
        else:
            print("No subjects added. Student not created.")

    def view_all_students(self):
        if not self.students:
            print("No students in the database.")
            return
        
        print("The students we have are: ")
        for name, subjects in self.students.items():
            print(f"\n {name}")
            for subject, score in subjects.items():
                print(f"    {subject}: {score}")

    def calculate_stats(self, scores):
        if not scores:
            return None, None, None
        return min(scores), max(scores), mean(scores)
    
    def view_stats(self):
        if not self.students:
            print("No students in the database.")
            return
        
        all_scores = [score for subjects in self.students.values() for score in subjects.values()]
        min_score, max_score, avg_score = self.calculate_stats(all_scores)
        print("OVERALL STATISTICS: ")
        print(f"Total students: {len(self.students)}")
        print(f"Lowest score: {min_score}")
        print(f"Highest score: {max_score}")
        print(f"Average score: {avg_score}")

    def search_student(self):
        name = input("Enter student name to search: ").strip()
        if name in self.students:
            print(f"\n Found {name}")
            for subject, score in self.students[name].items():
                print(f" {subject}: {score}")
        else:
            print(f"{name} not found in records.")

    def save_data(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.students, f)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.students = json.load(f)
                print("Data loaded successfully!")
            except Exception as e:
                print(f"Error loading data: {e}")
                self.students = {}
        else:
            self.students = {}

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.view_stats()
            elif choice == '4':
                self.search_student()
            elif choice == '5':
                self.save_data()
            elif choice == '6':
                self.save_data()
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    app = StudentScoreTracker()
    app.run()