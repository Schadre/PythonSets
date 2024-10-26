our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def finding_destinations():
    same = our_routes.intersection(competitor_routes)
    print(f"Destinations both airlines fly to: {same}")

def unqiue_destinations():
    unqiue = our_routes.difference(competitor_routes)
    print(f"Destinations unique to our airline: {unqiue}")

def no_connection():
    difference = our_routes.symmetric_difference(competitor_routes)
    print(difference)

while True:
    print("\nWelcome to the Python Sets Adventure")
    print("1. Find destinations that both airlines fly to ")
    print("2. Find destinations unique to your airline")
    print("3. Find if there are any destinations that neither airline shares")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        finding_destinations()
    elif choice == "2":
        unqiue_destinations()
    elif choice == "3":
        no_connection()
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice. Please try again. ")