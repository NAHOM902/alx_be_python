from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        # Prompt the user for the number of days
        days_to_add = input("Enter the number of days to add to the current date: ")
        if not days_to_add.isdigit():
            raise ValueError("Invalid input. Please enter a valid integer.")
        
        days_to_add = int(days_to_add)
        # Get the current date
        current_date = datetime.now()
        # Calculate the future date
        future_date = current_date + timedelta(days=days_to_add)
        # Format the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError as e:
        print(e)

# Main Program
if __name__ == "__main__":
    # Display the current date and time
    display_current_datetime()
    # Calculate and display the future date
    calculate_future_date()
