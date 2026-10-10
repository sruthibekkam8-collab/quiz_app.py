import time

# Question Bank
quiz_data = [
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. def", "C. create", "D. func"],
        "answer": "B"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A. .pyt", "B. .pt", "C. .py", "D. .pyw"],
        "answer": "C"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "What will be the output of print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which built-in function returns the length of a list?",
        "options": ["A. len()", "B. count()", "C. size()", "D. length()"],
        "answer": "A"
    }
]

def run_quiz():
    print("=" * 50)
    print("        WELCOME TO THE PYTHON QUIZ APPLICATION        ")
    print("=" * 50)
    
    student_name = input("\nEnter your full name: ").strip()
    if not student_name:
        student_name = "Student"
        
    score = 0
    total_questions = len(quiz_data)
    
    print(f"\nHello {student_name}! Starting the quiz...\n")
    time.sleep(1)

    for idx, q in enumerate(quiz_data, start=1):
        print("-" * 50)
        print(f"Question {idx}: {q['question']}")
        for opt in q['options']:
            print(f"  {opt}")
            
        user_ans = input("\nYour answer (A, B, C, or D): ").strip().upper()
        
        while user_ans not in ["A", "B", "C", "D"]:
            user_ans = input("Invalid option! Please enter A, B, C, or D: ").strip().upper()
            
        if user_ans == q['answer']:
            print(" Correct!")
            score += 1
        else:
            print(f" Incorrect. The correct answer was {q['answer']}.")
            
    print("\n" + "=" * 50)
    percentage = (score / total_questions) * 100
    print(f"QUIZ COMPLETED! {student_name.upper()}'S RESULT:")
    print(f"Score: {score} / {total_questions}")
    print(f"Percentage: {percentage:.1f}%")
    
    status = "PASSED" if percentage >= 60 else "NEEDS IMPROVEMENT"
    print(f"Status: {status}")
    print("=" * 50)

    # Export score summary to a local file
    report_filename = f"{student_name.replace(' ', '_')}_quiz_result.txt"
    with open(report_filename, "w") as file:
        file.write("=== QUIZ PERFORMANCE REPORT ===\n")
        file.write(f"Student Name: {student_name}\n")
        file.write(f"Score: {score}/{total_questions}\n")
        file.write(f"Percentage: {percentage:.1f}%\n")
        file.write(f"Status: {status}\n")
        
    print(f"\n[INFO] Score report saved to '{report_filename}'")

if __name__ == "__main__":
    run_quiz()