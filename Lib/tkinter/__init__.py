import tkinter as tk

# Questions and answers
questions = [
    {"question": "1️⃣ What is an example of a network?", "answer": "lan"},
    {"question": "2️⃣ What does LAN stand for?", "answer": "local area network"},
    {"question": "3️⃣ Name one place where a LAN might be used:", "answer": ["house", "home", "office"]},
    {"question": "4️⃣ Why is LAN used in places like homes or offices?", "keywords": ["small", "area"]}
]

current_question = 0

def check_answer():
    global current_question
    user_input = entry.get().strip().lower()
    entry.delete(0, tk.END)

    correct = False

    if "answer" in questions[current_question]:
        correct_answer = questions[current_question]["answer"]
        if isinstance(correct_answer, list):
            if user_input in correct_answer:
                correct = True
        else:
            if user_input == correct_answer:
                correct = True

    elif "keywords" in questions[current_question]:
        correct = all(keyword in user_input for keyword in questions[current_question]["keywords"])

    if correct:
        feedback_label.config(text="✅ Correct!", fg="green")
        current_question += 1
        if current_question < len(questions):
            question_label.config(text=questions[current_question]["question"])
        else:
            question_label.config(text="🎉 You completed the challenge!")
            submit_button.config(state="disabled")
    else:
        feedback_label.config(text="❌ Incorrect. Try again.", fg="red")


# Create the window
window = tk.Tk()
window.title("Challenging Learning")
window.geometry("500x250")

# Question Label
question_label = tk.Label(window, text=questions[0]["question"], font=("Arial", 14), wraplength=400)
question_label.pack(pady=20)

# Entry box
entry = tk.Entry(window, font=("Arial", 14))
entry.pack()

# Submit button
submit_button = tk.Button(window, text="Submit", command=check_answer, font=("Arial", 12))
submit_button.pack(pady=10)

# Feedback label
feedback_label = tk.Label(window, text="", font=("Arial", 12))
feedback_label.pack()

# Run the app
window.mainloop()
