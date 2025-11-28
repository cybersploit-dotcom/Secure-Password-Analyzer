import logic
import sys

def show_menu():
    print("\n--- CYBER SECURITY PASSWORD TOOL ---")
    print("1. Analyze a Password")
    print("2. Generate a Secure Password")
    print("3. View Saved Passwords")
    print("4. Exit")

def main():
    while True:
        show_menu()
        try:
            choice = input("Enter choice (1-4): ")
            
            if choice == '1':
                pwd = input("Enter password to test: ")
                strength, tips = logic.check_strength(pwd)
                print(f"Result: {strength}")
                if tips: print(f"Tips: {', '.join(tips)}")
                
            elif choice == '2':
                length = int(input("Enter length (default 12): ") or 12)
                new_pass = logic.generate_password(length)
                print(f"Generated: {new_pass}")
                save = input("Save to history? (y/n): ")
                if save.lower() == 'y':
                    logic.save_to_file(new_pass)
                    print("Saved!")

            elif choice == '3':
                print("--- History ---")
                try:
                    with open("history.txt", "r") as f:
                        print(f.read())
                except FileNotFoundError:
                    print("No history found.")

            elif choice == '4':
                print("Exiting...")
                sys.exit()
            
            else:
                print("Invalid choice, try again.")
                
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()