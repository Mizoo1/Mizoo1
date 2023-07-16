import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Willkommen zu meinem Ratespiel! Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?")

    while True:
        try:
            user_guess = int(input("Gib deine Vermutung ein: "))
            attempts += 1

            if user_guess == secret_number:
                print(f"Glückwunsch! Du hast die Zahl {secret_number} in {attempts} Versuchen erraten!")
                break
            elif user_guess < secret_number:
                print("Die Zahl ist größer als deine Vermutung. Versuche es erneut.")
            else:
                print("Die Zahl ist kleiner als deine Vermutung. Versuche es erneut.")
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

if __name__ == "__main__":
    guess_number()
