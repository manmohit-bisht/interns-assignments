#fmt: off
import re

questions = []
answers = []
with open("questions.txt", "r", encoding="utf-8") as file:
    for line in file:
        question = line.strip()
        if not question:
            continue

        question = question.rstrip("=").strip()  # to remove the last character i.e "="
        formatted_question = (
            question.replace("^", "**")
            .replace("{", "(")
            .replace("}", ")")
            .replace("[", "(")
            .replace("]", ")")
        )
        # formatting below is for implicit multiplication, e.g. 2(3+4) => 2*(3+4)
        formatted_question = re.sub(r"\)\s*\(", ")*(", formatted_question)
        formatted_question = re.sub(r"(\d)\s*\(", r"\1*(", formatted_question)
        formatted_question = re.sub(r"\)\s*(\d)", r")*\1", formatted_question)

        questions.append(question)  # appended the original question without formatting, so that it can be printed in the answers.txt file as it originally was in the questions.txt file
        print(repr(formatted_question))
        answers.append(eval(formatted_question))


with open("answers.txt", "w", encoding="utf-8") as file:
    for i in range(len(questions)):
        file.write(f"{questions[i]} = {answers[i]}\n")
