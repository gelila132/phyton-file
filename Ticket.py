""""4)	 Movie Ticket Booking Simulation
-	Simulate a movie theater booking system that:
•	Shows a list of available movie titles, showtimes, and seat prices.
•	Asks the user to choose a movie and number of tickets.
•	Confirms total price and asks if they want to book another movie.
•	Ends when they say "no" and displays total bookings and cost."""

def cinema_booking_ethiopia():
    # Local movies, times (24hr), and prices in ETB
    movies = {
        "1": {"title": "Adababay (አደባባይ)", "time": "14:00", "price": 150},
        "2": {"title": "Lamba (ላምባ)", "time": "16:30", "price": 200},
        "3": {"title": "Sostu (ሦስቱ)", "time": "19:00", "price": 180}
    }
    
    total_cost = 0
    bookings = []

    print("--- Welcome to Cinema Ethiopia ---")
    
    while True:
        for k, m in movies.items():
            print(f"{k}. {m['title']} | {m['time']} | {m['price']} ETB")
        
        choice = input("\nSelect movie number: ")
        if choice in movies:
            movie = movies[choice]
            try:
                count = int(input(f"How many tickets for {movie['title']}? "))
                if count > 0:
                    cost = count * movie['price']
                    confirm = input(f"Total is {cost} ETB. Confirm? (y/n): ").lower()
                    
                    if confirm == 'y':
                        total_cost += cost
                        bookings.append(f"{count}x {movie['title']}")
                        print("Successfully booked!")
            except ValueError:
                print("Please enter a valid number.")
        
        if input("\nBook another? (y/n): ").lower() != 'y':
            break

    print("\n--- Final Summary ---")
    for b in bookings: print(f"- {b}")
    print(f"Total Amount: {total_cost} ETB\nEnamesegenalen (Thank you)!")

cinema_booking_ethiopia()