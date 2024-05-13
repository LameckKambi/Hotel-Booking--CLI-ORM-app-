from models import Hotel, Booking, create_tables, engine
from sqlalchemy.orm import sessionmaker
from datetime import date

Session = sessionmaker(bind=engine)

def main():
    create_tables()
    session = Session()

    while True:
        print("\nWelcome to the Hotel Booking System!")
        print("1. Create a Hotel")
        print("2. List Hotels")
        print("3. Create a Booking")
        print("4. List Bookings")
        print("5. Exit")
        print("6. Update a Hotel")
        print("7. Delete a Hotel")
        print("8. Delete a Booking")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            name = input("Enter hotel name: ")
            address = input("Enter hotel address: ")
            hotel = Hotel.create(session, name, address)
            print(f"Hotel created: {hotel}")

        elif choice == "2":
            hotels = Hotel.get_all(session)
            if hotels:
                for hotel in hotels:
                    print(hotel)
            else:
                print("No hotels found.")

        elif choice == "3":
            hotel_id = int(input("Enter hotel ID: "))
            hotel = Hotel.find_by_id(session, hotel_id)
            if hotel:
                check_in = input("Enter check-in date (YYYY-MM-DD): ")
                check_out = input("Enter check-out date (YYYY-MM-DD): ")
                try:
                    check_in_date = date.fromisoformat(check_in)
                    check_out_date = date.fromisoformat(check_out)
                    bookings = Booking.get_all(session)
                    hotel_bookings = [b for b in bookings if b.hotel_id == hotel_id]
                    if any(b.check_in <= check_in_date < b.check_out or b.check_in < check_out_date <= b.check_out for b in hotel_bookings):
                        print("Sorry, the hotel is fully booked for the given dates.")
                    elif Booking.check_availability(session, hotel_id, check_in_date, check_out_date):
                        booking = Booking.create(session, hotel_id, check_in_date, check_out_date)
                        print(f"Booking created: {booking}")
                    else:
                        print("Sorry, the hotel is not available for the given dates.")
                except ValueError:
                    print("Invalid date format. Please enter dates in YYYY-MM-DD format.")
            else:
                print(f"Hotel with ID {hotel_id} not found.")

        elif choice == "4":
            bookings = Booking.get_all(session)
            if bookings:
                for booking in bookings:
                    print(booking)
            else:
                print("No bookings found.")

        elif choice == "5":
            print("Goodbye!")
            break

        elif choice == "6":
            hotel_id = int(input("Enter hotel ID: "))
            hotel = Hotel.find_by_id(session, hotel_id)
            if hotel:
                new_name = input(f"Enter new name (current: {hotel.name}), or leave blank to keep the same: ")
                new_address = input(f"Enter new address (current: {hotel.address}), or leave blank to keep the same: ")
                updated_hotel = Hotel.update(session, hotel, new_name or None, new_address or None)
                print(f"Hotel updated: {updated_hotel}")
            else:
                print(f"Hotel with ID {hotel_id} not found.")

        elif choice == "7":
            hotel_id = int(input("Enter hotel ID: "))
            hotel = Hotel.find_by_id(session, hotel_id)
            if hotel:
                confirm = input(f"Are you sure you want to delete '{hotel.name}' (y/n)? ")
                if confirm.lower() == "y":
                    Hotel.delete(session, hotel)
                    print(f"Hotel '{hotel.name}' has been deleted.")
                else:
                    print("Hotel deletion canceled.")
            else:
                print(f"Hotel with ID {hotel_id} not found.")

        elif choice == "8":
            booking_id = int(input("Enter booking ID: "))
            booking = Booking.find_by_id(session, booking_id)
            if booking:
                confirm = input(f"Are you sure you want to delete booking {booking.id} (y/n)? ")
                if confirm.lower() == "y":
                    Booking.delete(session, booking)
                    print(f"Booking {booking.id} has been deleted.")
                else:
                    print("Booking deletion canceled.")
            else:
                print(f"Booking with ID {booking_id} not found.")

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()