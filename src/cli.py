# MediGuide - Command Line Interface
# Educational project for basic rule-based symptom matching


diseases = {
    "Respiratory": {
        "Common Cold": [
            "Cough",
            "Runny Nose",
            "Sneezing",
            "Sore Throat"
        ],
        "Influenza": [
            "Fever",
            "Cough",
            "Headache",
            "Muscle Pain",
            "Fatigue"
        ],
        "Asthma": [
            "Wheezing",
            "Shortness of Breath",
            "Chest Tightness",
            "Cough"
        ],
        "Bronchitis": [
            "Cough",
            "Mucus",
            "Fatigue",
            "Chest discomfort"
        ],
        "Pneumonia": [
            "Cough",
            "Fever",
            "Chest Pain",
            "Shortness of Breath"
        ]
    },

    "Digestive": {
        "Indigestion": [
            "Stomach discomfort",
            "Heartburn",
            "Bloating"
        ],
        "Food Poisoning": [
            "Stomach Pain",
            "Nausea",
            "Diarrhea",
            "Vomiting"
        ],
        "Gastritis": [
            "Stomach Pain",
            "Nausea",
            "Bloating",
            "Indigestion"
        ]
    },

    "Skin": {
        "Acne": [
            "Pimples",
            "Blackheads",
            "Oily Skin"
        ],
        "Eczema": [
            "Itchy Skin",
            "Dry Skin",
            "Red Skin",
            "Rash"
        ],
        "Ringworm": [
            "Itchy Skin",
            "Circular Rash",
            "Red Skin"
        ]
    }
}


def get_symptoms(category):
    """Return all unique symptoms for a category."""

    symptoms = set()

    for disease_symptoms in diseases[category].values():
        symptoms.update(disease_symptoms)

    return sorted(symptoms)


def analyse_symptoms(category, selected_symptoms):
    """Compare selected symptoms with the predefined disease data."""

    results = {}

    for disease, disease_symptoms in diseases[category].items():

        matching_symptoms = (
            set(selected_symptoms) & set(disease_symptoms)
        )

        percentage = (
            len(matching_symptoms) /
            len(disease_symptoms)
        ) * 100

        results[disease] = percentage

    return results


def symptom_analysis():
    """Run the command-line symptom analysis."""

    print("\n===================================")
    print("       MEDIGUIDE SYMPTOM ANALYSIS")
    print("===================================")

    print("\nSelect a category:")
    print("1. Respiratory")
    print("2. Digestive")
    print("3. Skin")

    choice = input("\nEnter your choice: ").strip()

    categories = {
        "1": "Respiratory",
        "2": "Digestive",
        "3": "Skin"
    }

    if choice not in categories:
        print("\nInvalid choice.")
        return

    category = categories[choice]

    print(f"\n--- {category} Symptoms ---")

    symptoms = get_symptoms(category)

    for number, symptom in enumerate(symptoms, start=1):
        print(f"{number}. {symptom}")

    user_input = input(
        "\nEnter symptom numbers separated by commas: "
    ).strip()

    if not user_input:
        print("\nNo symptoms were selected.")
        return

    try:
        numbers = [
            int(number.strip())
            for number in user_input.split(",")
        ]
    except ValueError:
        print("\nInvalid input. Please enter numbers only.")
        return

    selected_symptoms = []

    for number in numbers:

        if 1 <= number <= len(symptoms):
            selected_symptoms.append(symptoms[number - 1])
        else:
            print(f"Warning: symptom number {number} is invalid.")

    if not selected_symptoms:
        print("\nNo valid symptoms were selected.")
        return

    print("\nSelected symptoms:")

    for symptom in selected_symptoms:
        print(f"- {symptom}")

    results = analyse_symptoms(
        category,
        selected_symptoms
    )

    print("\n===================================")
    print("             RESULTS")
    print("===================================")

    for disease, percentage in results.items():
        print(f"{disease}: {percentage:.1f}%")

    print("\n-----------------------------------")
    print("IMPORTANT:")
    print(
        "These results are produced by a simple "
        "rule-based educational program."
    )
    print(
        "They are NOT a medical diagnosis and "
        "should not replace professional medical advice."
    )


def health_information():

    print("\n===================================")
    print("        GENERAL HEALTH INFORMATION")
    print("===================================")

    print("""
1. Maintain a balanced diet.

2. Drink adequate water according to
   your individual needs.

3. Maintain regular physical activity.

4. Get adequate sleep.

5. Maintain good personal hygiene.

6. Avoid smoking and harmful substances.

7. Seek professional medical advice when
   symptoms are severe, persistent, or concerning.

Emergency symptoms such as severe difficulty
breathing, severe chest pain, loss of consciousness,
or other serious conditions require prompt
medical attention.
""")


def about():

    print("\n===================================")
    print("              MEDIGUIDE")
    print("===================================")

    print("""
Personal Health Information Assistant

MediGuide is a Python educational project
designed to demonstrate:

- Python programming
- Functions
- Dictionaries
- Lists and sets
- Input validation
- Rule-based symptom matching
- Command-line interaction

The program is intended only for educational
demonstration and should not be used for
medical diagnosis.
""")


def main():

    while True:

        print("\n===================================")
        print("             MEDIGUIDE")
        print("===================================")

        print("\n1. Symptom Analysis")
        print("2. Health Information")
        print("3. About MediGuide")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            symptom_analysis()

        elif choice == "2":
            health_information()

        elif choice == "3":
            about()

        elif choice == "4":
            print("\nThank you for using MediGuide.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
