def manage_family_member(family, name):
    while True:
        action = input("(U)pdate, (R)emove, (Q)uit, (P)rint list: ").lower()

        if action in ['u', 'update']:
            new_name = input("Enter the new name: ").strip().lower()
            try:
                index = family.index(name)
                family[index] = new_name
                name = new_name  # Update local name as well
                print("Update successful!")
            except ValueError:
                print(f"Couldn't find '{name}' in the family. Please try again.")
        elif action in ['r', 'remove']:
            try:
                family.remove(name)
                print("Name deleted!")
            except ValueError:
                print(f"Couldn't find '{name}' in the family. Please try again.")
        elif action in ['p', 'print']:
            print("Updated list of names:")
            for member in family:
                print(member.title())  # Print each name with proper capitalization
        elif action in ['q', 'quit']:
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    family = ["adam", "anas", "salma", "houda", "omar"]

    while True:
        name = input("Enter Your Name: ").strip().lower()

        if name in family:
            print(f"Welcome back, {name.title()}")
            manage_family_member(family, name)
            break  # Exit after managing the found member
        else:
            print("Sorry, you're not currently a family member.")

        if input("Do you want to continue? (y/n): ").lower() not in ['y', 'yes']:
            break

if __name__ == "__main__":
    main()
