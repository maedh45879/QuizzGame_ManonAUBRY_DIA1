def quiz_histoire_france():
    # Définir les questions et réponses
    questions = [
        {
            "question": "En quelle année a eu lieu la Révolution française ?",
            "options": ["A. 1789", "B. 1799", "C. 1776"],
            "answer": "A"
        },
        {
            "question": "Qui était le roi de France pendant la Révolution française ?",
            "options": ["A. Louis XIV", "B. Louis XVI", "C. Louis XVIII"],
            "answer": "B"
        },
        {
            "question": "Quelle bataille Napoléon a-t-il perdue en 1815 ?",
            "options": ["A. La bataille d'Austerlitz", "B. La bataille de Waterloo", "C. La bataille de Trafalgar"],
            "answer": "B"
        },
        {
            "question": "Quel roi a été surnommé 'le Roi-Soleil' ?",
            "options": ["A. Louis XIII", "B. Louis XV", "C. Louis XIV"],
            "answer": "C"
        },
        {
            "question": "Quelle est la date de la fin de la Première Guerre mondiale ?",
            "options": ["A. 11 novembre 1918", "B. 8 mai 1945", "C. 14 juillet 1789"],
            "answer": "A"
        }
    ]

    score = 0  # Initialiser le score

    print("Bienvenue au Quiz sur l'Histoire de France !")
    print("------------------------------------------")

    # Parcourir les questions
    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1}: {question['question']}")
        for option in question['options']:
            print(option)

        # Récupérer la réponse de l'utilisateur
        user_answer = input("Votre réponse (A, B ou C) : ").strip().upper()

        # Vérifier si la réponse est correcte
        if user_answer == question['answer']:
            print("Bonne réponse !")
            score += 1
        else:
            print(f"Mauvaise réponse ! La bonne réponse était {question['answer']}.")

    # Afficher le score final
    print("\nQuiz terminé !")
    print(f"Votre score final est : {score}/{len(questions)}")

# Lancer le quiz
if __name__ == "__main__":
    quiz_histoire_france()
