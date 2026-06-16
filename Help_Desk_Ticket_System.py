tickets = []
ticket_id = 1000

while True:
    print("\n=== Darwin Help Desk Ticket System ===")
    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Search Ticket")
    print("4. Close Ticket")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Employee Name: ")
        issue = input("Issue Description: ")

        ticket = {
            "id": ticket_id,
            "name": name,
            "issue": issue,
            "status": "Open"
        }

        tickets.append(ticket)

        print(f"Ticket #{ticket_id} Created")
        ticket_id += 1

    elif choice == "2":
        if len(tickets) == 0:
            print("No tickets found")
        else:
            for ticket in tickets:
                print("\n------------------")
                print("Ticket ID:", ticket["id"])
                print("Employee:", ticket["name"])
                print("Issue:", ticket["issue"])
                print("Status:", ticket["status"])

    elif choice == "3":
        search_id = int(input("Enter Ticket ID: "))

        found = False

        for ticket in tickets:
            if ticket["id"] == search_id:
                print("\nTicket Found")
                print("Employee:", ticket["name"])
                print("Issue:", ticket["issue"])
                print("Status:", ticket["status"])
                found = True

        if not found:
            print("Ticket Not Found")

    elif choice == "4":
        close_id = int(input("Enter Ticket ID to Close: "))

        found = False

        for ticket in tickets:
            if ticket["id"] == close_id:
                ticket["status"] = "Closed"
                print("Ticket Closed")
                found = True

        if not found:
            print("Ticket Not Found")

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid Option")

print("Created by Darwin Brown")