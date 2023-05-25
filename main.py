from functions import *

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. All quotes")
    print("4. Add quote")

def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()

        choice = input("Choose your an action (1-3): ")
        
        if choice == "1":
            print_quote(random_quote(quotes))
        elif choice == "2":
            view_quotes(quotes)
        elif choice == "4":
            filename = input("Enter a filename: ")
            add_quote(quotes, filename)
        else:
            print("Invalid input")

if "__main__" == __name__ :
    main()